#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

# The function
# counts number of occurrences of vowels
# in given string

# Principle:
# Loop through list of vowels
# count occurrences of each vowel in given string
# yield/generate the occurrences of that vowel

def vowel_count(S):
	vowels = ['a', 'e', 'i', 'o', 'u']
	for vowel in vowels:
		counter = 0
		for char in S:
			if char == vowel:
				counter += 1
		yield(vowel, counter)

# CLI
# Testing or Playing Interface
while True:
	usr_input = raw_input("\nPress (e) to Exit\nor Enter string: ").strip().lower()
	if not usr_input == "e":
		print("> Results: ")
		for vow, counter in vowel_count(usr_input):
			print("  " + vow + " > occurred " + str(counter) + " times.")
	else:
		print("\nHope you enjoyed!")
		sys.exit()
