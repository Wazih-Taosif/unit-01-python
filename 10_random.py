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
for colors in range(1000): #range 1000 just guarantees the loop to run as many times as we need, so that we can get 3 chosen colors which are all unique.
    chosen_color = random.choice(list_color) #chooses a random color from the list
    if chosen_color in output_list: #if chosen color is already chosen previously, it won't be picked again, by using 'continue' on the next line.
        continue
    output_list.append(chosen_color)#adding the chosen color to the output list.
    if len(output_list) == 3:#We need only 3 colors....Breaks the loop after we get 3 colors in the list.
        break
print(output_list)
"""
Task 4 (random module):
Write a program that creates a list of numbers from 1 to 10, then shuffles the list
and prints the shuffled result.
"""
print()
print("-----------------Task4----------------")

original_list = []
shuffled_list = []
for num in range(1, 11):
    original_list.append(num) #just prints number 1 to 10 in the original list

print(f"The original list is: {original_list}")

for x in range(1000): #iterates enough time to get unique 10 numbers.
    chosen_number = random.choice(original_list)
    if chosen_number in shuffled_list:
        continue #does not let already chosen number to get reprinted
    shuffled_list.append(chosen_number)
    if len(shuffled_list) == 10:#only allows 10 items in the new shuffled list.
        break
print(f"The shuffled list is: {shuffled_list}")