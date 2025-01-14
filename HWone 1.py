# Luis Garcia
# CSC 2720 Homework One
# Lab Time: Friday, 1:00 - 1:50 
# Due Time: Feb 6, 2024

def intersection_brute_force(lst1, lst2):
    intersection = []  # Initialize an empty list to store the intersection elements
    # Loop through elements of lst1
    for num1 in lst1:
        # Loop through elements of lst2
        for num2 in lst2:
            # If there's a match and it's not already in the intersection list, add it
            if num1 == num2 and num1 not in intersection:
                intersection.append(num1)
                break  # Break to avoid duplicates
    return intersection

# Provided lists
LST1 = [1, 5, 6, 6, 9, 9, 9, 11, 11, 21]
LST2 = [6, 6, 9, 11, 21, 21, 21]

# Test cases
# Case 1: Empty lists
assert intersection_brute_force([], []) == []

# Case 2: Lists with one element
assert intersection_brute_force([1], [1]) == [1]

# Case 3: Lists with no common elements
assert intersection_brute_force([1, 2, 3], [4, 5, 6]) == []

# Case 4: Lists with some common elements
assert intersection_brute_force([1, 2, 3, 4, 5], [4, 5, 6]) == [4, 5]

# Function call and output
print("Intersection of LST1 and LST2:", intersection_brute_force(LST1, LST2))