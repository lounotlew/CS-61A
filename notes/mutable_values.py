"""Mutable Values"""

"""
Lists:

Mutable values that can change in the course
of a program.
Only lists and dictionaries can change.
"""

"""
Operations:

- lst.pop(): removes the last element of a list and returns it.
**add argument n to lst.pop() to remove nth index.**
- lst.append(x): adds x to the end of a list.
- lst.extend([a, b, c...]): adds [a, b, c...] to the
end of a list.
"""

suits = ['coin', 'string', 'myriad']
original_suits = suits
suits.pop()  # removes and returns the final element.
suits.remove('string')  # removes the first element that equals the argument.
suits.append('cup')  # add an element to the end.
suits.extend(['sword', 'club'])  # add all elements of a list to the end.
suits[2] = 'spade'  # replace an element.
suits[0:2]  # replace a slice.
[suit.upper() for suit in suits]  # list comprehension.
[suit[1:4] for suit in suits if len(suit) == 5]  # list comprehension with a condition.

"""Dictionaries"""

numerals = {'I': 1, 'V': 5, 'X': 10}
original_numerals = numerals

numerals['X'] = 11  # the value for key 'X' changes from 10 to 11.
numerals['L'] = 50  # adds key 'L' and corresponding value 50 to numerals.
numerals.pop('X')  #removes the key 'X' and corresponding value 11 from numerals; returns 11.

"""
Dictionary Restrictions:

Dictionaries are unordered collection of key-value pairs.
A key cannot be a list or a dictionary (or any mutable type).
Two keys cannot be equal.
"""

def mystery(s):
	s.pop()
	s.pop()

def mystery2(s):
	s[2:] = []

# mystery and mystery2 do the same thing for four = [1, 2, 3, 4].

"""
Tuples:

Protects immutable values from mutation.
Stored in parenthesis, not brackets.
Tuples can be used as keys for dictionaries.
"""

a = {tuple([1, 2]): 3}
b = tuple(x+1 for x in range(5))  #Tuple comprehension.

###Try not to use mutable values as arguments.###
