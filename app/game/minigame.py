import random
from app.system.systemcheck import cleansc

Computer = random.choice(["Rock", "Paper", "Scissors"])

def anwser():
    cleansc()
    print("Do you want to play again?")
    print("[1] Yes")
    print("[2] No")
    textInput = input('Please enter a number: (Default : Yes):')
    if (textInput == 1):
        game()
    elif (textInput == 2):
        exit()
    else:
        game()

def game():
    print("Welcome to the game")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")
    player = int(input('Please enter a number: '))
    if (player == 1):
        print("You chose Rock")
        print("Computer chose", Computer)
        if (Computer == "Rock"):
            print("Draw")
            anwser()
        elif (Computer == "Paper"):
            print("You lose")
            anwser()
        elif (Computer == "Scissors"):
            print("You win")
    elif (player == 2):
        print("You chose Paper")
        print("Computer chose", Computer)
        if (Computer == "Rock"):
            print("You win")
        elif (Computer == "Paper"):
            print("Draw")
            anwser()
        elif (Computer == "Scissors"):
            print("You lose")
            anwser()
    elif (player == 3):
        print("You chose Scissors")
        print("Computer chose", Computer)
        if (Computer == "Rock"):
            print("You lose")
            anwser()
        elif (Computer == "Paper"):
            print("You win")
        elif (Computer == "Scissors"):
            print("Draw")
            anwser()
    elif (player == 4):
        exit()
    else:
        anwser()
