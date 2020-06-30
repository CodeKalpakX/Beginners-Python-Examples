#!/usr/bin/python
# -*- coding: utf-8 -*-


# Finds the minium number
# in un-sorted data

# Sudo Algo:
# Iterate through data
# each time a number(say k) is less than previous 
# consideration(say p), replace previous 
# consideration(p) with that smaller number(k)
# By this way, 
# 	At last we get the smallest(minium) number from data

def min_(seq):
	min_n = seq[0]
	for item in seq[1:]:
		if item < min_n:
			min_n = item 
	return min_n


# Test
# Add your tests too!
tests = [[9017289, 782367, 736812903, 9367821, 71256716278, 676215, 2398, 0, 1], 
		 [19208, 9239, 4376, 738, 78, 51, 5, 6, 12, 78, 123, 65765, 1999999999],
		 [1, 2, 4, 7, 9]]

# checking our functions results
# with python's built-in min() function
for test_i in range(len(tests)):
	m = min_(tests[test_i])
	if m == min(tests[test_i]):
		print("Min number in array({}) -> ".format(test_i + 1) + str(m))
	else:
		print("Oops! Someting went wrong!") 
