"""
Calculator library containing basic math operations.
"""
def sum_numbers(*args):
    s = 0
    for i in args:
        s = s+i
    return s


def multiply_numbers(*args):
    s = 1
    for i in args:
        s = s*i
    return s

def subtract(first_term, second_term):
    return first_term - second_term