"""Midterm 1: Previous Midterms"""

"""Fall 2014"""

"""1) World Cup"""

def square(x):
	return x * x

def argentina(n):
	print(n)
	if n > 0:
		return lambda k: k(n+1)
	else:
		return 1 / n

def germany(n):
	if n > 1:
		print('hallo')
	if argentina(n-2) >= 0:
		print('bye')
	return argentina(n+2)

"""3) Express Yourself a)"""

def kbonacci(n, k):
	if n < k - 1:
		return 0
	elif n == k - 1:
		return 1
	else:
		total = 0
		i = n-k
		while i < n:
			total = total + kbonacci(i, k)
			i = i + 1
		return total

"""3) Express Yourself b)"""

def combine(left, right):
	factor = 1
	while factor <= right:
		factor = factor * 10
	return left * factor + right

def reverse(n):
	if n < 10:
		return n
	else:
		return combine(n%10, reverse(n//10))

def remove(n, digit):
	removed = 0
	while n:
		n, last = n // 10, n % 10
		if last != digit:
			removed = removed * 10 + last
		return reverse(removed)

"""4) Lambda at Last a)"""

two_thousand = lambda two: lambda k: k(two)(two)
lamb = lambda x: lambda: 2*x
