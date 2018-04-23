"""Midterm 2: Official Review"""

"""
Mutation:

You don't need nonlocal to mutate lists; nonlocal is
for immutable objects.
"""

"""1) What Would Python Print?"""

funk = [1, 2, 3, 4]
bee = funk[1:]
bop = [1, 2, 3, 4]

def all(that, jazz):
	all = that + jazz
	if len(jazz) >= len(that):
		that[1] = jazz
		# ***This mutates bee, since func all takes in 
		# the original copy of bee.***
	return all

"""
>>>[funk[3], funk[0]]
[4, 1]
>>>all(bee, bee)
[2, 3, 4, 2, 3, 4]
>>>bee[1][0]
2
>>>funk == bop
True
>>>funk is bop
False
>>>bee[1] is bee
True
"""

"""
Recursion:

Base Case: simplest/smallest possible input
Recursive Case: Express the solution in terms of a smaller problem.
"""

"""
2) Recursion

subtraction game: game with 2 players (0, 1). In the beginning, there
is a pile of n cookies. Players alternate turns; each turn, a player can
take anywhere from 1 to 3 cookies. Player who takes the last cookie wins.

Write can_win to see if you can force a win in the current game state.

- if # of cookies < 0, impossible to win.
- otherwise, current player can take 1-3 cookies.
"""
def can_win(number):
	"""Returns True if the current player can win starting from the given
	state. It is impossible to win a game from an invalid game state.

	>>>can_win(-1) # invalid game state
	False
	>>>can_win(3) # Take all three!
	True
	>>>can_win(4)
	False
	"""
	# Use Tree Recursion.
	if number <= 0:
		return False
	for action in (1, 2, 3):
		new_state = number - action
		if not can_win(new_state):
			# see if the opponent cannot win if you choose action
			return True
	return False

"""
Objects:

Classes are "blueprints" for instances.
Methods are also attributes.
"""

"""
Trees:

Can be implemented using OOP or Data Abstraction.
Trees have a root, and children - the root is a value, and
the children are a list of Tree objects.

Binary Tree:

Each tree only has at most 2 children (left and right).
"""

"""
3) Trees

a) Draw the tree represented by:

Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(6)])])

b) Write a function alt_apply that applies f to one level
of the elements of t, and then g at the next level, etc.

>>>my_tree = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(6)])])
>>>other_tree = alt_apply(my_tree, lambda x: x*2, lambda x: x*x)
>>>print_tree(other_tree)
2
	4
	9
		8
		12
"""
def alt_apply(t, f, g):
	new value = f(t.root)
	new_branches = []
	for branch in t.branches:
		new_branches.append(alt_apply(branch, g, f))
	return Tree(new_value, new_branches)

# Level != each values; Level = each "rows'"
