#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

# Length of array(number of elements in array)
# is simple algorithm
#  Iterates through array
#  at each iteration (count) variable
#  is incremented
# 
# This solution is ideal for small array
# But not that good for bigger array's

# There are many ways to do same thing
# but always go with solution that is
# simple, and has least instructions
# for computer to execute, making
# process faster

# is_ap parameter indicates weather array
# is an arithmetic progression or not
#
# Similarly, 
# is_gp indicates weather array is an geometric progression or not
# If array is either ap or gp then it's length can be
# found by derivation of it's general term formula
# e.g. ap's general term,
# tn = a + (n - 1)d
# thus, n = (tn - a) / d + 1 

def length(ar, is_ap = False, is_gp = False, big_data = False, data_outline = []):
	# Length of data if it is an arithmetic progression
	# using derived formula, n = (tn - a) / d + 1
	if is_ap:
		return ((ar[-1] - ar[0]) / (ar[1] - ar[0])) + 1

	# Length of data if it is an geometric progression
	# using derived formula, n = ((log base 10 an / a1) / log 10 r) + 1
	elif is_gp:
		# length is never a float
		return int(math.log10((ar[-1] / ar[0])) / math.log10((ar[1] / ar[0])) + 1)

	# Length of big data using data outline
	# data outline is selective elements to be counted from entire
	# data
	elif big_data:
		count = 0
		for element in data_outline:
			count += ar.count(element)
		return count 
	
	# Sequential counting
	# of elements in array
	else:
		res = 0
		for item in ar:
			res += 1
		return res 
		

# Test
# Geometric progression Test
if length([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096], None, is_gp = True) == 13:
	print("\nLength of geometric progression: " + str(13))
	print("--> geometric progression counting works!\n")
else:
	print("Something's wrong with gp feature")

# Arithmetic progression test
if length([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43], is_ap = True) == 15:
	print("Length of arithmetic progression: " + str(15))
	print("--> arithmetic progression counting works!\n")
else:
	print("Something's wrong with ap feature")

# Big data test
# Passing only useful numbers in outline array
if length([1, 1, 4, 5, 7, 1, 9, 5, 2, 4, 3, 5, 9], None, None, True, [1, 4, 5, 7, 9]) == 11:
	print("Length of arithmetic progression: " + str(11))
	print("--> big data counting works!\n")
else:
	print("Something's wrong with ap feature")

# Small data
print("Length: " + str(length([1, 1, 2, 3, 5, 8, 13, 21, 34, 55])))
print("Everything Works!\n")
