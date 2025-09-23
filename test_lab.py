number = input("Enter a number :")
list_number = list(number)
print(list_number)
length_number = len(number)
print(length_number)

if list_number[0] == "-":
    del list_number[0]
    length_number = length_number - 1
print(list_number)    
print(length_number)