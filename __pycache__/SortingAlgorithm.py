# Luis Garcia
# CSC 2720 Homework Five
# Lab Time: Friday, 1:00 - 1:50 
# Due Time: Apr 23, 2024

def top_k_frequent_sort(nums, k):
    """
    Function to find the top k frequent elements in the input array using sorting.

    Args:
    - nums: Input list of integers
    - k: Number of top frequent elements to return

    Returns:
    - List of top k frequent elements
    """

    # Count the frequency of each element using a dictionary
    freq_map = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1
    
    # Sort the elements based on their frequency in descending order
    sorted_nums = sorted(freq_map, key=lambda x: freq_map[x], reverse=True)
    
    # Return the top k frequent elements
    return sorted_nums[:k]

# Test cases:
# Test case 1: Input array has multiple elements with different frequencies
# Output should be [1, 2] since 1 and 2 both occur twice, and k=2
print(top_k_frequent_sort([1,2,1,3,2,2], 2))

# Test case 2: Input array has only one element
# Output should be [1] since there's only one element in the array and k=1
print(top_k_frequent_sort([1], 1))

# Test case 3: Input array is empty
# Output should be an empty list since there are no elements in the array
print(top_k_frequent_sort([], 2))