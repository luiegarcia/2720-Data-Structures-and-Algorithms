# Luis Garcia
# CSC 2720 Lab 2
# Lab Time: Friday, 1:00 - 1:50 
# Due Time: Jan 19, 2024

from DeDuplication import *

def BinarySearch(sorted_list, target):
    checks = 0
    low, high = 0, len(sorted_list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        checks += 1
        
        if sorted_list[mid] == target:
            return True, checks
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return False, checks

# Test the program with the de-duplicated list from the previous code
de_dup_list = DeDupe([50, 11, 33, 21, 40, 50, 40, 40, 21])

# Test with different values
search_value1 = 21
search_value2 = 35
search_value3 = 50

# Perform BinarySearch on the de-duplicated list
result1, checks1 = BinarySearch(de_dup_list, search_value1)
result2, checks2 = BinarySearch(de_dup_list, search_value2)
result3, checks3 = BinarySearch(de_dup_list, search_value3)

# Print results
if result1:
    print(f"{search_value1} found! Checks: {checks1}")
else:
    print(f"Fail to find {search_value1}...")

if result2:
    print(f"{search_value2} found! Checks: {checks2}")
else:
    print(f"Fail to find {search_value2}...")

if result3:
    print(f"{search_value3} found! Checks: {checks3}")
else:
    print(f"Fail to find {search_value3}...")