
with open("to_do_list.txt", "r") as file:
    to_do_list = file.readlines()
    
while True:
    count = 0 # resets the list counter to 0. so that every #number of the todo's starts from 1.
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print(f"You have {len(to_do_list)} to-do's: ")
    print()
    for x in to_do_list:
        count += 1 #The counter increments by 1 till the total number of items in the list
        print(f"{count})", end=" ") #types the number count beside the todo's
        print(x) #prints all the todo's
    print()
    add_remove_edit_clear = input("Do you want to 'add'/'remove'/'edit' a to-do/ 'clear' all/ 'exit' the app ?" ).lower().strip() #user choose to add/remove/clear/edit/exit the app.
    if add_remove_edit_clear == "add":
        adding_todo = input("What is your new to-do? ").strip()
        to_do_list.append(adding_todo) #appends the new todo
    elif add_remove_edit_clear == "remove":
        removing_todo = int(input("Which # to-do would you like to remove: ")) # user choosing which todo number to remove
        del to_do_list[removing_todo - 1] #removes that specific todo in the index
    elif add_remove_edit_clear == "edit":
        editing_todo_index = int(input("Which # would you like to edit: ")) # user choosing which todo number they want to edit
        edited_newTodo = input("Whats your edited to do: ")
        to_do_list[editing_todo_index - 1] = edited_newTodo #replaces the existing todo with the new todo, at the same index
    elif add_remove_edit_clear == "clear":
        to_do_list = [] #list is cleared.
    elif add_remove_edit_clear == "exit":
        with open("to_do_list.txt", "w") as file:
            file.write("\n".join(to_do_list)) #writes the new updated list to the text file
        break

