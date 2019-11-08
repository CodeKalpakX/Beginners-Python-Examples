#Profit Loss calculator in python

i=input('Enter cost : ')
s=input('Enter selling cost : ')
k=s-i
if(k>0):
	print('Profit : ' + str(k))
elif(k<0):
	print('Loss : ' +  str(-k))
else:
	print("NO Profit NO Loss")
