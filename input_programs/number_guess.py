import random

secret = random.randint(1, 10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == secret:
        print("Correct! 🎉")
        break
    else:
        print("Wrong! Try again.")
