# Luis Garcia
# CSC 2720 Lab 13
# Lab Time: Friday, 1:00 - 1:50 
# Due Time: Apr 14, 2024

import heapq

def kBiggest(lst, k):
    """
    Finds the k-biggest element in an unsorted array without using sorting algorithms,
    using a heap-based approach.
    
    Args:
    lst (list): The unsorted list.
    k (int): The kth biggest element to find.
    
    Returns:
    int: The kth biggest element.
    """
    # Create a min heap with the first k elements of the list
    heap = lst[:k]
    heapq.heapify(heap)
    
    # Iterate through the remaining elements
    for num in lst[k:]:
        # If the current element is bigger than the smallest element in the heap
        if num > heap[0]:
            # Replace the smallest element with the current element
            heapq.heappop(heap)
            heapq.heappush(heap, num)
    
    # Return the smallest element in the heap, which is the kth biggest element
    return heap[0]

# Test cases:
# Test with a simple list
print(kBiggest([3, 1, 4, 2, 5], 3))  # Should output: 3

# Test with a larger list
print(kBiggest([9, 2, 7, 1, 5, 4, 6, 3, 8], 4))  # Should output: 6

# Test with repeated elements
print(kBiggest([5, 5, 5, 5, 5], 2))  # Should output: 5

"""
Time Complexity:

- Building the initial heap from the first k elements takes O(k) time.
- Iterating through the remaining n-k elements and adjusting the heap takes O((n-k) * log(k)) time.
- Overall, the time complexity is O(k + (n-k) * log(k)), which can be simplified to O(n * log(k)).

Space Complextiy:

- The space complexity is O(k) due to the heap storing the k biggest elements.
- Additionally, there is O(1) space complexity for variables and constants.
- Therefore, the overall space complexity is O(k).
"""