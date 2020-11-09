#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys

# Functions to apply basic arithmetic
# operations on 2 numbers
# Each func, takes 2 numbers as input

add = lambda a, b: a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b
modulus = lambda a, b: a % b

# CLI
# Testing/Playing Interface
i = 0
while True:
	if input("\n\n[{}] Exit(press e) or Calculate(press c): ".format(i)) == "c":
		op = input("\nAdd(press a), Subtract(press s), Multiply(press m),\nDivide(press d), Modulus(press mo): ").strip().lower()
		if op == "a":
			print("  Sum: " + str(add(float(input("\nN1: ")), float(input("N2: ")))))
		elif op == "s":
			print("  Subtracted: " + str(subtract(float(input("\nN1: ")), float(input("N2: ")))))
		elif op == "m":
			print("  Multiplied: " + str(multiply(float(input("\nN1: ")), float(input("N2: ")))))
		elif op == "d":
			print("  Divided: " + str(divide(float(input("\nN1: ")), float(input("N2: ")))))
		else:
			print("  Modulus: " + str(modulus(float(input("\nN1: ")), float(input("N2: ")))))
		i += 1
	else:
		print("\nHope you enjoyed!")
		sys.exit()
