import random 
# display the welcome mesasge and game rules 
def welcome_message():
    print("Welcome to the Number Guessing Game! 🎉")

def random_number():
    # generate and return a number between 1 and 100 
    return random.randint(1,100)

def player_guess():
    while True:
        try:
            guess = int(input("Guess the number between (1-100):"))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 to 100")

        except:
                print("⚠️ Invalid input. Please enter a valid number.")

def play_game():
    welcome_message()
    computerGuessed = random_number()
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        guess = player_guess()
        attempts += 1
        if guess == computerGuessed:
            guessed_correctly = True
            print("congrats! you guessed the number")
            print(f"🎉 You guessed the number in {attempts} attempts!\n")
        else:
            check_guess(computerGuessed, guess)


def check_guess(computerGuessed, guess):
    if guess > computerGuessed:
        print("Too high! try again")
    elif guess < computerGuessed:
        print("Too low! try again")

    else:
        print("congrats! you guessed the number")

def main():
    
    play_again = True
    while play_again:
       play_game()
    while True:
        response = input("Do you want to play again? (yes/no): ").strip().lower()
        if response not in ("yes", "y"):
            play_again = False
            print("Thanks for playing! Goodbye 👋") 

if __name__ == "__main__":
    main()