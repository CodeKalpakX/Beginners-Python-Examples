#!/usr/bin/python
# -*- coding: utf-8 -*-


# *args is used when we don't know the exact number of 
# arguments are going that will be passed, so this placeholder
# is used commonly

def add_numbers(*args):
    res = 0
    for i in args:
        res += i
    return res

# Quick Test
t1 = add_numbers(123,435,876,12,54,76,78954,89,87,56,78,98,56,32,87)
if t1 == sum([123,435,876,12,54,76,78954,89,87,56,78,98,56,32,87]):
    print("Sum: " + str(t1))
else:
    print("Something went wrong!")

