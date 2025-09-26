"""
Challenges number 1
Write a Python program that takes a string and counts how many vowels
"""

text = input("Write something :").lower()
n = 0
for x in text:
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        n += 1
print(f"The number of vowels the sentence has is: {n}")