#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

# Collatz conjecture
# is a series of numbers
# where the orignal number is manipulated, until
# one is obtained
# if n is even n // 2 is the next number
# else n * 3 
# No matter what the value of n we'll,
# always reach 1.
# See: https://en.wikipedia.org/wiki/Collatz_conjecture

# Collatz series generator
def collatz_conjecture(n):
    if n < 1: 
    	raise Exception("\n  Expected a value greater than 1")
	
    while n != 1:
		if n % 2 == 0:
			n = n // 2
		else: n = 3*n + 1
		yield n

# If n will be negative then
# sequence will be infinite

# Interface
# Test/Play
i = 0
while True:
	if raw_input("\n[%i] Continue[Y/n]?: " % i).strip().lower() == "y":
		for v in collatz_conjecture(int(raw_input("N?: "))):
			print("  > " + str(v))
		i += 1
	else:
		print("\nSee you soon!")
		sys.exit(0)

