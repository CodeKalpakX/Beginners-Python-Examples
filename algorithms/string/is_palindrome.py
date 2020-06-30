#!/usr/bin/python
# -*- coding: utf-8 -*-

# Palindrome is a special string, is same if reversed
# e.g. noon, racecar, et cetera
# Notice in above strings, there is no difference between 
# string and it's reversed form

# Function checks if given string is a palindrome or not
# string[::-1] is a clever way to reverse string
# string from start index to end index 
# whose difference is -1(reverse)
# found on stack overflow, very pythonic

def is_palindrome(s) :
	if s[::-1] == s:
		return True
	return False

# Test
S = raw_input("String: ")
if is_palindrome(S):
	print("Results:\n   " +S + " is a palindrome string.")
else:
	print("Results:\n   " + S + " is not a palindrome string.")

# add a loop to play many times(maybe infinite)
