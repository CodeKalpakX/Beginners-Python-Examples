#!/usr/bin/python
# -*- coding: utf-8 -*-


# *params is just a placeholder(try putting other name) 
# for n number of arguments
# so that n can be any number, instead of params
# any name can be used, but the * asterisk is important

# Below function, is a generator
# generates a tuple containing arg, and a boolean value
# every time it encounters argument
def squared(*params):
    for arg in params:
        yield((arg, arg % 2 == 0))

# Quick Test
print("Divisibility Test(by 2): ")
for n, bool_ in squared(12, 13, 34, 4576, 234536, 2341):
    if bool_:
        print("  [" + str(n) + "] -> is divisible by 2!")
    else:
        print("  [" + str(n) + "] -> is NOT divisible by 2!")
