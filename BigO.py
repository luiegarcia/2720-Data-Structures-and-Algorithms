# Luis Garcia
# CSC 2720 Lab 3
# Lab Time: Friday, 1:00 - 1:50 
# Due Time: Jan 28, 2024
# Big-O time analysis for Bubble Sort
"""
Bubble Sort has a time complexity of O(n^2) in the worst-case scenario, where n is the number of elements in the input list.
This is because it uses nested loops to compare and swap elements. In the best-case scenario, when the list is already sorted, the time complexity is O(n).

"""

# Big-O space analysis for Bubble Sort
"""
Bubble Sort has a space complexity of O(1) as it only requires a constant amount of extra space for variables, irrespective of the input size.

"""

# Big-O time analysis for Counting Sort
"""
Counting Sort has a time complexity of O(n + k), where n is the number of elements in the input list and k is the range of input values.
The counting phase takes O(n), and the second loop takes O(k), where k is the range of input values. Counting Sort is more efficient than Bubble Sort for large datasets.

"""

# Big-O space analysis for Counting Sort
"""
Counting Sort has a space complexity of O(k), where k is the range of input values. It requires additional space for the counting array.
In scenarios where the range of input values is small, Counting Sort is more space-efficient than Bubble Sort.

"""

# Comparison between two algorithms
"""
Bubble Sort is suitable for small datasets due to its simplicity, but its quadratic time complexity makes it less efficient for large datasets.
Counting Sort, with its linear time complexity, is more efficient for larger datasets, especially when the range of input values is not significantly large.

"""