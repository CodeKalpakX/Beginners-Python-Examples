#!/usr/bin/python
# -*- coding: utf-8 -*-

import string, sys

# Caesar's cipher is type of shift cipher, 
# an encryption technique
# First used by roman rular Julius Caesar
# To see how it works refer:
# web-page/article: https://en.wikipedia.org/wiki/Caesar_cipher OR 
#                   https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/caesar-cipher


def caesars_cipher_encoding(s, k, lowercase = True, uppercase = False):
	
	# To encrypt plain text in either 
	# uppercase letters or lowercase letters
	if lowercase:
		alphas = list(string.lowercase)
	elif uppercase:
		alphas = list(string.uppercase)

	encrypted = ""
	# List characters in orignal string
	char_s = list(s)

	# Shifting of each single 
	# character in orignal string
	# using given key
	for char in char_s:

		# avoid encryption of spaces
		if char == " ":
			encrypted += " "
		
		else:  
			# n_index or new index is
			# the index of encrypted character
			n_index = k + alphas.index(char)
			
			# if encrypted character is greater than
			# length of english alphabets
			if n_index > 25:

				# Read explaination on line 59
				while not n_index <= 25:
					n_index = n_index - 26
				encrypted += alphas[n_index]
			
			# simple shift
			else:
				encrypted += alphas[n_index]
				
	return encrypted

# Explaination of key bigger than 26:
# say we have key 54, 
# we add index of char(say 'a') to key, i.e. key = 54 + 1 = 55
# so after first iteration over array of length(26), 
# i.e. 55(total iterations to perform) - 26(iterations completed) = 29(iterations left)
# but, 29 is still a big index i.e. 29 > length of array(26)
# so we continue to subtract more 26(iterations), 
# i.e. 29(iterations to perform) - (26 iterations done) = 3(remaining)
# so 3 is smaller than length of array and can be used as key, 
# i.e. 3 < 26(length of array)
# thus, we reached at index of 3 after 54 iterations over an array of length 26
# bit complicated but read it twice, you'll master it!

# Test, Playing UI
i = 0
while True:
	if raw_input("[{}] Exit(press e), To continue(press c): ".format(i)).lower() == "c":
		# Number of times 
		i += 1

		# Input for String and key for char shift
		S, K = raw_input("\nString: "), int(raw_input("Key: "))
		
		# Results
		print("\nOrignal string: " + S + " ,  Key: " + str(K))
		print("Encrypted text: " +  caesars_cipher_encoding(S, K, True, False) + "\n")
	
	else:
		sys.exit()
