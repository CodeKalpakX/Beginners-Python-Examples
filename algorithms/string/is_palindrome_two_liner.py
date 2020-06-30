

import string

def is_palindrome(s):
	# String Clenasing
	s = "".join([char for char in list(s.lower()) if char in list(string.ascii_lowercase)])
	
	# (index+1) * -1 gives negative index of corresponding counterpart
	# for e.g. s = "noon"  s[0] = s[-1] = "n"  and so on 
	#  all() and list comprehensions make task so easy!!
	return all([s[index]==s[(index+1)*-1] for index in range(0, len(s))])


# Tests
print(is_palindrome("racecar"))
print(is_palindrome("ra cec, a?r   "))  // True
print(is_palindrome("noooonnn"))
print(is_palindrome("cool..eh")
