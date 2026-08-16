#NUMBER GUESSING GAME
import random
lowest=1
highest=100
answer=random.randint(lowest, highest)

guesses=0
is_running=True

print("Welcome to Python Number Guessing Game")
print(f"Select a number between {lowest} and {highest}")

while is_running:
    guess=input("Enter your guess")
    if guess.isdigit:
        guess=int(guess)
        guesses+=1

        if guess<lowest or guess>highest:
           print("INVALID INPUT")
           print(f"Select a number between {lowest} and {highest}")
        elif guess<answer:
           print("Too low try again")
        elif guess>answer:
           print("Too high guess again")
        else:
            print(f"CORRECT ANSWER!!! The answer was {answer}")
            print(f"No.of guesses was: {guesses}")
    else:
        print("INVALID INPUT")
        print(f"Select a number between {lowest} and {highest}")