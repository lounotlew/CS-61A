"""Midterm 1: Official Review"""

"""1) What Would Python Print?"""

f = lambda x: print(x)
def g(x):
	if x == 5:
		def h(y):
			return lambda: f(y)
		return h
	print(x, print(x))
	return lambda: f(x)

y = g(5)

"""
>>> y(8)()
8
>>> z = g(6)
6
6 None
>>> z(f(7))
7
Error (Arg when expected no arg)
"""

"""2) Environment Diagrams"""

x = 4
def chain(x):
	def event(blarp):
		if x > 5:
			return blarp
		else:
			return lambda q: q + 100
	return event

def arp(blarp):
	return blarp(blarp)

"""
>>> arp(chain(6))(3)
3
"""

"""3) Fill In the Blanks"""

from operator import add, mul
def f(x):
	def g(y):
		def h(f):
			return f(add(1, x), y)
		return h
	return g

"""
>>> f(k) = 15
k = ?
# k = (2)(5)(mul)
>>> f(2)(5)(mul)
15
"""

def fox_says(start, middle, end, num):
	"""
	>>> fox_says('wa', 'pa', 'pow', 3)
	'wa-pa-pa-pa-pow'
	"""
	def repeat(k):
		if k == 1:
			return middle
		else:
			return middle + '-' + repeat(k-1)
	return start + '-' + repeat(num) + '-' + end
