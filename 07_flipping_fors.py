"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
print()
print("-----task1-----")
string_1 = input("Write a string :") #user inputs a string
for char in string_1:
    print(char) #prints all the charactors in the string


"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""
print()
print("------task2-------")
list_2 = [1.5, 2, 3, 4, 5] # The requied list
sum = 0 # setting value of sum 0, because we will do addition.
for x in list_2:
    sum = x + sum # it will add all values of the elements in the list and store it in the variable sum.
print(sum)

"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""
print()
print("-------task3--------")
sentence = "Quick brown foxes are seen in minecraft" #given string
list_sentence = list(sentence.split(" ")) #converting the string to list
for x in list_sentence:
    print(len(x), end=" ") #prints the length of each word/element in the list


"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result

In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""
print()
print("---------task4-------")
#The required dictionary
dictionary = {
    "apples": 3,
    "bananas": 4,
    "guavas": 10,
    "mangos": 15,
    "papayas": 2
}
for x in dictionary:
    print(x) #prints all the keys of the dictionary.

#Not what I thought. I thought it would print the values and keys both. But it printed only the keys