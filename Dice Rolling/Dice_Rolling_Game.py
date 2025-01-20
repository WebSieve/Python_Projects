import random

while True:
 User_Choice = input("roll the dice (y/n) :").lower()
 if User_Choice == "y":
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    print(f'({die1},{die2})')

 elif User_Choice == "n":
     print("Thanks for Playing")
     break
 else:
     print("Invalid Choice !!")