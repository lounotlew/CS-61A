# CS 61A Fall 2014
# Name:
# Login:

def harmonic(x, y):
    """Return the harmonic mean of x and y.

    >>> harmonic(2, 6)
    3.0
    >>> harmonic(1, 1)
    1.0
    >>> harmonic(2.5, 7.5)
    3.75


    """

    if x != 0 and y != 0 and -x != y:
        return 2 / ((1 / x) + (1 / y))
    else:
        print("Cannot divide by zero.")

from math import pi

def pi_fraction(gap):
    """Print the fraction within gap of pi that has the smallest denominator.

    >>> pi_fraction(0.01)
    22 / 7 = 3.142857142857143
    >>> pi_fraction(1)
    3 / 1 = 3.0
    >>> pi_fraction(1/8)
    13 / 4 = 3.25
    >>> pi_fraction(1e-6)
    355 / 113 = 3.1415929203539825


    """
    p, q = 3, 1
    while abs(pi - (p / q)) >= (gap):
        q = q + 1
        p = round(pi * q)
    print(p, '/', q, '=', p/q)

def nearest_two(x):
    """Return the power of two that is nearest to x.

    >>> nearest_two(8)    # 2 * 2 * 2 is 8
    8.0
    >>> nearest_two(11.5) # 11.5 is closer to 8 than 16
    8.0
    >>> nearest_two(14)   # 14 is closer to 16 than 8
    16.0
    >>> nearest_two(2015)
    2048.0
    >>> nearest_two(.1)
    0.125
    >>> nearest_two(0.75) # Tie between 1/2 and 1
    1.0
    >>> nearest_two(1.5)  # Tie between 1 and 2
    2.0


    """
    n = 0
    if x >= 1:
        while x > pow(2, n):
            n = n + 1.0
            if x == pow(2, n):
                return pow(2, n)
                stop
        a, b = pow(2, n), pow(2, n - 1)
        c, d = (a - x), (x - b)
        if c > d:
            return b
            stop
        else:
            return a
            stop
    if x > 0 and x < 1:
        while x < pow(2, n):
            n = n - 1.0
            if x == pow(2, n):
                return pow(2, n)
                stop
        e, f = pow(2, n + 1), pow(2, n)
        g, h = (e - x), (x - f)
        if g < h:
            return e
            stop
        elif g == h:
            return e
            stop
        else:
            return f
            stop
    """Had to add this:
        elif g == h:
            return e
    because without it, the tie breaker didn't work. It seems like the program chooses whatever value is greater when there's a tie.
    """