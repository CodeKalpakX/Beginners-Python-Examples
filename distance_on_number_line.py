# this is a simple geometric distance formula
# d(x,y) = |x-y| = distance
# where x and y are co-ordinates on a number line

def distance(x,y):
   return abs(x-y)

flag = True
while flag:
    usr = str(input("start [Y/n]: ")).strip().lower()
    if usr == "y":
        print(distance(float(input("Value of X co-ordinate: ")), float(input("Value of Y co-ordinate: ")) ), "\n")
    else:
        flag = False



# New_branch added Wow!