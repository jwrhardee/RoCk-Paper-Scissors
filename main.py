import random

choices = ["rock", "paper" , "scissors"]

computer = random.choice (choices)
print (computer)

player = input("choose rock paper or scissors:\n")

print ("you choose:"+player)

#who wins
if player == computer:
  print ("Tie Game")
else:
  if player == "rock":
    if computer == "paper":
      print ("computer Won ")
    else:
      print("Player Won")
  elif player == "paper":
    if computer == "scissors":
      print ("computer Won")
    else:
        print ("player Won")
  else: 
    if computer == "rock":
      print ("compueter Won ")
    if computer == "paper":
      print ("Player wins")
