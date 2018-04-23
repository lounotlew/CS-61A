"""Control"""

"""Operators"""

from operator import add, mul

2 + 3
add(2, 3)
2 + 3 * 4 + 5
add(add(2, mul(3, 4)) , 5)
(2 + 3) * (4 + 5)
mul(add(2, 3), add(4, 5))

"""Division"""

2014 / 10
2014 // 10
2014 % 10
from operator import truediv, floordiv, mod
floordiv(2014, 10)
truediv(2014, 10)
mod(2014, 10)

"""Multiple return values"""

def divide_exact(n, d):
	return n // d, n % d

quotient, remainder = divide_exact(2014, 10)

"""Doctrings, doctests, & default arguments"""

def divide_exact2(n, d):
	"""Return the quotient and remainder of dividing N by D.

	>>> quotient, remainder = divide_exact2(2014, 10)
	>>> quotient
	201
	>>> remainder
	4
	"""
	return floordiv(n, d), mod(n, d)

def increase(number, by=1):  #default arguments
	return number + by

def absolute_value(x):  # Conditional expressions
	"""Return the absolute value of x.

	>>> absolute_value(-3)
	3
	>>> absolute_value(0)
	0
	>>> absolute_value(3)
	3
	"""
	if x < 0:
		return -x
	elif x == 0:
		return 0
	else:
		return x

i, total = 0, 0  # Summation via while
while i < 3:
	i = i + 1
	total = total + i
total
