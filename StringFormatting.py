a = "This is a string and you need to print it and become a better Pythonista. Good Luck"

#Type 1 : The Boring way

a , b , c = 10 , 20 , 30
print("A = " , a , ", B = ", b , ", C = " , c , "and the sum of A , B , C is " , a+b+c)

# A bit more Pythonic way

x= "A = {} , B = {} , C = {} and the sum of A,B,C is {}".format(a,b,c,a+b+c)
print(x)

#My favourite way (Python String Interpolation)

x = f"A = {a} , B = {b} , C = {c} and the sum of  A , B , C is {a+b+c}"
print(x)
