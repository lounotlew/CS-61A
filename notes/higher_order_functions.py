"""Higher-Order Functions"""

def fib(n):
	"""Compute the nth Fibonacci number, for N >= 2.

	>>> fib(8)
	21
	"""
	pred, curr = 0, 1  #0th and 1st Fibonacci numbers
	k = 1  #Tracks which Fib number is curr
	while k < n:
		pred, curr = curr, pred + curr
		k = k + 1
	return curr

def pyramid(n):
	"""Sum increasing and decreasing sequences.

	>>> pyramid(10)
	100
	"""
	a, b, total = 0, n, 0
	while b:
		a, b = a + 1, b - 1
		total = total + a + b
	return total

"""Generalizing patterns using arguments"""

from math import pi, sqrt

def area_square(r):
	"""Return the area of a square with side length R."""
	return r * r

def area_circle(r):
	"""Return the area of a circle with radius R."""
	return r * r * pi

def area(r, shape_constant):
	"""Return the area of a shape from length measurement R."""
	assert r > 0, 'A length must be positive'
	return r * r * shape_constant

def area_square2(r):
	return area(r, 1)

def area_circle2(r):
	return area(r, pi)

def area_hexagon2(r):
	return area(r, 3 * sqrt(3) / 2)

"""Functions as arguments"""

def sum_naturals(n):
	"""Sum the first N natural numbers.

	>>> sum_naturals(5)
	15
	"""
	total, k = 0, 1
	while k <= n:
		total, k = total + k, k + 1
	return total

def sum_cubes(n):
	"""Sum the first N cubes of natural numbers.

	>>> sum_cubes(5)
	225
	"""
	total, k = 0, 1
	while k <= n:
		total, k = total + pow(k, 3), k + 1
	return total

def identity(k):
	return k

def cube(k):
	return pow(k, 3)

def summation(n, term):
	"""Sum the first N terms of a sequence.

	>>> summation(5, cube)
	225
	"""
	total, k = 0, 1
	while k <= n:
		total, k = total + term(k), k + 1
	return total

from operator import mul

def pi_term(k):
	return 8 / mul(k * 4 - 3, k * 4 - 1)

summation(10000, pi_term)

"""Local function definitions; returning functions"""

def make_adder(n):
	"""Return a function that takes one argument K and returns K + N.

	>>> add_three = make_adder(3)
	>>> add_three(4)
	7
	"""
	def adder(k):
		return k + n
	return adder

make_adder(2000)(13)
