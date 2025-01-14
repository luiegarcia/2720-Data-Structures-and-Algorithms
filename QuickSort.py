# Luis Garcia
# CSC 2720 Lab 6
# Lab Time: Friday, 1:00 - 1:50 
# Due Time: Feb 18, 2024

# Recursive function that implements the Quick Sort algorithm
def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

# Partitions the array by selecting the pivot element
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def deduplicate_and_sort(arr):
    # Sort the input list using Quick Sort
    quicksort(arr, 0, len(arr) - 1)

    # Deduplicate the sorted list
    i = 0
    while i < len(arr) - 1:
        if arr[i] == arr[i + 1]:
            arr.pop(i)
        else:
            i += 1

    return arr

# Input list
LST = [50, 11, 33, 21, 40, 50, 40, 40, 21]

# Deduplicate and sort the input list
result = deduplicate_and_sort(LST)

# Print the deduplicated and sorted list
print(result)  # Output: [11, 21, 33, 40, 50]