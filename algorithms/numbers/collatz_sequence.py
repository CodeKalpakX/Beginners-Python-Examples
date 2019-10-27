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
print("Collatz Sequence")
x = int(input("Enter a number: "))

def collatz(n):
    print(n)
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = (n * 3)+ 1
        print(n)


collatz(x)
