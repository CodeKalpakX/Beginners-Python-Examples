# pre code

def square():
    print(" ")
    makeUse = raw_input("Square or Cube : ")
    if makeUse.strip() == "Square":
        print(" ")
        user = int(raw_input("Enter number to get square : "))
        square = user ** 2
        print(" ")
        print("Square of the number " + str(user) + " is " + str(square))
    elif makeUse.strip() == "Cube":
        print(" ")
        userAgain = int(raw_input("Enter number to get cube : "))
        cube = userAgain ** 3
        print(" ")
        print("Cube of the number " + str(userAgain) + " is " + str(cube))

# main code

while True:
    print("Hello,")
    print(" ")
    startOrEnd = raw_input("Start or End : ")
    print(" ")
    if startOrEnd.strip() == "Start":
        print(square())
    elif startOrEnd.strip() == "End":
        print(" ")
        print(" ")
        print("Program Ended......")
        break
    else :
        print(" ")
        print("Try Again")
        continue
    startagain = ("Start again or End : ")
    print(" ")
    if startagain.strip() == "Start again":
        print(" ")
        print("Starting again.....")
        continue
    elif startagain == "End":
        print(" ")
        print(" ")
        break
    else :
        print(" ")
        print("Try Again")
        continue
