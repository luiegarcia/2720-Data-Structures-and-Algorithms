# Luis Garcia
# CSC 2720 Homework Four
# Lab Time: Friday, 1:00 - 1:50 
# Due Time: Apr 9, 2024

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def in_order_traversal(root, result):
    """
    Perform in-order traversal of the BST.
    """
    if root:
        in_order_traversal(root.left, result)
        result.append(root.val)
        in_order_traversal(root.right, result)

def delete_root(root):
    """
    Delete the root node value of the BST and replace it with the appropriate value of the existing BST.
    """
    # If the root has only one child or no child, simply delete the root
    if not root.left:
        return root.right
    elif not root.right:
        return root.left
    
    # If the root has both left and right children, find the inorder successor
    successor = root.right
    while successor.left:
        successor = successor.left
    
    # Replace the root value with the inorder successor
    root.val = successor.val
    
    # Delete the inorder successor
    root.right = delete_node(root.right, successor.val)
    
    return root

def delete_node(root, key):
    """
    Delete a node with a given key from the BST.
    """
    if not root:
        return root
    
    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        # Node to be deleted is found
        
        # Node with only one child or no child
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        
        # Node with two children: Get the inorder successor
        successor = root.right
        while successor.left:
            successor = successor.left
        
        # Copy the inorder successor's content to this node
        root.val = successor.val
        
        # Delete the inorder successor
        root.right = delete_node(root.right, successor.val)
    
    return root

# Test cases:
# Case 1: Deleting root with no children
# Expected BST after deletion: 2 -> 1
root = TreeNode(2)
root.left = TreeNode(1)
root = delete_root(root)
result = []
in_order_traversal(root, result)
print(result)  # Expected output: [1]

# Case 2: Deleting root with one right child
# Expected BST after deletion: 6 -> 5 -> 7
root = TreeNode(6)
root.right = TreeNode(7)
root.left = TreeNode(5)
root = delete_root(root)
result = []
in_order_traversal(root, result)
print(result)  # Expected output: [5, 7]

# Case 3: Deleting root with two children
# Expected BST after deletion: 6 -> 5 -> 7 -> 8
root = TreeNode(6)
root.right = TreeNode(7)
root.left = TreeNode(5)
root.right.right = TreeNode(8)
root = delete_root(root)
result = []
in_order_traversal(root, result)
print(result)  # Expected output: [5, 6, 7, 8]