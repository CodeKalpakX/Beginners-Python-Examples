# piggy bank
# pre code
money = 0

# function to add money to current amount
def addMoney():
    print(" ")
    userAdd = float(raw_input("Add money : "))
    print(" ")
    money = money + userAdd
    print("After adding current Money you have is " + str(money) + " rupees")

# function to withdraw money from current amount
def withdrawMoney():
    print(" ")
    userWithdraw = float(raw_input("Add money : "))
    print(" ")
    money = money - userWithdraw
    print("After adding current Money you have is " + str(money) + " rupees")

# function to display current amount
def currentMoney():
    print(" ")
    current = "Current money you have is " + str(money) + " rupees"

# main code
print(" ")
print("--------------------Start-------------------")
while True:
    print(" ")
    user = raw_input("Start or End : ")
    if user.strip() == "Start":
        controlPiggy = raw_input("Add Withdraw or Check : ")
        if controlPiggy.strip() == "Add":
            print(addMoney())
            continue
        elif controlPiggy.strip() == "Withdraw":
            print(withdrawMoney())
            continue
        elif controlPiggy.strip() == "Check":
            print(currentMoney())
            continue
        else :
            print(" ")
            print("Invalid Input.Try again")
            continue

    elif user.strip() == "End" :
        print(" ")
        print("------------Program Ended-----------")
        print(" ")
        break

    else :
        print(" ")
        print("Invalid Input. Try again")
        continue
