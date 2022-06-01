#Contacts usually have the format "PrimaryKeyElement":<keyvalue>, but we cannot alter the primary key element
contacts = {"John":999999999, "Doe":888888888} #declaring a dictionairy
contacts["Doe"] = 777777777 #altering a value that belongs to Doe
print(len(contacts))
print(contacts)