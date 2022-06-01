#creating a basic dictionary
contact = {"James":111333, "Smith":222444}


#creating a new contact
print("Give a new contact: ")
name = input("Give a name:")
tel = input("Give a phone contact number:")
contact[name] = int(tel)
print("Your contacts are:\n",contact)

#sorting the contacts in alphabetical order
contact_sorted=list(contact.items()) #transfering the contacts into a new dictionary
contact_sorted.sort() #sorting the contact list
print("The contact list has been sorted:\n",contact_sorted)
