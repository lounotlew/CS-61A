#############
# Iterators #
#############

class IteratorRestart:
    """
    >>> i = IteratorRestart(2, 7)
    >>> for item in i:
    ...     print(item)
    2
    3
    4
    5
    6
    7
    >>> for item in i:
    ...     print(item)
    2
    3
    4
    5
    6
    7
    """
    def __init__(self, start, end):
        self.reset = start - 1
        self.start = start - 1
        self.end = end

    def __next__(self):
        if self.start + 1 > self.end:
            self.start = self.reset
            raise StopIteration
        self.start += 1
        return self.start

    def __iter__(self):
        return self

##############
# Generators #
##############

def countdown(n):
    """
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    num = n
    while num >= 0:
        yield num
        num -= 1

class Countdown:
    """
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    def __init__(self, n):
        self.start = n
        self.end = 0

    def __iter__(self):
        while self.start >= self.end:
            yield self.start
            self.start -= 1


def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    num = n
    while num > 0:
        if num == 1:
            yield num
            num -= 1
        elif num % 2 == 0:
            yield num
            num = num // 2
        elif num % 2 == 1:
            yield num
            num = 3*num + 1
