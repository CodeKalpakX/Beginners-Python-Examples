# Creating tuples
# Tuples are used to store 2-d grids and fixed values
# tuples are immutable that means they cant be changed

tupA = () # Empty tuple
print(tupA)

c = 12,56,78

tupC = tuple(c) # tuple() is built-in
print(tupC)

x,y,z = (12,45,42)

a = x,y,z
print(a)
print(type(a))

# Accessing items in tuples
print(tupC[0])
print(a[1])
print(tupC[2],'\n')

# tuples cant be reassigned
# tupC[1] = 18 # uncomment this line to see the error  this should cause a error 'TypeError'

# iterating through tuples
for x in tupC:
	print(x)
	
	
	
	########
	
thistuple = ("apple", "banana", "cherry")
print(thistuple)
	
