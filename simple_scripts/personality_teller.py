#!/usr/bin/python
# -*- coding: utf-8 -*-

# Personality Teller
import random

# Chooses personality randomly
# Just for fun!
# Don't be serious!

personalities = ['Arrogant and Rude','Funny and Polite','Insane and Crazy'
,'Lover and Cute','Nerd and Boring','Cool and Rude','Cute but arrogant','Intelligent and Geek'
,'Cool and Funny','Idiot and Crazy','Awesome and Crazy','Good and Smart','Cool and Smart',
'Smart and Geek','Cool and Smart']

while True:
    if raw_input("\nPress(e) to Exit,\nName?: ").strip() == "e":
        print("\nHope you enjoyed!")
        exit(0)
    else:
        print("  > You are %s" % random.choice(personalities))
