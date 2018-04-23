"""Trees"""

"""Slicing: creates a new list."""

lst = [1, 2, 3, 4, 5]
sliced = lst[1:3]
# includes index 1, excludes index 3.

"""
>>> sliced
[2, 3]
"""

"""Tree Functions"""

def tree(root, branches=[]):
	for branch in branches:
		assert is_tree(branch), 'branches must be trees.'
	return [root] + list(branches)

def root(tree):
	return tree[0]

def branches(tree):
	return tree[1:]

def is_tree(tree):
	if type(tree) != list or len(tree) < 1:
		return False
	for branch in branches(tree):
		if not is_tree(branch):
			return False
	return True

def is_leaf(tree):
	return not branches(tree)

def fib_tree(n):
	if n == 0 or n == 1:
		return tree(n)
	else:
		left, right = fib_tree(n-2), fib_tree(n-1)
		r = root(left) + root(right)
		return tree(r, [left, right])

def count_leaves(n):
	if is_leaf(n):
		return 1
	else:
		counts = [count_leaves(b) for b in branches(tree)]
		return sum(counts)

def leaves(tree):
	"""Return a list containing the leaves of tree.

	>>>leaves(fib_tree(5))
	[1, 0, 1, 0, 1, 1, 0, 1]
	"""
	if is_leaf(tree):
		return [root(tree)]
	else:
		return sum([leaves(b) for b in branches(tree)], [])

def partition_tree(n, m):
	if n == 0:
		return tree(True)
	elif n < 0:
		return tree(False)
	elif m == 0:
		return tree(False)
	else:
		left = partition_tree(n-m, m)
		right = partition_tree(n, m-1)
		return tree(m, [left, right])

def print_parts(tree, partition=[]):
	if is_leaf(tree):
		if root(tree):
			print(partition)
	else:
		left, right = branches(tree)
		print_parts(left, partition+[root(tree)])
		print_parts(right, partition)

"""Tree Class"""

class Tree:
	def __init__(self, entry, branches=()):
		self.entry = entry
		for branch in branches:
			assert isinstance(branch, Tree)
		self.branches = branches

	def __repr__(self):
		if self.branches:
			return 'Tree({0}, {1})'.format(self.entry, repr(self.branches))
		else:
			return 'Tree({0})'.format(repr(self.entry))

	def is_leaf(self):
		return not self.branches

"""Binary Tree Class"""

class BinaryTree(Tree):
	empty = Tree(None)
	empty.is_empty = True

	def __init__(self, entry, left=empty, right=empty):
		for branch in (left, right):
			assert isinstance(branch, BinaryTree) or branch.is_empty
		Tree.__init__(self, entry, (left, right))
		self.is_empty = False

	@property
	def left(self):
		return self.branches[0]

	@property
	def right(self):
		return self.branches[1]
