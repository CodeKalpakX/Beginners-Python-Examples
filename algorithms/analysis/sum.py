#!/usr/bin/python
# -*- coding: utf-8 -*-

# Sudo ALgorithm:
# both functions work on same principle
# Iterate through array/arguments
# add each element to variable(res)
# return sum

def sum_(*args):
	res = 0.0
	for arg in args:
		res += arg
	return res

def sum_ar(ar, end_i):
	# end_i is the last index of array
	# till which function should add
	# array's elements
	if end_i > 0 and end_i <= len(ar):
		if end_i == len(ar):
			end_i = end_i - 1
	else:
		end_i = len(ar) - 1

	res = 0.0
	for elem in ar[:end_i + 1]:
		res += elem 

	return res 

# Simple Algorithm

# Testing
# First Function
if sum_(1, 2, 3, 4, 5, 6, 7, 8, 9) == 45:
	print("First Function Works!")

# Second Function
if sum_ar([1, 2, 3, 4, 5, 6, 7, 8, 9], -1) == 45:
	print("Second Function Partially Works!")

if sum_ar([1, 2, 3, 4, 5, 6, 7, 8, 9], 6) == 28:
	print("Second Function Completely Works!")
