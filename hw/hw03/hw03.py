def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    if n <= 3:
        return n
    else:
        return g(n-1) + 2*g(n-2) + 3*g(n-3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    if n <= 3:
        return n
    else:
        g1, g2, g3 = 1, 2, 3
        while n > 3:
            g1, g2, g3 = g2, g3, (g3 + (2 * g2) + (3 * g1))
            n = n - 1
        return g3

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    while k:
        k, last = k // 10, k % 10
        if last == 7:
            return True
        else:
            has_seven(k)
    return False

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    def moveAlong(nth, value, MoveRight):
        if nth == n:
            return value
        if MoveRight:
            return switchDirection(nth+1, value+1, MoveRight)
        else:
            return switchDirection(nth+1, value-1, MoveRight)

    def switchDirection(nth, value, MoveRight):
        if nth % 7 == 0 or has_seven(nth):
            return moveAlong(nth, value, not MoveRight)
        else:
            return moveAlong(nth, value, MoveRight)

    return moveAlong(1, 1, True)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """

    def partition_change(smallest_change, amount):
        if amount < 0:
            return 0
        elif amount == 0:
            return 1
        elif smallest_change > amount:
            return 0
        else:
            return partition_change(smallest_change, amount - smallest_change) + partition_change(2 * smallest_change, amount)

    return partition_change(1, amount)

def towers_of_hanoi(n, start, end):
    """Print the moves required to solve the towers of hanoi game, starting
    with n disks on the start pole and finishing on the end pole.

    The game is to assumed to have 3 poles.

    >>> towers_of_hanoi(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> towers_of_hanoi(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> towers_of_hanoi(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 0 < start <= 3 and 0 < end <= 3 and start != end, "Bad start/end"

    def movement(n, start, end, middle):
        if n >= 1:
            movement(n-1, start, middle, end)
            print('Move the top disk from rod', start, 'to rod', end)
            movement(n-1, middle, end, start)

    return movement(n, start, end, middle=6-end-start)



from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
    return 'YOUR_EXPRESSION_HERE'
