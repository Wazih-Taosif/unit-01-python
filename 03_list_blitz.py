"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
print()
print('------task1-----')
list1 = ["Wazih", 18, "hello", True] #this is the list
print(list1)
print()
"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""
print()
print('------task2------')
#Using the previous list and adding an element
list1.append(False)
print(list1)

"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
print()
print('-------task3--------')
#same list, and removing the last element.
del list1[4]
print(list1)
"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""
print()
print('---------task4------')
#same list, modified the first element.
list1[0] = "Taosif"
print(list1)
"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
print()
print('--------task5------')
#same list, appending 3 more elements
list1.append(1)
list1.append(2)
list1.append(3)
print(list1)

"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
print()
print('--------task6-------')
#deleting index 2 from the same list
del list1[2]
print(list1)

"""
Task 7: Slicing lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""
print()
print('-----task7-----')
list2 = list1[0:2]#first 2 elements from list1.
print(list2)

"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""
print()
print('------task8-------')
#extending list1 with list2
final_list = list1 + list2 
print(final_list)
