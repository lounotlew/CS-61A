"""Objects"""

"""Class: a template for its instances (case-sensitive)."""

class Clown:
	nose = 'big and red'
	def dance():
		return 'No thanks'

"""
Methods: functions defined in the suite of a class statement.

***self should always be bound to an instance of the Account class.
***self should always be listed as the first argument for each method.
"""

class Account:
	"""An account has a balance and a holder.
	All accounts share a common interest rate.

	>>> a = Account('John')
	>>> a.holder
	'John'
	>>> a.deposit(100)
	100
	>>> a.withdraw(90)
	10
	>>> a.withdraw(90)
	'Insufficient funds'
	>>> a.balance
	10
	>>> a.interest
	0.02
	>>> Account.interest = 0.04
	>>> a.interest
	0.04
	"""

	interest = 0.02  #A Class attribute

	def __init__(self, account_holder):
		self.balance = 0
		self.holder = account_holder

	def deposit(self, amount):
		"""Add amount to balance."""
		self.balance = self.balance + amount
		return self.balance

	def withdraw(self, amount):
		"""Subtract amount from balance if funds are available."""
		if amount > self.balance:
			return 'Insufficient funds'
		self.balance = self.balance - amount
		return self.balance

"""
Invoking methods:
tom_account is bound to self.
"""

tom_account = Account('Tom')

"""
getattr looks up an attribute using a string.

>>>getattr(tom_account, 'balance')
10
>>>hasattr(tom_account, 'deposit')
True

Python differentiates between functions and bound methods.

Class attributes are "shared" across all instances of a class;
they are attributes f the class, not the instance.

Attributes assignment adds/modifies the attribute of tom_account:

tom_account.interest = 0.08
>>>jim_account.interest
0.04
>>>tom_account.interest
0.08
"""
