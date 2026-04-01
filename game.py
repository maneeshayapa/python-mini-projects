import random

number = random.randint(1,100)

guess = None
attempts = 0

print("welcome to the number guessing game!")
print("guess a number between 1 and 100")

while guess != number:
    guess = int(input("enter your guess:"))
    attempts += 1

    if guess < number:
        print("too low! try again.")
    elif guess > number:
        print("too high! try again.")
    else:
        print("congratulations! you guessed the number." )
        print(attempts, "attempts.")