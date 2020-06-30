#!/usr/bin/python
# -*- coding: utf-8 -*-

# Bubble Sort
# Ideal sorting algorithm for 
# small data/array

# temporary parameter tells
# function to sort a copy of 
# orignal array, and not the array itself

# reverse parameter tells func
# to sort array in reverse/decending
# order

def sort_(arr, temporary = False, reverse = False):
	
	# Making copy of array if temporary is true
	if temporary:
		ar = arr[:]
	else:
		ar = arr
	
	# To blend every element
	# in correct position
	# length of total array is required
	length = len(ar)
	
	# After each iteration right-most
	# element is completed sorted
	while length > 0:

		# So every next time we iterate only
		# through un-sorted elements
		for i in range(0, length - 1):

			if reverse:

				# Swapping greater elements to left
				# and smaller to right
				# decending order
				if ar[i] < ar[i+1]:
					tmp = ar[i]
					ar[i] = ar[i + 1]
					ar[i + 1] = tmp
			else:

				# Swapping greater elements to right
				# and smaller to left
				# accending order
				if ar[i] > ar[i+1]:
					tmp = ar[i]
					ar[i] = ar[i + 1]
					ar[i + 1] = tmp


		# making sure loop breaks
		length = length - 1 
	
	# if temporary, then returning
	# copied arr's sorted form
	# cuz if not returned, then function
	# is literally of no use
	if temporary:
		return ar 	

# See proper explaination 
# at: https://www.geeksforgeeks.org/bubble-sort/
# a good site!


# Testing
tests = [[7, 8, 9, 6, 4, 5, 3, 2, 1, 15], [1, 90, 1110, 1312, 1110, 98, 76, 54, 32, 10], ] # Add your test cases 

for test in tests:
	accend, decend = sort_(test, True), sort_(test, True, True)
	if accend == sorted(test) and decend == sorted(test, reverse = True):
		print("Orignal: {}".format(test))
		print("Sorted: {}".format(accend))
		print("Sorted(reverse): {}\n".format(decend))
	else:
		print("Something went wrong!\n")


# Seems our bubble sort works
# however for small data/array!
