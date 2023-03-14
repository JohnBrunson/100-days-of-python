rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
print("Welcome to Rock, Paper, Scissors!")
print("ASCII art by unknown artist")
#Global variables
player_input = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors\n"))
cpu_input = random.randint(0, 2)
rps_list = [rock, paper, scissors]

#Some error checking...
if player_input >= 3 or player_input < 0:
  print("Invalid choice.")
else:
  print("Player chose: " + rps_list[player_input])
  print("CPU chose: " + rps_list[cpu_input])

  #Logic  
  if player_input == cpu_input:
    print ("This game is a draw")
  elif player_input == 0 and cpu_input == 1:
    print ("CPU Wins")
  elif player_input == 1 and cpu_input == 0:
    print("Player wins")
  elif player_input == 2 and cpu_input == 0:
    print ("CPU Wins")
  elif player_input == 0 and cpu_input == 2:
    print ("Player wins")
  elif player_input == 1 and cpu_input == 2:
    print ("CPU wins")
  elif player_input == 2 and cpu_input == 1:
    print("Player wins")

