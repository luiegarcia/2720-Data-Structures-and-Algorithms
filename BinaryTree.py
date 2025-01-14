# Luis Garcia
# CSC 2720 Lab 10
# Lab Time: Friday, 1:00 - 1:50 
# Due Time: Mar 24, 2024

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def preorderTraversal(root):
    """
    Perform pre-order traversal on the binary tree.
    
    Args:
    - root: The root node of the binary tree
    
    Returns:
    - List containing the values of nodes visited in pre-order
    """
    result = []
    if root:
        result.append(root.val)  # Visit root node
        result.extend(preorderTraversal(root.left))  # Traverse left subtree
        result.extend(preorderTraversal(root.right))  # Traverse right subtree
    return result

def inorderTraversal(root):
    """
    Perform in-order traversal on the binary tree.
    
    Args:
    - root: The root node of the binary tree
    
    Returns:
    - List containing the values of nodes visited in in-order
    """
    result = []
    if root:
        result.extend(inorderTraversal(root.left))  # Traverse left subtree
        result.append(root.val)  # Visit root node
        result.extend(inorderTraversal(root.right))  # Traverse right subtree
    return result

def postorderTraversal(root):
    """
    Perform post-order traversal on the binary tree.
    
    Args:
    - root: The root node of the binary tree
    
    Returns:
    - List containing the values of nodes visited in post-order
    """
    result = []
    if root:
        result.extend(postorderTraversal(root.left))  # Traverse left subtree
        result.extend(postorderTraversal(root.right))  # Traverse right subtree
        result.append(root.val)  # Visit root node
    return result

# Test cases
def test_traversals():
    # Create a binary tree
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)

    # Test pre-order traversal
    pre_order_result = preorderTraversal(root)
    print("Pre-order traversal:", pre_order_result)

    # Test in-order traversal
    in_order_result = inorderTraversal(root)
    print("In-order traversal:", in_order_result)

    # Test post-order traversal
    post_order_result = postorderTraversal(root)
    print("Post-order traversal:", post_order_result)

test_traversals()