"""Required questions for lab 2"""

## Boolean Operators ##

# Q6
def both_positive(x, y):
    """
    Returns True if both x and y are positive.
    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    return x > 0 and y > 0
    

## while Loops ##

# Q9
def factors(n):
    """Prints out all of the numbers that divide `n` evenly.

    >>> factors(20)
    20
    10
    5
    4
    2
    1
    """
    divider = n
    while divider > 0:
        if n % divider == 0:
            print(divider)
            divider = divider - 1
        else:
            divider = divider - 1
    

# Q10
def fib(n):
    """Returns the nth Fibonacci number.

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    >>> fib(6)
    8
    """
    a, b, c = 0, 1, 0
    while c < n:
        a, b, c = b, a + b, c + 1
    return a
