#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys

# Binary to decimal conversion
# See explaination: https://i.imgur.com/heAT0PB.gif   , 
# https://www.electronics-tutorials.ws/binary/bin_2.html

def binary_to_decimal_conv(binary_string):
	res = 0
	binary_l = list(binary_string)
	for bit_i in range(len(binary_l)):
		res += int(binary_l[bit_i]) * (2 ** bit_i) 
	return res 

# Test
# Testing interface
i = 0
while True:
	if raw_input("\n[{}] Exit(press e) or Continue(press c): ".format(i)).strip().lower() == "c":
		print("Decimal form: " + str(binary_to_decimal_conv(raw_input("\nBinary?: "))))
	else:
		print("\nHope you enjoyed!")
		sys.exit()
	i += 1
