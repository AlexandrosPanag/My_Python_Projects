mylist = [] #creating a null list
for i in range(1,30): #from the numbers 1-30
    if i%2==0 and i %3 == 0:
        mylist.append(i)

print(mylist)  #print the numbers from [1 to 30] that can be multiplied by 2 and 3 at the same time