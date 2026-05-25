"""
GAME: ROCK PAPER SCISSORS

===== VARIABLES =====

Players(2):
    - playerOne
    - playerTwo(computer)

gameChoices:
    - "rock"
    - "paper"
    - "scissors" 

===== FUNCTIONS =====
- Get player choices
    - playerOne selects choice
    - playerTwo selects choice
    - print out playerOne and playerTwo choices

- Determine Winner: 
    - playerOne and playerTwo select the same choice == IT'S A TIE!
    - if playerOne selects "rock":
        if playerTwo selects "paper":
            "Paper covers rock, PLAYER TWO WINS!"
        if playerTwo selects "scissors":
            "Rock crashes scissors, PLAYER ONE WINS!"

    - if playerOne selects "paper":
        if playerTwo selects "rock":
            "Paper covers rock, PLAYER ONE WINS!"
        if playerTwo selects "scissors":
            "Scissors cut paper, PLAYER TWO WINS!"

    - if playerOne selects "scissors":
        if playerTwo selects "rock":
            "Rock crashes scissors, PLAYER TWO WINS!"
        if playerTwo selects "paper":
            "Scissors cut paper, PLAYER ONE WINS!"

"""
""" 

gameChoices:
    - "rock"
    - "paper"
    - "scissors" 
"""

import random 

gameChoices = ["rock", "paper", "scissors"]
output =""

# selectChoices
def selectChoices():
    playerOneName =input("Enter your player name: ")
    playerOneChoice = input("Enter your poison (rock, paper, scissors): ")
    playerTwoChoice = random.choice(gameChoices) # computer
    output= f"PlayerOne({playerOneName}): {playerOneChoice} || PlayerTwo(Comp): {playerTwoChoice}"
    print("\n\n======================= PLAYER CHOICES ======================= ")
    print(output)
    print("======================= PLAYER CHOICES ======================= ")

    return playerOneName, playerTwoChoice, playerOneChoice

# determineWinners
def determineWinner(playerOneName, playerTwoChoice, playerOneChoice):
    if playerOneChoice == playerTwoChoice:
        return "It's a TIE!"

    elif playerOneChoice == "rock":
        if playerTwoChoice == "paper":
            return "Paper covers rock, COMP WINS!"
        elif playerTwoChoice =="scissors":
            return f"Rock smashes scissors, {playerOneName} WIN!"

    elif playerOneChoice == "paper":
        if playerTwoChoice == "rock":
            return f"Paper covers rock, {playerOneName} WIN!"
        elif playerTwoChoice =="scissors":
            return "Scissors cut paper, COMP WINS!"

    elif playerOneChoice == "scissors":
        if playerTwoChoice == "rock":
            return "Rock smashes scissors, COMP WINS!"
        elif playerTwoChoice =="paper":
            return f"Scissors cut paper, {playerOneName} WIN!"

playerOneName, playerTwoChoice, playerOneChoice = selectChoices()
output = determineWinner(playerOneName, playerTwoChoice, playerOneChoice)

print("\n\n======================= ✨ WINNNER ✨  ======================= ")
print(output)
print("======================= ✨ WINNNER ✨ ======================= \n\n")