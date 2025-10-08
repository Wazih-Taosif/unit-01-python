import random

"""
Task 1 (random module):
Write a program that simulates rolling a six-sided die 10 times.
Print each roll result.
"""
print()
print("-------------Task1-----------")
for rolls in range(10): #iterates 10 times
    random_roll = random.randrange(1, 7) #gives a pseudo-random number between 1-6
    print(random_roll) # prints all die rolls.


"""
Task 2 (random module):
Write a program that generates 5 random floating-point numbers between 0 and 1.
Then generate 5 random floating-point numbers between 10 and 20.
Print both sets of numbers.
"""
print()
print("------------Task2----------")
print("First part: ")
for num in range(5): #iterates 5 times
    rand_float = random.random() # gives pseudo-random float number from 0 to 1.
    print(rand_float)
print()
print("second part: ")
for num in range(5):#iterates 5 times
    rand_float = random.uniform(10, 20) #gives pseudo-random float numebr between 10 and 20.
    print(rand_float)

"""
Task 3 (random module):
Create a list of colors: ["red", "blue", "green", "yellow", "purple"].
Write a program that randomly selects and prints 3 colors from this list without replacement.
"""
print()
print("---------------Task3---------------")
list_color = ["red", "blue", "green", "yellow", "purple"]
output_list = []
for colors in range(3):
    chosen_color = random.choice(list_color)
    if chosen_color in output_list:
        continue
    output_list.append(chosen_color)
print(output_list)
"""
Task 4 (random module):
Write a program that creates a list of numbers from 1 to 10, then shuffles the list
and prints the shuffled result.
"""