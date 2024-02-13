# Salmaan Rauf
# 2-08-2024
# Creating all the actions that allow the user to modify and view the list

def print_list(contactlist, /):
    """ This function formats and prints out the index, first name, and last name of each contact"""

    # Need to print out the labels for index, first name, last name based off the example spacing
    print("================== CONTACT LIST ==================")
    print(f'{"Index":7}{"First name":20}{" Last name":22}')
    print("====== ==================== ====================")

    #iterate through the whole length of the contact list and print the corresponding values
    for i in range (len(contactlist)):
        # Given for formatting convention
        print(f'{str(i):8}{contactlist[i][0]:22}{contactlist[i][1]:22}')
        #        |Index    | index 0 of contact  | index 1 of contactlist 
                        #    list is first name    is last name




def add_contact(contactlist, /, *, first_name, last_name):
    """This function will allow users to add a new contact to the contact list"""

    new_contact =[first_name, last_name]

    contactlist.append(new_contact)

    return contactlist




def modify_contact(contactlist, /, *, mod_first_name, mod_last_name, index_number):
    """The purpose of this function is to modify a contact based off the index. This could be used for misspellings etc..."""

    if 0 <= index_number < len(contactlist):
    

        contactlist[index_number][0]= mod_first_name
        contactlist[index_number][1]= mod_last_name
        return True
#contactlist[index_number] = [mod_first_name, mod_last_name]
    else:
        return False




    # #must reassign to int because it comes standard as a string
    # if 0 <= index_number < len(contactlist):
        

    #     contactlist[index_number][0]= mod_first_name
    #     contactlist[index_number][1]= mod_last_name
    #     return True
    # #contactlist[index_number] = [mod_first_name, mod_last_name]
    # else:
    #     return False

def delete_contact(contactlist, /, *, index_delete):
    """This function deletes existing contacts"""



    if 0 <= index_delete < len(contactlist):
        del contactlist[index_delete]
        return True
    else:
        return False
        # return updated list



def sort_contacts(contactlist, /, *, column):

    contactlist = sorted(contactlist, key=lambda i: i[column])
    return contactlist
