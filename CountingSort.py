# Luis Garcia
# CSC 2720 Lab 3
# Lab Time: Friday, 1:00 - 1:50 
# Due Time: Jan 28, 2024
def counting_sort(lst):
    """
    Implement Counting Sort algorithm.
    :param lst: Input list to be sorted
    """
    max_value = max(lst)
    min_value = min(lst)
    range_of_elements = max_value - min_value + 1

    count = [0] * range_of_elements
    output = [0] * len(lst)

    for i in range(len(lst)):
        count[lst[i] - min_value] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    i = len(lst) - 1
    while i >= 0:
        output[count[lst[i] - min_value] - 1] = lst[i]
        count[lst[i] - min_value] -= 1
        i -= 1

    for i in range(len(lst)):
        lst[i] = output[i]

# Sample usage and testing
if __name__ == "__main__":
    # Input list
    input_list = [50, 11, 33, 21, 40, 50, 40, 40, 21]

    # Displaying original list
    print("Original List:", input_list)

    # Sorting using Counting Sort
    counting_sort(input_list)

    # Displaying sorted list
    print("Sorted List:", input_list)