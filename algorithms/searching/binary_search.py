#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys

# I'm too lazy to explain how it works, 
# instead check below sites out:
# https://en.wikipedia.org/wiki/Binary_search_algorithm
# https://www.geeksforgeeks.org/binary-search/

# Make sure you know concept of Recursion

# Function explaination:
# ar is the array
# f is starting index for divided search array
# l is ending index for divided search array
# v is the query to search in array data space
# sorted_ar tells the func, if array is sorted or not
# as binary search won't work on an un-sorted array

def binary_search(arr, f, l, v, sorted_ar = False):
	# need an ordered/sorted array for search, 
	# else search won't produce desirable results
	if not sorted_ar:
		arr.sort()
	
	# If input is invalid
	if l - f < 0:
		return -1

	else:
		# Index of mid-term of array[f:l+1]
		mid_element_i = (f + l) // 2

		# If mid-term matches the query
		if arr[mid_element_i] == v:
			return mid_element_i
		
		# If query is bigger than that mid-term
		# then we'll look at next_half of array
		elif v > arr[mid_element_i]:
			return binary_search(arr, mid_element_i+1, l, v, True)
		
		# else query is smaller than mid-term 
		# so we'll look at lesser half of array
		else:
			return binary_search(arr, f, mid_element_i-1, v, True)

# Tests
# Add your tests
# Arrays below are not sorted or are un-ordered
# Index returned by function is for sorted array
# thus index might differ for same element, array below and in sorted array!
tests = [
	[10, 29, 38, 47, 56, 19, 28, 37, 46, 50],
	[1, 92, 83, 74, 65, 29, 84, 75],
	[1, 21, 32, 43, 54, 65, 79],
	[7, 7],
]

# Play as long as you can
# Searches query in all of arrays in tests
i = 0
while True:
	if raw_input("\n[%i] Exit(press e) or Continue(press c): " % i) == "e":
		sys.exit()
	q = int(raw_input("\nSearch?: "))
	print("Results:")
	for test in tests:
		find_i = binary_search(test, 0, len(test) - 1, q, False)	
		if test[find_i] == q:
			print("  Found [{}] at index({}) in array({})".format(q, find_i, tests.index(test) + 1))
		else:
			# else is executed means, 
			# something is wrong with the algorithm
			print("  No results for [{}] in array({}). Try another search!".format(q, tests.index(test) + 1))
	i += 1
