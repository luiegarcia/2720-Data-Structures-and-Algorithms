# Luis Garcia
# CSC 2720 Lab 3
# Lab Time: Friday, 1:00 - 1:50 
# Due Time: Jan 28, 2024
def bubble_sort(lst):
    """
    Implement Bubble Sort algorithm.
    :param lst: Input list to be sorted
    """
    n = len(lst)

    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

# Sample usage and testing
if __name__ == "__main__":
    # Input list
    input_list = [50, 11, 33, 21, 40, 50, 40, 40, 21]

    # Displaying original list
    print("Original List:", input_list)

    # Sorting using Bubble Sort
    bubble_sort(input_list)

    # Displaying sorted list
    print("Sorted List:", input_list)