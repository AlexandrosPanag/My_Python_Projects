# By Alexandros Panagiotakopoulos - alexandrospanag.github.io


#Define the linear search function
def search(my_list, x):
    
    for i in range(len(my_list)):
 
        if my_list[i] == x:
            return i
 
    return -1

#Creating a list full of elements
my_list = ["a","b","c","d","e"]

print(search(my_list, "c")) #search the position of the element
