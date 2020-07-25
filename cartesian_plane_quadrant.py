# quadrant determiner
# I(+,+) II(-,+) III(-,-) IV(+,-)

def determine_quadrant(x, y):
	try:
		if x > 0 and y > 0:
			return 'I(+,+)' 
		elif x < 0 and y > 0:
			return 'II(-,+)'
		elif x < 0 and y < 0 :
			return 'III(-,-)'
		elif x > 0 and y < 0 :
			return 'IV(+,-)'
		else :
			return 'Invalid parameters were provided'
	except TypeError:
		return "X and Y co-ords must be integers and not X {}, Y{}".format(type(x), type(y))

# Test
result = determine_quadrant(float(input('X co-ordinate: ')), float(input('Y co-ordinate: ')))
print("Quadrant is " + result)
