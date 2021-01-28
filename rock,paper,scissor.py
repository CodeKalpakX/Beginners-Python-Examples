import random
print("Welcome to Rock, Paper, Scissors Game")
uchoice = input("Scissors, Rock, Paper ?")
choice = ['Scissors', 'Rock', 'Paper']
mchoice = random.choice(choice)
print(mchoice)

if mchoice == uchoice:
    print("Tie")
elif mchoice == choice[0] and uchoice == 'Rock':
    print("You win")
elif mchoice == choice[2] and uchoice == 'Rock':
    print("You loose")
elif mchoice == choice[0] and uchoice == 'Paper':
    print("You loose")
elif mchoice == choice[1] and uchoice == 'Paper':
    print("You win")
elif mchoice == choice[1] and uchoice == 'Scissors':
    print("You loose")
elif mchoice == choice[2] and uchoice == 'Scissors':
    print("You win")
else:
    print("Please enter valid choice!")
