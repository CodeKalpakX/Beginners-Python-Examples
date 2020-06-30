# -*- coding: utf-8 -*-

# Selection Sort
# Ideal sorting algorithm for 
# small/small-medium data/array

# temporary parameter tells
# function to sort a copy of 
# orignal array, and not the array itself

# reverse parameter tells func
# to sort array in reverse/decending
# order


def sort_(arr,temporary =False,reverse=False):

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
    for i in range(0,length):
        min = i

        # In each iteration we compare
        # current element with the right
        # unsorted sub-array and replace 
        # the minimum/maximum with current
        # element
        for j in range(i+1,length):

            # Checking for minimum/maximum
            if reverse:
                 if ar[min]<ar[j]:
                      min = j
            else:
                 if ar[min]>ar[j]:
                      min = j
       
       
        # Replacing minimum/maximum
        # with current element
        tmp = ar[i]
        ar[i]=ar[min]
        ar[min]=tmp
    
    

    # if temporary, then returning
	# copied arr's sorted form
	# cuz if not returned, then function
	# is literally of no use
    if temporary:
        return ar


# See proper explaination 
# at: https://www.hotdogcode.com/selection-sort/


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


# Seems our selection sort works
# however for small/small-medium data/array!

