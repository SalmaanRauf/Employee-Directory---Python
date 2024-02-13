import Contacts
# Salmaan Rauf
# 2-08-2024
# Creating menu for user interaction allowing modification and viewing of list

contact_list = []

while True:
    print("*** EMPLOYEE CONTACT MAIN MENU")
    print("1. Print list")
    print("2. Add contact")
    print("3. Modify contact")
    print("4. Delete contact")
    print("5. Sort list by first name")
    print("6. Sort list by last name")
    print("7. Exit the program")


    choice= input("Enter menu choice: ")

    if choice == '1':
        Contacts.print_list(contact_list)


    elif choice == '2':
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        contact_list = Contacts.add_contact(contact_list, first_name=first_name, last_name=last_name)


    elif choice == '3':
        try:
            index_number = int(input("Enter the index number: "))
            mod_first_name = input("Enter first name: ")
            mod_last_name = input("Enter last name: ")

            if not Contacts.modify_contact(contact_list, mod_first_name=mod_first_name, mod_last_name=mod_last_name, index_number=index_number):
                print("Invalid index number.")
        except ValueError:
            print("Invalid index number. Please enter integers only.")

    elif choice == '4':
        try:
            index_delete = int(input("Enter the index number: "))
            if not Contacts.delete_contact(contact_list, index_delete=index_delete):
                print("Invalid index number.")
        except ValueError:
            print("Inalid  index number. Please enter integers only.")
    

    elif choice == '5':
        contact_list = Contacts.sort_contacts(contact_list, column=0)
    
    elif choice == '6':
        contact_list = Contacts.sort_contacts(contact_list, column=1)

    elif choice == '7':
        break
    
    else: 
        print("Invalid menu choice.")
        

















    
    #User_Choice = input("\nEnter menu choice: ")















    # if User_Choice in menu_Options:
    #     if User_Choice == '7':
    #         menu_Options[User_Choice]()
    #     else: 

















    # elif User_Choice == '1':
    #     print_list(contact_list)
    
    # elif User_Choice == '2':
    #     contact_list = add_contact(contact_list)

    # elif User_Choice == '3':
    #     pass

    # elif User_Choice == '4':
    #     pass
    # elif User_Choice == '5':
    #     break

    # elif User_Choice == '6':
    #     pass

    # elif User_Choice == '7':
    #     break

    # if User_Choice in menu_Options:
    #     if User_Choice == '5':
    #         sys.exit()
    #     else:
    #         menu_Options[User_Choice](contact_list)
    # else:
    #     print("Invalid index number.")

