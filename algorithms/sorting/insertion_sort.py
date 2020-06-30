# -*- coding: utf-8 -*-

# Insertion Sort
# Ideal sorting algorithm for 
# small/small-medium data/array

# temporary parameter tells
# function to sort a copy of 
# orignal array, and not the array itself

# reverse parameter tells func
# to sort array in reverse/decending
# order


def sort_(arr,temporary=False,reverse=False):
    
    # Making copy of array if temporary is true
    if temporary:
        ar = arr[:]
    else:
        ar = arr
    
    # To blend every element
	# in correct position
	# length of total array is required
    length = len(ar)
    
    # After each iteration left-most
	# sub-array is completed sorted
    for i in range(1,length):
        # In each iteration we place
        # the current element to its
        # proper position in left sorted 
        # sub array
        tmp = ar[i]
        j = i-1
        if reverse:
            while j>=0 and tmp>ar[j]:
                ar[j+1]=ar[j]
                j-=1
            ar[j+1]=tmp
        else:
            while j>=0 and tmp<ar[j]:
                ar[j+1]=ar[j]
                j-=1
            ar[j+1]=tmp


    # if temporary, then returning
	# copied arr's sorted form
	# cuz if not returned, then function
	# is literally of no use
    if temporary:
        return ar


# See proper explaination 
# at: https://www.hotdogcode.com/insertion-sort/


# Testing
tests = [[7, 8, 9, 6, 4, 5, 3, 2, 1, 15], [1, 90, 1110, 1312, 1110, 98, 76, 54, 32, 10], ] # Add your test cases 

for test in tests:
	accend, decend = sort_(test, True), sort_(test, True, True)
	if accend == sorted(test) and decend == sorted(test, reverse = True):
		print("Orignal: {}".format(test))
		print("Sorted: {}".format(accend))
		print("Sorted(reverse): {}\n".format(decend))
	else:
		print("Something went wrong!\n")


# Seems our insertion sort works
# however for small/small-medium data/array!
