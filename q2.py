from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import json

def load_page(url:str) -> str:
    """
    load_page opens a url, waits for it to finish loading (~ 5 seconds),
    and then returns HTML for the url page.
    """
    op = webdriver.ChromeOptions()
    op.add_argument('headless') # avoid opening up chromium testing
    driver = webdriver.Chrome(options=op)
    driver.get(url)
    time.sleep(5) # wait until page loads.
    return driver.page_source

def parser() -> None:
    """
    parser extracts product information from https://www.microfocus.com/en-us/products?trial=true
    and stores it in data.json file as JSON.
    """
    URL:str = "https://www.microfocus.com/en-us/products?trial=true"
    page_content = load_page(URL)
    soup = BeautifulSoup(page_content, 'html.parser')
    products = soup.find_all('div', class_='uk-card')
    
    data = []

    for product in products:
        product_content = product.find('div', class_='uk-card-body')
        title = product_content.find('h3')
        description = product_content.find('div', class_='description')
        cta = product_content.find('div', class_='cta-section')
        product_name = '' # handle edge case where name is missing.
        if title.find('a'):
            product_name = title.find('a').text
        elif title.find('span'):
            product_name = title.find('span').text
        product_description = description.find('p').text
        demo_link = cta.find('a', href=True)['href']
        if demo_link[0] == '/':
            demo_link = 'https://www.microfocus.com' + demo_link
        footer = product.find('div', class_='footer')
        links = {} # storing community and support links
        for a in footer.find_all('a', href=True):
            if a.text == 'Community':
                links['community'] = a['href']
            if a.text == 'Support':
                links['support'] = a['href']
                if links['support'][0] == '/':
                    links['support'] = 'https://www.microfocus.com' + links['support']
        
        data.append({
            'product_name' : product_name,
            'starting_letter': product_name[0],
            'description' : product_description,
            'demo_url': demo_link,
            'support_url' : links.get('support', ''),
            'community_url' : links.get('community', '')
        })

    with open('data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    parser()