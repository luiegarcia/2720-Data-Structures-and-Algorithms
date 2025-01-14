# Luis Garcia
# CSC 2720 Lab 4
# Lab Time: Friday, 1:00 - 1:50 
# Due Time: Feb 4, 2024

def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

if __name__ == "__main__":
    # Test the program with the given input array
    input_array = [50, 11, 33, 21, 40, 50, 40, 40, 21]

    print("Original Array:", input_array)

    selection_sort(input_array)

    print("Sorted Array:", input_array)