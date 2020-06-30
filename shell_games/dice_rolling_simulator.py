# Add encoding and path to executable


import sys
import time
import random


class DiceRollSim:
	def __init__(self, no_of_players, no_of_dies):
		self.players = self.assign_names(no_of_players)
		self.die_n = no_of_dies

	def assign_names(self, n):
		# Assigns names to 'n' players playing
		dict_players = {}

		# All members are indentified by name
		# and not number
		for i in range(n):
			dict_players[i + 1] = str(
			    input("Name for player({}): ".format(i + 1)))
		
		return dict_players

	def roll_die(self):
		# Roll die n number of times 
		# In case playing with multiple dies
		return [random.randint(1, 6) for roll in range(self.die_n)]

	def play(self):
		# Main
		rounds = 0
		while True:
			# Continue playing until desired
			if str(input("\n\n[+]Continue [Y/n]? ")).strip().lower() == "y":
				print("\nRound-> %d" % rounds)

				# Print rolled die upper face number/s
				# for each player playing, along with sum for quick moves
				for player_num in self.players.keys():
					rolled = self.roll_die()
					print("  > Chance of player %s:  %s  total: %d" %
					      (self.players[player_num], rolled, sum(rolled)))

					# Delay for better user experience
					time.sleep(5)

				# Update rounds played
				rounds += 1
				continue
			else:
				# Finished playing
				print("\n > Rounds played: %d" % rounds)
				break


def main_interface():
	# Indroductions
	print(" " * 7 + "| Dice Rolling Simulator | \n\n")

	# Initializations/Declarations
	players_n = abs(int(input("> How many players?  ")))
	die_n = abs(int(input("> Number of dies?  ")))
	print("\n\n")
	die_rolling_simulator = DiceRollSim(players_n, die_n)

	print("\nNumber of players playing -> %d\nWith %d dies." % (players_n, die_n))
	# And the game begins
	die_rolling_simulator.play()

	print("\n\nSee you at another game!")
	sys.exit(0)


main_interface()
