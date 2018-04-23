"""CS 61A Final"""

"""Fall 2012"""

"""1) Bank Rewrite"""

jan = [1, 3, 5]
feb = [3, 5, 7]

def mar(apr, may):
	if not apr or not may:
		return []
	if apr[0] == may[0]:
		return mar(apr[1:], may[1:]) + [apr[0]]
	elif apr[0] < may[0]:
		return mar(apr[1:], may)
	else:
		return mar(apr, may[1:])