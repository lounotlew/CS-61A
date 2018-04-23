"""Midterm 2: Previous Midterms"""

"""Fall 2011"""

"""1) Mutation and Nonlocal Assignment"""

def make_deposit():
	fraud = False
	contents = []
	def deposit(bucks):
		nonlocal fraud
		# isn't nonlocal contents because list is a mutable value.
		for bucks in bucks:
			if bucks in contents:
				fraud = True
			contents.append(buck)
		if fraud:
			return 'Fraud'
		return len(contents)
	return deposit


"""3) Object-Oriented Programming"""

class M:
	# p = 2
	q = True
	def r(self):
		if self.q:
			return self.p
		# return self.r() - 1

"""4) Defining Functions Without Iteration"""

def overlap(word1, word2):
	if word1 == word2:
		return word1
	return overlap(word1[1:], word2[:len(word2)-1])

class N(M):
	p = 1
	# q = False
	# def r(self):
	# 	return self.p + 1

"""Fall 2012"""

"""1) Expressionism b)"""

class Lawyer:
	def __init__(self, s):
		if len(s) < 2:
			self.s = s
		else:
			self.s = Lawyer(s[2:])

	def __repr__(self):
		return 'Lawyer(' + repr(self.s) + ')'

	def think(self):
		if hasattr(self, 'decide'):
			return self.decide()
		while type(self.s) == Lawyer:
			self.s = self.s.s
		return self.s

class CEO(Lawyer):
	def decide(self):
		return 'Denied'

obama = Lawyer(['a', 'b', 'c'])
romney = CEO(['x', 'y', 'z'])

"""4) Form and Function b)"""

def list_anagrams1(w):
	if w == '':
		return ['']
	anagrams = []
	for i in range(len(w)):
		subgrams = list_anagrams1(w[:i] + w[i+1:])
		anagrams += [w[i] + s for s in subgrams]
	return anagrams

def list_anagrams2(w):
	if w == '':
		return ['']
	anagrams = []
	for i in range(len(w)):
		subgrams = list_anagrams(w[1:])
		anagrams += [s[:i] + w[0] + s[i:] for s in subgrams]
	return anagrams

"""Fall 2013"""

"""1) Classy Costumes"""

class Monster:
	vampire = {2: 'scary'}
	def werewolf(self):
		return self.vampire[2]

class Blob(Monster):
	vampire = {2: 'night'}
	def __init__(self, ghoul):
		vampire = {2, 'frankenstein'}
		self.witch = ghoul.vampire
		self.witch[3] = self

spooky = Blob(Monster)
spooky.werewolf = lambda self: Monster.vampire[2]

"""Spring 2013"""

"""1) You Will Be Baked. And Then There Will Be Cake. a)"""

the_cake = [1, 2, [3], 4, 5]
a_lie = the_cake[1:4]
the_cake = the_cake[1:4]
great = a_lie
delicious = the_cake
moist = great[:-1]

"""Fall 2014"""

"""1) Class Hierarchy"""

class Worker:
	greeting = 'Sir'
	def __init__(self):
		self.elf = Worker
	def work(self):
		return self.greeting + ' , I work'
	def __repr__(self):
		return Bourgeoisie.greeting
class Bourgeoisie(Worker):
	greeting = 'Peon'
	def work(self):
		print(Worker.work(self))
		return 'My job is to gather wealth'
class Proletariat(Worker):
	greeting = 'Comrade'
	def work(self, other):
		other.greeting = self.greeting + ' ' + other.greeting
		other.work()
		return other

jack = Worker()
john = Bourgeoisie()
jack.greeting = 'Maam'

"""2) Space"""

def locals(only):
	def get(out):
		nonlocal only
		def only(one):
			return lambda get: out
		out = out + 1
		return [out + 1]
	out = get(-only)
	return only

only = 3
earth = locals(only)
earth(4)(5)
