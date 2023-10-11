#By Alexandros Panagiotakopoulos - alexandrospanag.github.io
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Generate a list of 10 random integers between 1 and 100
arr = [random.randint(1, 100) for _ in range(10)]

print("Unsorted list:", arr)
insertion_sort(arr)
print("Sorted list:", arr)
