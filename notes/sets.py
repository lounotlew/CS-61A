"""Sets"""

"""Linked list processing"""

def empty(s):
	return s is Link.empty

def filter_link(f, s):
	"""Return a Link with elements of s for which f returns a true value."""
	if s is Link.empty:
		return s
	else:
		filtered = filter_link(f, s.rest)
		if f(s.first):
			return Link(s.first, filtered)
		else:
			return filtered

def extend_link(s, t):
	if empty(s):
		return t
	else:
		return Link(s.first, extend_link(s.rest, t))

"""Sets as unordered sequences"""

def set_contains(s, v):
	"""Return true if set s contains value v as an element.

	>>> s = Link(1, Link(2, Link(3))) 
	>>> set_contains(s, 2)
	True
	>>> set_contains(s, 5)
	False
	"""
	if empty(s):
		return False
	elif s.first == v:
		return True
	else:
		return set_contains(s.rest, v)

def adjoin_set(s, v):
	"""Return a set containing all elements of s and element v.

	>>> s = Link(1, Link(2, Link(3))) 
	>>> t = adjoin_set(s, 4)
	>>> t
	Link(4, Link(1, Link(2, Link(3))))
	"""
	if set_contains(s, v):
		return s
	else:
		return Link(v, s)

def intersect_set(set1, set2):
	"""Return a set containing all elements common to set1 and set2.

	>>> s = Link(1, Link(2, Link(3))) 
	>>> t = adjoin_set(s, 4)
	>>> intersect_set(t,  Link(1, Link(4, Link(9))))
	Link(4, Link(1))
	"""
	in_set2 = lambda v: set_contains(set2, v)
	return filter_link(in_set2, set1)

def union_set(set1, set2):
	"""Return a set containing all elements either in set1 or set2.

	>>> s = Link(1, Link(2, Link(3))) 
	>>> t = adjoin_set(s, 4)
	>>> union_set(t, s)
	Link(4, Link(1, Link(2, Link(3))))
	"""
	not_in_set2 = lambda v: not set_contains(set2, v)
	set1_not_set2 = filter_link(not_in_set2, set1)
	return extend_link(set1_not_set2, set2)

"""Sets as (sorted) ordered sequences"""

def set_contains2(s, v):
	"""Return true if set s contains value v as an element.

	>>> s = Link(1, Link(2, Link(3)))
	>>> set_contains2(s, 2)
	True
	>>> set_contains2(s, 5)
	False
	"""
	if empty(s) or s.first > v:
		return False
	elif s.first == v:
		return True
	else:
		return set_contains2(s.rest, v)

def intersect_set2(set1, set2):
	"""Return a set containing all elements common to set1 and set2.

	>>> s = Link(1, Link(2, Link(3))) 
	>>> t = Link(2, Link(3, Link(4)))
	>>> intersect_set2(s, t)
	Link(2, Link(3))
	"""
	if empty(set1) or empty(set2):
		return Link.empty
	else:
		e1, e2 = set1.first, set2.first
		if e1 == e2:
			return Link(e1, intersect_set2(set1.rest, set2.rest))
		elif e1 > e2:
			return intersect_set2(set1.rest, set2)
		elif e2 < e1:
			return intersect_set2(set1, set2.rest)

"""Sets as trees"""

import trees

def set_contains3(s, v):
	"""Return true if set s contains value v as an element.

	>>> t = Bin(2, Bin(1), Bin(3))
	>>> set_contains3(t, 3)
	True
	>>> set_contains3(t, 0)
	False
	>>> set_contains3(big_tree(20, 60), 34)
	True
	"""
	if s.is_empty:
		return False
	elif s.entry == v:
		return True
	elif s.entry < v:
		returns set_contains3(s.right, v)
	elif s.entry > v:
		return set_contains3(s.left, v)

def adjoin_set3(s, v):
	"""Return a set containing all elements of s and element v.

	>>> b = big_tree(0, 9)
	>>> b
	Bin(4, Bin(1), Bin(7, Bin.empty, Bin(9)))
	>>> adjoin_set3(b, 5)
	Bin(4, Bin(1), Bin(7, Bin(5), Bin(9)))
	"""
	if s.is_empty:
		return Bin(v)
	elif s.entry == v:
		return s
	elif s.entry < v:
		return Bin(s.entry, s.left, adjoin_set3(s.right, v))
	elif s.entry > v:
		return Bin(s.entry, adjoin_set3(s.left, v), s.right)

def big_tree(left, right):
	"""Return a tree of elements between left and right.

	>>> big_tree(0, 12)
	Bin(6, Bin(2, Bin(0), Bin(4)), Bin(10, Bin(8), Bin(12)))
	"""
	if left > right:
		return Bin.empty
	split = left + (right - left) // 2
	return Bin(split, big_tree(left, split - 2), big_tree(split + 2, right))
