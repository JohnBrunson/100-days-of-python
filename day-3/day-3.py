print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("ASCII Art courtesy of https://ascii.co.uk/art")
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

player_response = input("You\'re at a crossroad. Where do you want to go? Type \"left\" or \"right\"\n")
player_response = player_response.lower()
if player_response == "right":
  player_response = input("The door opens to a dock on the lake. You see an island in the distance. Type \"wait\" to wait for a boat. Type \"swim\" to swim across the lake\n")
  player_response = player_response.lower()
  if player_response == "wait":
    player_response = input("You arrive at the island unharmed. There is a house with three doors. One red, one yellow, and one blue. Which color do you choose?\n")
    player_response = player_response.lower()
    if player_response == "red":
      print("Flames leap out and burn you to bits! Game over.")

    elif player_response == "blue":
      print("The three headed monster eats your face off! Game over.")

    elif player_response == "yellow":
      print("You have found the treasure! You win!")
  else:
    print("You are attacked by the resident Kraken. Doesn't look good for you! Game over.")
else:
  print ("The door turns ravenous and consumes you! Game over.")
  