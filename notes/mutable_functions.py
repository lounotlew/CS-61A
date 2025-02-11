"""Mutable Functions"""

def make_withdraw(balance):
	"""Return a withdraw function with a starting balance."""

	def withdraw(amount):
		nonlocal balance
		if amount > balance:
			return 'Insufficient funds'
		balance = balance - amount
		return balance

	return withdraw

def make_withdraw_list(balance):
	b = [balance]

	def withdraw(amount):
		if amount > b[0]:
			return 'Insufficient funds'
		b[0] = b[0] - amount
		return b[0]
		
	return withdraw

"""
Nonlocal statements: nonlocal <name>

Future assignments to that name change its pre-existing binding in th
first non-local frame of the current environment in which that name
is bound.
"""

def f(x):
	x = 4
	def g(y):
		def h(z):
			nonlocal x
			x = x + 1
			return x + y + z
		return h
	return g

a = f(1)
b = a(2)
total = b(3) + b(4)  # total = 22
