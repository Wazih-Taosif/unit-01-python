"""
Try to make the wordle game.
"""

import random



word_list = [
    "apple", "grape", "flame", "chair", "stone", "water", "cloud", "tiger", "lions", "zebra",
    "shine", "blink", "glove", "table", "piano", "brick", "mango", "pearl", "quick", "vocal",
    "sword", "dream", "tease", "flash", "purse", "drink", "whale", "heist", "flick", "smile",
    "judge", "guitar", "dance", "plane", "sword", "sleep", "cross", "haste", "night", "grass",
    "storm", "piano", "crawl", "sneak", "brisk", "peace", "grove", "fetch", "blaze", "lunar"
]


random_word = random.choice(word_list)
print(random_word)

guess = 0
attempt = 0

while guess != random_word:
    if guess == random_word:
        print(f"You got it!!")
        break
    guess = input("Guess the wordle: ")
    for char in guess:
        if char in random_word:
            print(f"{char} is in the wordle.")
    attempt += 1



