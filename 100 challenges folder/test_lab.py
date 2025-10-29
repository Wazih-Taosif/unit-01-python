import random

randnumber = random.randint(0,100)
guess = 0

while guess < 4:
    user_attempt = input("Guess the correct number between 0-100 : ")
    try:
        user_attempt = int(user_attempt)
    except ValueError:
        print("Please type a number! ")
        continue
    if user_attempt == randnumber:
        print("Bravo! You guessed the correct number. ")