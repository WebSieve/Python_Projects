import random

print(" ")
print(" WELCOME TO THE NUMBER GUESSING GAME. ")
print(" ")

correctno = random.randint(1, 100)
guesses = 0

while(guesses <= 7):
    num1 = int(input("enter a number between 1 to 100:  "))
    if num1 == correctno:
        print("CONGRATULATIONS, you guessed it.")
        break
    elif num1 < correctno:
        print(" ")
        print("you have guessed low.")
        print("try to select a number more than", num1)
        print(" ")
    elif num1 > correctno:
        print(" ")
        print("you have guessed high.")
        print("try to guess a number less than", num1)
        print(" ")
    guesses = guesses + 1