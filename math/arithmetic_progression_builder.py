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
#	 a -> if the first term, 
#    d -> is the common difference 

# Third param 'n_last' refers to limit or length or index of last term

def arithmetic_p_sequence_builder(a, d, n_last):

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
print("Arithmetic progression: {}".format(arithmetic_p_sequence_builder(int(raw_input("A(a, first term): ")), int(raw_input("D(d, common difference): ")), int(raw_input("N(n, length): ")))))

# Although big line, but works just fine!
