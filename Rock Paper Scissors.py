import random
choice = "y"

while choice == "y":
  comp = random.randint(0, 2)
  if(comp == 0):
    rps = "rock"
  elif(comp == 1):
    rps = "paper"
  else:
    rps = "scissors"
  guess = input("Hey, lets play Rock Paper Scissors. What do you choose? ").lower()
  if(guess == rps):
    print("Thats a tie, try again?")
  elif(guess == "rock"):
    if(rps == "paper"):
      print("You lose, paper beats rock")
    else:
      print("You win, rock beats scissors")
  elif(guess == "paper"):
    if(rps == "scissors"):
      print("You lose, scissors beats paper")
    else:
      print("You win, paper beats rock")
  elif(guess == "scissors"):
    if(rps == "rock"):
      print("You lose, rock beats scissors")
    else:
      print("You win, scissors beats paper")
  choice = input("\nDo you want to play again? (y/n) ").lower()
print("\nAh Well, lets play again later. bye")
