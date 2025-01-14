# Luis Garcia
# CSC 2720 Lab 5
# Lab Time: Friday, 1:00 - 1:50 
# Due Time: Feb 11, 2024

def merge_sort(arr):
    """
    Sorts the input array in ascending order.
    
    Time complexity: O(n log n)
    Space complexity: O(n)
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    merge_sort(left_half)
    merge_sort(right_half)
    
    i = j = k = 0
    
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1
    
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1
    
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1
    
def deduplicate_sorted(arr):
    """
    Removes duplicates from a sorted array in-place.
    
    Time complexity: O(n)
    Space complexity: O(1)
    """
    if not arr:
        return 0
    
    write_index = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[write_index] = arr[i]
            write_index += 1
    
    return write_index

def deduplicate(arr):
    """
    Sorts the input array using merge sort and then removes duplicates.
    
    Time complexity: O(n log n) + O(n) = O(n log n)
    Space complexity: O(n) (for merge sort)
    """
    merge_sort(arr)  # Using Merge Sort
    new_length = deduplicate_sorted(arr)
    return arr[:new_length]

# Example usage:
LST = [50, 11, 33, 21, 40, 50, 40, 40, 21]
print(deduplicate(LST))  