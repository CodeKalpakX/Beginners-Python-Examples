#!/usr/bin/python
# -*- coding: utf-8 -*-


# Mode
# mode or modal value, is the number in data
# that has highest frequency, or occurs in data/array
# maximum number of times

# This function produces an outline of data
# each element occurs only once in outline
# that means no repeats of same numbers
def reduce_data(data):
	# Simplest way to do this, just 1 line of code:
	# return list(set(data))
	# since set data structure does not have repeats

	# But below code is much more
	# illustrative and easier to understand

	data_outline = []
	for item in data:
		if item not in data_outline:
			data_outline.append(item)

	return data_outline

# To find mode, we apply same principle, that works
# behind finding the maximum or minimum number(see max.py, min.py)
def mode(data):
	mode_ = data[0]
	max_frequency = data.count(data[0])

	# Insted of iterating through every repeat of 
	# same number, then counting multiple repeats
	# of number multiple times, iterating through outline
	# of data is convinient, less time consuming.
	for value in reduce_data(data[1:]):
		if data.count(value) > max_frequency:
			mode_ = value 
			max_frequency = data.count(value)

	# instead of just mode, it's freq 
	# can also be helpful
	return (mode_, max_frequency)

# Test
# Add your test cases
tests = [
	[19, 17, 25, 34, 57, 17, 25, 52, 47, 42, 25, 17, 3, 0, 3, 41, 17],
	[1917, 2534, 5717, 1725, 5247, 1917, 4117, 5717, 17303, 1917],
]

# Function does work, 
# Check yourself
for test in tests:
	modal_v = mode(test)
	print("\nData outline: {}".format(reduce_data(test)))
	print("Mode: {}\nFrequency: {}".format(modal_v[0], modal_v[1]))

print("")

# Mode for un-grouped data
