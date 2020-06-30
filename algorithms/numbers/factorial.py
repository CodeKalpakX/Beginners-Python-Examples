#!/usr/bin/python
# -*- coding: utf-8 -*-

# Factorial
# is a mathematical function which 
# determines number of all possibilities
# you can arrange 'n' number of objects!
#
# If there are 5 options in total
# At first: there are 5 to choose from
# 5 X
# then, after choosing 1 from those 5 we'd have
# 4 remaining, 5 x 4 x
# then 3 remaining, 5 x 4 x 3
# then 2, 5 x 4 x 3 x 2
# then 1, 5 x 4 x 3 x 2 x 1 = 120

# n is total number of objects
def factorial(n):
	if n <= 1:
		return 1
	else:
		n = n * factorial(n - 1)
		return n

# Recursion is the easiest way to 
# solve this problem
# but, to make sure recursion's depth ends, above
# condition is necessary, otherwise
# errors occur

# Another way to solve problem
def factorial_(n):
	if n <= 1:
		return 1
	else:
		m = 1
		# range function produces inclusive range
		for integer in range(1, n + 1):
			m *= integer
		return m 

# This solution is bigger 
# and looks much more complex 
# than the recursion one
# Both work the same however

# Test
if factorial(5) == factorial_(5) == 120:
	print("(" + str(5) + ")! == " + str(120))
	print("Both functions work!\n-Try it yourself-")
	x = int(raw_input("\nNumber: "))
	print("(" + str(x) + ")! == " + str(factorial(x)))
else:
	print("Someting went wrong!")
