#!/usr/bin/python
# -*- coding: utf-8 -*-

# Compares elements at same 
# index in 2 different arrays
# and so called generates tuple of 
# that value, index, array number
# however if both numbers are equal
# returns zero simply

# Prime condition for correct results
# length(arr1) == length(arr2)

def compare_array_elements(arr1, arr2):
	for l in range(len(arr1)):
		if arr1[l] > arr2[l]:
			yield (arr1[l], l, 1)
		elif arr1[l] < arr2[l]:
			yield (arr2[l], l, 2)
		else:
			yield(0)


# Tests
tests = [
	[
		[21, 3454, 12, 77, 21, 90, 235],
		[123, 54, 21, 7, 23, 987, 21312]
	],

	[
		[1223, 8273, 17732, 7127],
		[12989, 2131223, 129, 10]
	]
]

# Does not test last condition of function
for test in tests:
	for n, index, array_n in compare_array_elements(test[0], test[1]):
		print("  [ %i ] is biggest value at index(%i) from array(%i)" %(n, index, array_n))
