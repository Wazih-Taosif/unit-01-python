user_string = input("Type a sentence: ")

user_list = list(user_string.split(" "))

user_dictionary = {}

x = 0

for items in user_list:
    user_dictionary[items] = x

print(user_dictionary)
