#!/usr/bin/python
# -*- coding: utf-8 -*-

# Median
# Median is the middle value of data
# Data of odd length has a mid value
# but, data of even length has 2 mid values
# so their median is mean of these 2 values

# ranked parameter is to tell function 
# weather data is ranked(sorted) or not
# 
def median(ar, ranked = False):
	if not ranked:
		data = sorted(ar[:])
	else:
		# Don't need an else block still
		# but to map program properly
		# i've added it 
		data = ar[:]

	# Data with odd length
	if len(data) % 2 != 0:

		# f(x) = (l(x) + 1) / 2 th term is the median of data
		# but since computer starts counting from 0
		# and not from 1, there is no need to add 1 
		# to length of data, otherwise results are
		# not accurate
		return data[len(data) / 2]

	# Data with even length
	# f(x) = [l(x) / 2 th term + (l(x) + 2) / 2th term] / 2
	# 2.0 is to declare that median can be a float
	# in case of even length data
	return (data[len(data) / 2 - 1] + data[(len(data) + 1) / 2]) / 2.0

# Test
odd = [123, 456, 789, 101112, 131415, 161718, 192021, 222324, 252627]
even = [8, 7, 5, 2, 1, 3, 4, 6]

if median(odd, ranked = True) == 131415 and median(even) == 4.5:
	
	# Print statements on separate lines look better
	print("Median of odd data: " + str(131415))
	print("Median of even data: " + str(4.5))
	print("Yeah, it works!")

else:
	# If algo didn't work
	print("There's something wrong!")

# This median is for un-distributed/un-grouped data
# i.e. no frequencies
# plain numbers in an array
