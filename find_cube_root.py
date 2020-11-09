
# This method is called exhaustive numeration!
# I am checking every possible value
# that can be root of given x systematically
# Kinda brute forcing

def find_cube_root(x):
	try:
		x = int(x)
		for i in range(0, x):
			if i ** 3 == x:
				return i
		return f"{x} is not a perfect cube"

	except ValueError:
		return "Expected an integer! Cannot find cube root of an string!"


# Test
x = 27
result = find_cube_root(x)
if type(result) == int:
	print("Cube root of {} is {}".format(x, result))
else:
	print(result)
