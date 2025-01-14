# Luis Garcia
# CSC 2720 Homework Five
# Lab Time: Friday, 1:00 - 1:50 
# Due Time: Apr 23, 2024

def is_binary_search_tree(tree):
    """
    Function to check if the given binary tree is a binary search tree.

    Args:
    - tree: List representing the binary tree

    Returns:
    - True if the tree is a binary search tree, False otherwise
    """

    # Define a helper function to recursively check if a subtree is a binary search tree
    def is_bst_helper(index, min_val, max_val):
        # Base case: If index exceeds the tree size, return True
        if index >= len(tree):
            return True
        
        # Check if the current node's value is within the valid range
        if tree[index] <= min_val or tree[index] >= max_val:
            return False
        
        # Recursively check the left and right subtrees
        # Left child's value should be less than current node's value
        # Right child's value should be greater than current node's value
        return (is_bst_helper(2*index + 1, min_val, tree[index]) and
                is_bst_helper(2*index + 2, tree[index], max_val))
    
    # Start the recursion from the root (index 0) with minimum and maximum possible values
    return is_bst_helper(0, float('-inf'), float('inf'))

# Test cases:
# Test case 1: Balanced binary search tree
# Output should be True
print(is_binary_search_tree([10,5,15,2,7,11,25,1]))

# Test case 2: Unbalanced binary search tree
# Output should be False
print(is_binary_search_tree([2,4,5]))

# Test case 3: Empty tree
# Output should be True since there are no nodes to violate the BST property
print(is_binary_search_tree([]))