

import os
import sys
import webbrowser
from time import sleep as sleep_sheep 


# Executing ping with input host
# using systems functionality (only linux)
def ping(host):
	instr = "ping -c 1 %s" %(host) 
	response = os.system(instr)
	return response == 0


# Finite state loop if 
# computer re-connects to network
# else will run till re-conn
def you_cant_be_dead(host):
	if (not ping(host)):
		# Status update
		print("  [.] Status -> Not connected to network")
		print("  / CONSTANTLY Re-CHECKING CONNECTIVITY... /")
		while (True):
			if not ping(host): continue
			else: break

			# Connectivity is checked 
			# every 7 secs
			sleep_sheep(7)

	return True


def exit_(status):
	if (status == 0 or status == 1):
		print("\n ~ See you soon!")
		sys.exit(status)
	else:
		return None


# User 
# Shell Interface
while True:
	if raw_input("\nStart [Y/n]? ").strip().lower() == "y":
		inp = raw_input("URI (alive) HOST: ").strip()
		print("\n > CHECKING CONNECTION...\n > Host -> %s\n" % inp)
		
		if you_cant_be_dead(inp):
			# When connected to internet
			# Status update, and proof of connection
			print("\n  [.] Status -> CONNECTED to network")
			webbrowser.open("https://www.youtube.com/watch?v=JbjIH5pvT5A")
			exit_(0)

	else:
		exit_(0)
