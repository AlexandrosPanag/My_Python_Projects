# By Alexandros Panagiotakopoulos - alexandrospanag.github.io

#BubbleSort searching algorithm is a good example of O(n^2) Algorithm Searching Complexity
def bubbleSort(my_list):
    n = len(my_list)
    
    # Traverse through all list elements
    for i in range(n):
    
        # Last i elements are already in place
        for j in range(0, n-i-1):
    
            # traverse the list from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if my_list[j] > my_list[j+1] :
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

# Driver code to test above
my_list = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(my_list) #call the function

#output the sorted list
print("Sorted array is:") 
for i in range(len(my_list)):
    print("% d" % my_list[i], end=" ")
