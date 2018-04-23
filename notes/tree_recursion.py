"""Tree Recursion"""

"""Order of recursive calls"""

def cascade(n):
	"""Print a cascade of prefixes of n.

	>>> cascade(1234)
	1234
	123
	12
	1
	12
	123
	1234
	"""
	if n < 10:
		print(n)
	else:
		print(n)
		cascade(n//10)
		print(n)  # Placed on "hold" until the recursive call 

def cascade2(n):
	"""Print a cascade of prefixes of n."""
	print(n)
	if n >= 10:  # Base case implied in "if n >= 10" statement.
		cascade(n//10)
		print(n)

def inverse_cascade(n):
	"""Print an inverse cascade of prefixes of n.

	>>> inverse_cascade(1234)
	1
	12
	123
	1234
	123
	12
	1
	"""
	grow(n)
	print(n)
	shrink(n)

def f_then_g(f, g, n):  # The order in which something needs to be completed.
	if n:
		f(n)
		g(n)

grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)
# inverse_cascade(n) isn't a recursive function; grow, shrink is.

"""Tree Recursion"""

def fib(n):
	"""Compute the nth Fibonacci number.

	>>> fin(8)
	21
	"""
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-2) + fib(n-1)

def count_partitions(n, m):
	"""Count the partitions of n using parts up to size m.

	>>> count_partitions(6, 4)
	9
	>>> count_partitions(10, 10)
	42
	"""
	if n == 0:
		return 1
	elif n < 0:
		return 0
	elif m == 0:
		return 0
	# The base cases involve situations where the function cannot continue, i.e. when n < 0.
	else:
		with_m = count_partitions(n-m, m)
		without_m = count_partitions(n, m-1)
		return with_m + without_m
