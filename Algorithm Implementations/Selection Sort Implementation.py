#By Alexandros Panagiotakopoulos - alexandrospanag.github.io
import random

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [random.randint(0, 100) for _ in range(10)]
print("Unsorted array:", arr)
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
