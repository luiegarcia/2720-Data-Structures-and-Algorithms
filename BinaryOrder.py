# Luis Garcia
# CSC 2720 Lab 11
# Lab Time: Friday, 1:00 - 1:50 
# Due Time: Mar 31, 2024

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def level_order_traversal(root):
    """
    Perform level order traversal of a binary tree.
    
    Args:
    root (TreeNode): The root node of the binary tree.
    
    Returns:
    list: A list containing the values of the nodes in level order traversal.
    """
    # Check if the root is None
    if not root:
        return []
    
    # Initialize a queue for level order traversal
    queue = deque([root])
    result = []
    
    # Perform level order traversal
    while queue:
        # Get the current node
        node = queue.popleft()
        result.append(node.val)
        
        # Add left and right children to the queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

# Test cases:
# Create a binary tree
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

# Test the function with the given binary tree
print(level_order_traversal(root))

# Additional test cases
# Test case 1: root is None
# Expected output: []
print(level_order_traversal(None))

# Test case 2: root has only one node
# Expected output: [4]
print(level_order_traversal(TreeNode(4)))

# Test case 3: Binary tree with only left children
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)
# Expected output: [1, 2, 3, 4]
print(level_order_traversal(root))

# Test case 4: Binary tree with only right children
root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)
# Expected output: [1, 2, 3, 4]
print(level_order_traversal(root))