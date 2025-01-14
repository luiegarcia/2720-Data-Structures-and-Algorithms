# Luis Garcia
# CSC 2720 Homework One
# Lab Time: Friday, 1:00 - 1:50 
# Due Time: Feb 20, 2024

def reverse_list(nums):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        # Swap elements at left and right indices
        nums[left], nums[right] = nums[right], nums[left]
        # Move the left pointer to the right
        left += 1
        # Move the right pointer to the left
        right -= 1
    
    return nums

# Example usage
input_list = [3, 4, 7, 6, 1]
reversed_list = reverse_list(input_list[:])  # Create a copy of the list to avoid modifying the original
print(reversed_list)