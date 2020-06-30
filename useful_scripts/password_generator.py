#!/usr/bin/python
# -*- coding: utf-8 -*-


# Now-a-days, hashes of our passwords are 
# flowing on internet, but to avoid password
# getting discovered by whoever got their hands
# on them, a password should contain:
#             1. Least 8 characters
#			  2. No words, instead randomly chosen characters
# 			  3. Characters i'm refering to are, numbers, 
#				 uppercase/lowercase letters, punctuation's
# This will protect password against, dictionary/brute force attacks


import random, string, sys

# List of characters, alphabets, numbers
# to choose from
data_set = list(string.ascii_letters) + list(string.digits) + list(string.punctuation)

# generates a random password 
# very strong due to random ness
# primary protection against dictionary attack on hash tables

def generate_random_password(n):
	# For password to be strong it should
	# be at least 8 characters long
	if n < 8:
		return "Invalid Input,\nPassword should be at least 8 characters long!"
	
	# Chooses a random character from data_set
	# after password of given length is created
	# returns it to user
	password = ""
	for x in range(n):
		password += random.choice(data_set)
	
	return password 

# Test

while True:
	usr = raw_input("Exit(press e), or Length: ").lower()
	if usr == "e":
		sys.exit()
	
	print("Generated password: " + generate_random_password(int(usr)) + "\n")
