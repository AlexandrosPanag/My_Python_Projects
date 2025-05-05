#By Alexandros Panagiotakopoulos - alexandrospanag.github.io

import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = []
    right = []
    equal = []
    for element in arr:
        if element < pivot:
            left.append(element)
        elif element > pivot:
            right.append(element)
        else:
            equal.append(element)
    return quicksort(left) + equal + quicksort(right)

# Example usage
arr = [random.randint(0, 100) for _ in range(10)]
print("Unsorted array:", arr)
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)
