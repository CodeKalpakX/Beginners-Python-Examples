"""
Made by github.com/ClarkeCDC
Don't edit the passwords.csv file
"""

import random
import csv

alphabet = []

def createPassword(length):
    password = []
    for i in range(length):
        password.append(random.choice(alphabet))

    return "".join(password)


def getAsciiCharacters():
    print("Gaining all characters")
    for i in range(97,123):
        alphabet.append(chr(i))

    for i in range(65,91):
        alphabet.append(chr(i))

    for i in range(0,10):
        alphabet.append(str(i))
    alphabet.append("!")
    alphabet.append("$")
    


def saveToCsv(account, password):
    with open("passwords.csv", "a") as csvfile:
        fieldnames = ["account", "password"]
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writerow({"account": account, "password": password})
        csvfile.close()
    
def printPasswords():
    with open("passwords.csv") as csvFile:
        reader = csv.DictReader(csvFile)
        print("\n")
        for row in reader:
            print("Account: " + row["account"] + "  Password: " + row["password"])
        print("\n")
        csvFile.close()
        
def deletePassword():
    with open("passwords.csv","r") as file:
        printPasswords()
        lines = file.readlines()
        line = 0
        account = input("Which password would you like to delete?\nAccount Name: ")
        for row in lines:
            if account in row:
                del lines[int(line)]
                print("deleting the password for the account, "+account)
                open("passwords.csv","w").writelines(lines)
            line = line + 1
        

def userOption():
    pLen = int(input("Hoe many characters do you want your password to have?\n>>>"))
    account = input("What is this password for?\n>>>")
    password = createPassword(pLen)
    print(password)
    saveOption = input("Would you like to save this password? (y/n)\n>>>")
    if (saveOption.lower() == "y"):
        saveToCsv(account, password)
        print("Password has been saved to database")
        
getAsciiCharacters()

while True:
    option = input("C - Create A Password\nD - Delete a Password\nV - View Your Passwords\n>>>")
    if (option.lower() == "c"):
        userOption()
    elif (option.lower() == "v"):
          printPasswords()
    elif (option.lower() == "d"):
        deletePassword()
    else:
        print("That is not option\n")
