# THIS SCRIPT IS TO UNDERSTAND
# THAN TO EXECUTE!

# Conditionals Examples
# if , elif , else 

# Condition Testing operators
# == checks equality
# != not equal to 
# > greater than
# < less than
# <= smaller than equal to
# >= greater than equal to

# Let's start with if 
# Let's say we have a robot and we want it to move forward by 20 steps
robotMoving = True
if robotMoving == True:
	print('Move 20 steps')

# Okay what about if robot is not moving
# This is where else : statement comes in 
robotMoving = False
else :
	print('You are not moving')	

# elif 
# What if there are multiple things to check like if
# We need more if statements but each if will run
# Thus we need elif(else if) statement 
# Only else : statements dont contain values to check
start = str(input('Enter a or b or c : '))
# we need to check if entered value is equal to a or b or c
if start == 'a':
	print('You entered ' + start)
elif start == 'b':
	print('You entered ' + start)
elif start == 'c':
	print('You entered ' + start)	
else:
	print('Invalid Input')

# Another Example
numsA = input('Enter a : ')
numsB = input('Enter b : ')
if numsA > numsB:
	print(str(numsA) + ' is greater than ' + str(numsB))
elif numsA < numsB:	
	print(str(numsB) + ' is greater than ' + str(numsA))
else : 
	print('Numbers are equal')	

# nested if else
# You can nest conditionals inside other conditionals
startProgram = True
numsA = input('Enter a : ')
numsB = input('Enter b : ')
if startProgram == True:
	if numsA > numsB:
		print(str(numsA) + ' is greater than ' + str(numsB))
	elif numsA < numsB:	
		print(str(numsB) + ' is greater than ' + str(numsA))
	else : 
		print('Numbers are equal')
else:
	print('Can\'t access program')	

#  and or not are helpful
# and returns True if both conditions are true
# or returns True if one of both condition is true	
# not returns True if condition is false and False if condition is True

# Think you have bike and you want to go out on a ride but you have to check if you have enough fuel
# remember not evaluates first then and then or 
# and 
youHaveBike = True
fuel = 30 
if youHaveBike == True and  fuel > 65:
	print('You are good to go')
else:
	print('You need to refill fuel')

# or
extraFuel = True
if extraFuel = True or  fuel > 65:
	print('You are good to go')
else:
	print('You need to refill fuel')

# not
number = 12
if not(number != 11):
	print('True')
else:
	print('False')
