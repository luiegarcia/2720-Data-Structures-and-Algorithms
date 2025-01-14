# Luis Garcia
# CSC 2720 Homework Three
# Lab Time: Friday, 1:00 - 1:50 
# Due Time: Mar 21, 2024

class MyLinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverseLinkedList(head):
    """
    Reverse a singly linked list.
    
    Args:
    - head: The head node of the original linked list
    
    Returns:
    - The head node of the reversed linked list
    """
    prev_node = None  # Initialize previous node as None
    curr_node = head  # Start traversal from the head node
    while curr_node is not None:
        next_node = curr_node.next  # Store the next node
        curr_node.next = prev_node  # Reverse the pointer of current node to the previous node
        prev_node = curr_node  # Move the previous node pointer forward
        curr_node = next_node  # Move the current node pointer forward
    return prev_node  # Return the new head node (which was the last node)


def printLinkedList(head):
    """
    Print the linked list from the given head node.
    """
    temp = head
    while temp:
        print(temp.val, end=" ")  # Print the value of each node
        temp = temp.next
    print()


# Test case
def test_reverseLinkedList():
    # Create a linked list
    head = MyLinkedListNode(5)
    head.next = MyLinkedListNode(7)
    head.next.next = MyLinkedListNode(1)
    head.next.next.next = MyLinkedListNode(2)
    head.next.next.next.next = MyLinkedListNode(3)

    print("Original List:")
    printLinkedList(head)

    reversed_head = reverseLinkedList(head)

    print("Reversed List:")
    printLinkedList(reversed_head)

    # Expected output: 3 2 1 7 5


test_reverseLinkedList()

# Time complexity: O(n)
# Space complexity: O(1)