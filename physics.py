# physics calcy

operations = ["1. Pressure", "2. Force", "3. Speed", "4. Velocity", "5. Accelaration", "6. Momentum"]


# pre code sector I
# preassure function to calculate preassure
def pressure():
    force = int(input("\nEnter force : "))
    area = int(input("\nEnter area : "))
    preassure = force / area
    print(f"\nPreassure is {preassure}")


# force function to calculate force
def force():
    mass = int(input("\nEnter mass : "))
    accelaration = int(input("\nEnter accelaration : "))
    force = mass * accelaration
    print(f"\nForce is  {force} Newtons")


# speed func to calculate speed of object
def speed():
    distance = int(input("\nEnter distance : "))
    time = int(input("\nEnter time taken : "))
    speed = distance / time
    print(f"\nSpeed of object is {speed}")


# velocity func to calculate velocity of object
def velocity():
    displacement = int(input("\nEnter displacement : "))
    time = int(input("\nEnter time taken : "))
    velocity = displacement / time
    print(f"\nVelocity of object is {velocity}")


# accelaration func to calculate accelaration
def accelaration():
    initialV = int(input("Enter initial velocity : "))
    finalV = int(input("Enter final velocity : "))
    time = int(input("Enter time taken : "))
    acce = (finalV - initialV) / time
    print(f"Accelaration is {acce}")


# monentum func to calculate momentum
def moment():
    mass = int(input("Enter mass : "))
    velocity = int(input("Enter velocity : "))
    momentum = mass * velocity
    print(f"Momentum is {momentum}")


# CLI code sector II

while True:
    print("\nHello,")
    startOrEnd = input("Start or End : ")
    if startOrEnd.lower() == "start":
        for op in operations:
            print(op)

        main = int(input("\nEnter 1-6 for Desired Operation : "))
        if main == 1:
            print(pressure())

        elif main == 2:
            print(force())

        elif main == 3:
            print(speed())

        elif main == 4:
            print(velocity())

        elif main == 5:
            print(accelaration())

        elif main == 6:
            print(moment())

        else:
            print("Invalid operation")

    elif startOrEnd.lower() == "end":
        print("...Progarm Ended...")
