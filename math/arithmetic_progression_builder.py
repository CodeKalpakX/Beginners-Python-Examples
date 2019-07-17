#!/usr/bin/python
# -*- coding: utf-8 -*-

# Arithmetic progressions
# are special types of sets(more of a series)
# where the difference between every consecutive
# numbers of series is constant or common
# for more refer: https://en.wikipedia.org/wiki/Arithmetic_progression

# formula for general term of arithmetic prog.
# tn = a + (n - 1) * d
# where, 
#    tn -> is the n(th) term, 
#    a -> if the first term, 
#    d -> is the common difference 

# Third param 'n_last' refers to limit or length or index of last term

def arithmeticProgression(a=1, d=1, n_last=1):
	'''Generates a sequence of Arithmetic Progression '''

	# To generate an A.P. length should be
	# greater than or equal to 1
	if n_last < 1:
		return -1

	seq = []

	# Every item is obtained by
	# applying the general term formula
	for n in range(1, n_last + 1):
		seq.append(a + (n - 1) * d)
		
	return seq 

# Test
if __name__ == "__main__":
	print("Arithmetic Progression builder")
	
	#Take inputs
	a = int(input("Enter the first term: "))
	d = int(input("Enter the common difference: "))
	n_last = int(input("Enter the number of terms desired: "))
	
	#call function
	sequence = arithmeticProgression(a, d, n_last)
	
	#display result
	if sequence == -1:
		print("The number of terms required should be greater than 1")
	else:
		print("Your sequence is: {}".format(sequence))
	
