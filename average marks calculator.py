t=0
subs=('IP', 'Chemistry', 'Maths', 'Physics', 'English')
print('Enter Marks out of 100 for all subjects')
for i in subs:
	s = float(input(i+" : "))
	t+=s
a=t/5
print("your average marks is {0}".format(a))
