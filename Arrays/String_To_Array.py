mystring = "This is a string type message" #creating a string type message

mylist = [] #creating a list

for i in mystring: #for i in mystring
    if i.isalpha(): #escaping the null characters
     mylist.append(i) #add to my list the letter

print(mylist)