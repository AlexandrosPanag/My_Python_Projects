# By Alexandros Panagiotakopoulos - alexandrospanag.github.io


#for the O(log(n)) - the best example is binary search)
def binary_search(lst, x):
    low = 0
    high = len(lst) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # If x is greater, ignore the left half
        if lst[mid] < x:
            low = mid + 1

        # If x is smaller, ignore the right half
        elif lst[mid] > x:
            high = mid - 1

        # means x is present in mid
        else:
            return mid
        
    else:
        # Else if the element was not found return -1
            return -1


# Test list
lst = [ 2, 3, 4, 10, 40 ]
x = 10 #input your element to be searched

# Function call
result = binary_search(lst, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in list")
