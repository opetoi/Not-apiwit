import random

top_of_number = input("Please Enter a Number: ")

if top_of_number.isdigit():
    top_of_number = int(top_of_number)
    if top_of_number <= 0:
        print("The Number must be greater than 0")
    if top_of_number > top_of_number:
        print("The Number must be less than", top_of_number)
else:
    print("Please enter a number")

random_number = random.randint(0, top_of_number)
guesses = 0

while True:
    guesses = guesses +1
    guess_number = input("Make a Guess: ")
    if guess_number.isdigit():
        guess_number = int(guess_number)
        if guess_number == random_number:
            print("Correct!")
            break
        else:
            print("Incorrect")
    else:
        print("Please Enter a Number")

print("Congrat! You got it in", guesses, "guessss")

Wanna play [Rock, Paper, Scissors?](https://github.com/opetoi/Gpa-calculate/blob/main/Rock%2C%20Paper%2C%20Scissors.py)
