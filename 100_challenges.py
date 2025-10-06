"""
Challenge number 1
Write a Python program that takes a string and counts how many vowels
"""

text = input("Write something :").lower()
n = 0
for x in text:
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        n += 1
print(f"The number of vowels the sentence has is: {n}")
print()

"""
challenge number 2
Write a Python function that checks whether a given word or phrase is a palindrome.

A palindrome is a word, phrase, or sequence that reads the same backward as forward, ignoring spaces, punctuation, and case.
"""
user_string = input("Enter a text: ").strip().lower() # user writes a text

corrected_String = user_string.replace(" ", "") #removing all spaces in the text
corrected_String = corrected_String.replace(",", "") #removing commas


user_list = list(corrected_String) #converting the user inputed string to a list so that we can do calculations



n = len(user_list) #tells how many elements there are in the list

r = 0
#checking if n is even or odd
if n % 2 == 0: 
    r = n - n/2 #this will get me the middle value(median)

else:
    r = (n + 1) / 2 #this will get me the middle value(median)


p = 0 #first element in the list
q = -1 #last element in the list
#reversing the order of the items from (left to right) to (right to left)
for x in range(int(r)): #iterates exactly the median value of the total items in the list.
    item_1 = user_list[p]
    item_2 = user_list[q]
    user_list[q] = item_1
    user_list[p] = item_2
    p += 1
    q -= 1

reversed_string = "".join(user_list) #converting the updated, reversed list to a string, so that we can compare the user input with this new string.
print(f" Your text was: {corrected_String}")
print(f" Your text reversed is: {reversed_string}")

#checks if the initial written text of the user is same as the reversed string.
if corrected_String == reversed_string: 
    print("Thus the text is a palindrome") 
else:
    print("Thus the text is not a palindrome")
print()

"""
Challenge number 3
Write a program that prints the numbers from 1 to N (user input). But for multiples of:

3, print "Fizz" instead of the number.

5, print "Buzz" instead of the number.

Both 3 and 5, print "FizzBuzz".
"""
N = int(input("Type a number: "))

for i in range(1, N + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
print()
