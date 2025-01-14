# Luis Garcia
# CSC 2720 Homework One
# Lab Time: Friday, 1:00 - 1:50 
# Due Time: Feb 6, 2024

def binary_search(lst, target):
    """
    Binary search algorithm to find if target exists in the sorted list lst.
    Returns True if found, False otherwise.
    """
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if lst[mid] == target:
            return True
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

def intersection_binary_search(lst1, lst2):
    """
    Finds the intersection of two sorted lists using binary search.
    Returns a list containing common elements without duplicates.
    """
    intersection = []
    # Choose the smaller list for binary search
    smaller_list = lst1 if len(lst1) < len(lst2) else lst2
    larger_list = lst2 if smaller_list is lst1 else lst1

    # Sort the larger list
    larger_list.sort()

    # Loop through elements of smaller list and perform binary search on larger list
    for num in smaller_list:
        if binary_search(larger_list, num) and num not in intersection:
            intersection.append(num)
    return intersection

# Provided lists
LST1 = [1, 5, 6, 6, 9, 9, 9, 11, 11, 21]
LST2 = [6, 6, 9, 11, 21, 21, 21]

# Function call and output
print(intersection_binary_search(LST1, LST2))

"""
    Finds the intersection of two sorted lists using binary search.
    Returns a list containing common elements without duplicates.

    Suggested improvement:
    Since both lists are sorted, we can utilize two pointers approach to traverse both lists simultaneously.
    Initialize two pointers, one for each list, and compare the elements at these pointers.
    If the elements are equal, add it to the intersection list and move both pointers.
    If the element in the first list is smaller, move the first list's pointer.
    If the element in the second list is smaller, move the second list's pointer.
    This approach allows linear traversal of both lists and results in O(m + n) time complexity.
    """