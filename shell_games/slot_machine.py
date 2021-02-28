import random

while True:
  # set of options
  options = ["Skull","Diamond","Heart","Star","Blood"]
  # random outcome 
  for i in range(0,3):
    print(random.choice(options))
    
  # play again? 
  if int(input("Press 1 if you Would You Like To Play Again? ")) == 1:
    print("")
    continue
  else:
    # What did the user earn? lol
    print("You earned.")
    break
