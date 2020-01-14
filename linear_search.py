# Linear Search or Sequential Search Algorithm

def linear_search(array, to_find):
	pos = 0			# Starting position or index
	to_return = (False, 0)
	while (pos < len(array)):		# while index is less than length of array
		if (array[pos] == to_find):		# if array with index of var pos is equal to find
			to_return = (True, pos)			# no need to break loop cuz return appends func
			return to_return
		else: 
			pos = pos + 1		# if elem not found continue to next pos 
	return to_return
	
nums = [12, 34, 54, 88, 21]			
print(linear_search(nums, 88))			
