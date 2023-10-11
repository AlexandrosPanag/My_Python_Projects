#By Alexandros Panagiotakopoulos - alexandrospanag.github.io

import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Generate a random list of 10 integers between 1 and 100
arr = [random.randint(1, 100) for _ in range(10)]

print("Original List:", arr)
bubble_sort(arr)
print("Sorted List:", arr)
