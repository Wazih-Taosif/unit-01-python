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

