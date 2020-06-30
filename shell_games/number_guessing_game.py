#!/usr/bin/python3
from random import randint

MAX_ = 500 # Specify biggest possible value from random number generation

# Asks user for a guess and returns this when successful
def get_guess():
	while True:                                         # Run forever, until broken
		try:                                            # Try the following, if fails, run the except statment
			user_input = int(input("Guess a number: ")) # Get user input and covert it to an int (number)
			break                                       # If the input can be converted, break the loop
		except ValueError:                              # This runs if the input could not be converted - text was entered
			print("Enter a number!\n")                  # Tell them to enter a number, then run loop again
	return user_input                                   # Return value when loop broken

num_to_guess = randint(0, MAX_) # Generates a random number between 0 and value of MAX_
print("Welcome to my random number guessing game!\nGuess a number between 0 and ", MAX_, "\n")

while True:
	guess = get_guess()
	if guess >= 0 and guess <= MAX_: # Check if guess between 0 and max

		# Correct number!
		if guess == num_to_guess:
			print("That's a correct guess!\nYou got it!\n")
			break

		# Incorrect - give hint
		elif guess < num_to_guess:
			print("Try a bigger num!")  # Number to small
		else:
			print("Try a smaller num!") # Number to big

	# Number is not in range
	else:
		print("Enter a number in between 0 and ", MAX_) 
	
	print("")

'''

*Challenge*

	 1) Can you give the user the option to Play Again? 
	  - if yes, the game will reset - including the random number

	 2) Try count the number of guesses and give a score to the user when they guess the number 
	  - the lower the guesses, the higher the score

'''
