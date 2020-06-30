#!/usr/bin/python
# -*- coding: utf-8 -*-

# returns UNICODE value of a character
def get_ascii(S):
	# even if string has only 1 character 
	# it yields same for all
	if len(S) > 0:
		for char_ in list(S):
			yield((char_, ord(char_)))
	
	# ord returns unicode value of given string of length 1
	# we only increased it's capacity
	# simple ..eh

# test
test_characters = ['A', 'x', 'Y', 'Z', 'm', 'K', "STack"]
for test_case in test_characters:
	print("Test Case: " + test_case)

	codes = list(get_ascii(test_case))
	for code in codes:
		print("  character: {}, unicode_val: {}".format(code[0], code[1]))
	print(" ")
