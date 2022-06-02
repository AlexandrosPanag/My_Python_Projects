mylist=['Doe',26,500.99] #this command extends the list
mylist.append('m') #this command adds an element 'm' into the list
mylist.extend(['James',32,623.68,'m']) #this command extends the list by adding multiple elements
mylist.remove('m') #this command removes an 'm' but only one m if we want to remove another m element we have to reuse the command
mylist.pop(6) #this command pops out from the list the 6 element, note that lists begin from 0 not from 1,basically we remove the 2nd 'm' element
print(mylist.index('James')) #it will return the value 3 because james is the 4th element on our list
print(mylist)