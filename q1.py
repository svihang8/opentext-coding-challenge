"""
Assumptions Made About the Triangle :
1. Triangle is right angled.
2. Display can be presented as a triangle filled with the character '*'
3. m represents height of triangle and n represents base length of triangle.
4. m and n are valid positive integers, and also define a valid triangle.
5. * represents 1 unit length.
"""


def produce_triangle(m : int, n : int) -> None:
    """
    Function outputs a right angled triangle of dimensions m height and n base width.
    Input:-
    m : int representing height of triangle.
    n : int representing base width of triangle.
    Output:-
    """
    for i in range(1, m + 1):
        print('*' * int(i * n / m))
    return


"""Answer to Coding Test Q1"""
produce_triangle(3, 4)


"""
Test Cases for bonus.
"""
# produce_triangle(3, 5)
# produce_triangle(5, 5)
# produce_triangle(6, 10)
# produce_triangle(4, 8)
# produce_triangle(3, 3)
# produce_triangle(10, 5)
# produce_triangle(8, 20)