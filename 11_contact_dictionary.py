#Create a program to manage a simple contact book. The book should store each contact's name and phone number and allow users to add, delete, and list contacts.

contacts_book = {}#dictionary that will store all contacts name and number

while True:
    print()
    print("------------------------------------------------------------------------")
    print("""Contact Book Menu: 
          1. Add contact
          2. Delete contact
          3. Edit contact
          4. List contacts
          5. Exit contact book""")
    choice = input("Enter your choice: ")
    #adding contacts
    if choice == "1":
        contact_name = input("Enter your contact's name: ").lower().strip()
        contact_number = input("Enter your contact's number: ").strip()
        while len(contact_number) != 10: #checks if the contact is only 10 digits or not
            print("Phone number needs to have 10 digits! Please retype")
            contact_number = input("Enter your contact's number: ").strip()
        while True:
            if contact_number.isdigit(): #checking to see if the inputed number is only integers or not
                number = int(contact_number)
                break
            else:
                print("Contact numbers can't have letters! Please retype")
                contact_number = input("Enter your contact's number: ").strip()

        contacts_book[contact_name] = contact_number
        print("Contact added successfully")
    #deleting contacts
    elif choice == "2":
        contact_name = input("Enter the contact you want to delete: ").lower().strip()
        if contact_name in contacts_book:#if contact is inside the dictionary, it will get deleted
            del contacts_book[contact_name]
            print("Contacts deleted successfully.")
        else:
            print("Contact does not exist in the contact book.")
    #editing contacts
    elif choice == "3":
        editing_name = input("Enter the contact to edit: ").lower().strip()
        if editing_name in contacts_book:#contact will only get edited if it is in the dictionary
            edited_number = input("Enter updated contact number: ")
            while len(edited_number) != 10:#making sure new contact number has 10 digits
                print("Phone number needs to have 10 digits! Please retype")
                edited_number = input("Enter your contact's number: ").strip()
            while True:
                if edited_number.isdigit():#making sure the user inputed only numbers and not letters
                    number = int(edited_number)
                    break
                else:
                    print("Contact numbers can't have letters! Please retype")
                    edited_number = input("Enter your contact's number: ").strip()
            contacts_book[editing_name] = edited_number
            print("Contact edited successfully")
        else:
            print("Contact does not exist in the contacts book.")
    #listing contacts
    elif choice == "4":
        print()
        print("Your current contacts are: ")
        for contactName in contacts_book:
            print(f"{contactName} : {contacts_book[contactName]}") #using for loop to format the print in a nicer way
    #exiting the while loop
    elif choice == "5":
        break


