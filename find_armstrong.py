#getting input from user
num = int(input("Enter a number:"))

temp = num
rev = 0

#finding the sum
while(temp >0):
    dig = temp % 10
    rev += dig ** 3
    temp //=10


#display the result
if(num == rev):
    print(num," is a Armstrong number!")

else:
    print(num, " is not a Armstrong number!")