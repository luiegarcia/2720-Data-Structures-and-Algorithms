# Luis Garcia
# CSC 2720 Lab 4
# Lab Time: Friday, 1:00 - 1:50 
# Due Time: Feb 4, 2024

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
    while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
    arr[j + 1] = key

if __name__ == "__main__":

    # Test the program with the given input array
    input_array = [50, 11, 33, 21, 40, 50, 40, 40, 21]

    print("Original Array:", input_array)

    insertion_sort(input_array)

    print("Sorted Array:", input_array)