# By Alexandros Panagiotakopoulos - alexandrospanag.github.io

def unique_elements(mylist):
    #check if the list is valid
    if not type(mylist) is list:
        return []
    mylist_new=[]
    for i in mylist:
        if i not in mylist_new: mylist_new.append(i)
    return mylist_new

print(unique_elements([1,2,3,4,2,3,4,2,3,4]))
