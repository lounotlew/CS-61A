"""Midterm 2: HKN Review"""

"""1) Box & Pinter Diagrams"""

r = ([1, 2, 1, 2],)
s = list(r)
t = r
r[0][2] = t[0]
s[0] = r[0][1:]
s[0][1][2][3] = 4

"""2) Data Abstraction"""

def make_point(x, y):
	# Constructor: Builds an object of the abstract data type.
	return (x, y)

def x(point):
	# Selector: Extracts relevant information from the object.
	return point[0]

def y(point):
	return point[1]

def dist(point1, point2):
	return sqrt((x(point2) - x(point1)) ** 2 + (y(point2) - y(point1)) **2)

"""3) Environment Diagrams"""

def k(b):
	def seven(up):
		b.extend(['<3', '<3'])
		# Don't need nonlocal to mutate something.
		nonlocal b
		# Need nonlocal to change what value a variable points to.
		b = 5
		up[0][0] = 'cs61a'
		return up[0:2]
		# Slicing creates a new list with the same values.
	return seven((b, 3, 6))

k(['cookies'])

"""6) Trees"""

"""
a) Write a function john_finder that takes in a tree and returns
whether it contains the string "DeNero":

>>> john_finder(Tree("DeNero", (Tree("Hilfinger")))
True
>>> john_finder(Tree("#420blazeit"))
False
"""
def john_finder(t):
	if t.entry == "DeNero":
		return True
	for b in t.branches:
		if john_finder(b):
			return True
	return False

"""
b) Write a function tree_equals that takes in two BinaryTrees
that contain integers and returns True if the binary trees have
the same 'shape' and the corresponding nodes have the same values.
"""
def tree_equals(t1, t2):
	if t1 is BinaryTree.empty_tree and t2 is BinaryTree.empty_tree:
		return True
	if t1 is BinaryTree.empty_tree or t2 is BinaryTree.empty_tree:
		return False
	return t1.entry == t2.entry and tree_equals(t1.left, t2.left) and tree_equals(t1.right, t2.right)

"""
c) Write the function prod_tree, which takes a Tree of numbers and
returns the product of all the numbers in the Tree.

>>> t = Tree(1, Tree(2), Tree(3, Tree(4, Tree(5), Tree(6))))
>>> prod_tree(t)
720
"""
def prod_tree(t):
	result = t.entry
	for branch in t.branches:
		result *= prod_tree(branch)
	return result
