# Add Encoding and path to exec 


from random import randint
import sys


class BattleShip:
	def __init__(self, rows_grid, columns_grid, co_ord_symbol):
		# Initializes battleship board of n * m size
		self.board = self.create_board(rows_grid, columns_grid, co_ord_symbol)
		
		# Placing ship randomly on board x refers to 
		# array, y refers to index in array
		self.ship_x = randint(0, rows_grid)
		self.ship_y = randint(0, columns_grid)


	def create_board(self, x_length, y_length, co_ord_symbol="o "):
		# creates a multi-dimensional array of 
		# n * m length
		return [[co_ord_symbol]*x_length for col in range(y_length)]


	def view(self):
		# For graphical representation of board
		for row in self.board:
			print(" ".join(row))


	def is_ship_there(self, x_cord_guess, y_cord_guess):
		# Check if ship exists at given co-ordinates
		if self.ship_x == x_cord_guess and self.ship_y == y_cord_guess:
			return True

		return False


	def no_place_for_old_guess(self, row, col):
		# Replaces the co-ordinate at wrong guessed
		# ship position for convinience with X
		self.board[row][col] = "X "


	def get(self, row, col):
		# For UI purpose see ln 72
		return self.board[row][col]


def battleshipUI():
	# Maximum n turns for player to guess the position of ship
	max_turns = 5
	turns = 0


	# Board of rows * columns for playing
	rows = int(input("How many rows? "))
	cols = int(input("How many columns? "))
	lets_battle = BattleShip(rows, cols, "o ")

	
	# Execute until user runs out of chances
	while turns < max_turns:
		# View the board at each new chance
		print("\n\nOcean:")
		lets_battle.view()


		# User to guess position of ship
		row_guess = int(input("\nGuess row? "))
		col_guess = int(input("Guess column? "))


		# Conditions if user guessed correctly,
		# or missed it or guessed extremely wrong
		# co-ordinates
		if lets_battle.is_ship_there(row_guess, col_guess):
			print("\n  > Damn! You sunk my SHIP!")
			print("  > You Won the Game!\n\nSee You Soon!")
			sys.exit(0)
		
		elif (row_guess >= rows or row_guess < 0 or col_guess >= cols or col_guess < 0):
			print("\n - Ship isn't even in Ocean!")
		
		else:
			if lets_battle.get(row_guess, row_guess) == "X ":
				print("\n - Really you tried that already!")
			else:
				print("\n - Wrong Guess! Use your sailor's instincts!")
			
			# Replace symbol o with X to tell user 
			# He/She already tried those co-ordinates
			lets_battle.no_place_for_old_guess(row_guess, col_guess)

		turns += 1

	print("\n~~~GAMEOVER~~~")


battleshipUI()
