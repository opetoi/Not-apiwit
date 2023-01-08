#Rock, Paper, Scissors

import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_pick = input("Please Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_pick == "q":
        break
    if user_pick not in options:
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("computer picked", computer_pick, ".")

    if user_pick == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_pick == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_pick == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_pick == computer_pick:
        print("Draw")
        
    else:
        print("Computer won!")
        computer_wins += 1

    print("You won", user_wins, "times")
    print("The Computer won", computer_wins, "times")
print("Goodbye!")