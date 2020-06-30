#!/usr/bin/python
# -*- coding: utf-8 -*-

def squared(n):
	return n * n 

def cubed(n):
	return n * n * n 

def raise_power(n, power):
	for t in range(power):
		n *= n 
	return n 

def is_divisible(n, t):
	return n % t == 0

def is_even(n):
	return n % 2 == 0

def is_odd(n):
	return n % 2 != 0

# These all functions are extremely 
# helpful when used with map method of python
# map(func, list) basically applies given function 
# to every element of list and appends results to a new
# list

# e.g.
print(map(squared, [1, 3, 5, 7, 9, 11, 13, 15]))

# for functions with multiple args
# see: https://www.quora.com/How-do-I-put-multiple-arguments-into-a-map-function-in-Python

