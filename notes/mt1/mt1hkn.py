"""Midterm 1: HKN Review"""

"""1) What would Python Print?"""

def best(n):
	def pikachu():
		print('Pika!')
		return n
	bulbasaur = lambda: 2
	charmander = lambda p: pikachu
	if pikachu() < bulbasaur():
		print('Mew')
	elif pikachu() == charmander(1):
		print('Pikachu!')
	if pikachu() % 2 == 1:
		return 'Squirtle'

# Function still evaluated in order to compare in an if/else statement.
# Charmander doesn't return "n" because it doesn't actually call the function; only returns it.

def print_moar(stuff):
	i = 0
	while stuff and i < 100:
		if not stuff:
			print('Best Champion')
		stuff = print(stuff, print('worst champion'))
		i = i + 1
	return stuff

# A string always returns true.

"""2) Booleans"""

def nth_fib_prime(n):

	def is_prime(n):
		k = 2
		if n == 1 or n == 0:
			return False
		while k < n:
			if n % k == 0:
				return False
			k = k + 1
		return True 

	count = 0
	curr, next = 2, 3
	while count < n:
		if is_prime(curr):
			print(curr)
			count += 1
		curr, next = next, curr + next

"""3) Higher Order Functions"""

def communative1(f):
	"""
	>>> communative(add)(1, 2)
	True #1 + 2 == 2 + 1
	>>> communative(lambda x, y: x*x+y)(2, 5)
	False # 2*2*5 != 5*5*2
	"""
	return lambda x, y: f(x, y) == f(y, x)

def communative2(f):
	def swappable(x, y):
		return f(x, y) == f(y, x)
	return swappable
	