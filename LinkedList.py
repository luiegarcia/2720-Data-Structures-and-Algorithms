# Luis Garcia
# CSC 2720 Lab 7
# Lab Time: Friday, 1:00 - 1:50 
# Due Time: Feb 23, 2024

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, value):
        if not self.head:
            self.head = ListNode(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(value)

    def delete_nth_from_end(self, n):
        if not self.head:
            return
        
        dummy = ListNode(0)
        dummy.next = self.head
        first = dummy
        second = dummy
        
        # Move second pointer to the n+1th node from the beginning
        for _ in range(n + 1):
            second = second.next
        
        # Move both pointers till second reaches the end
        while second.next:
            first = first.next
            second = second.next
        
        # Delete the nth node from the end
        first.next = first.next.next
        
        # Update head if the first pointer didn't move (i.e., deleted the head)
        self.head = dummy.next

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end="")
            if current.next:
                print(", ", end="")
            current = current.next
        print()


# Create a linked list
my_linked_list = LinkedList()
values = [50, 11, 33, 21, 40, 71]
for value in values:
    my_linked_list.add_node(value)

print("Original linked list:")
my_linked_list.print_list()

# Delete the second last element
my_linked_list.delete_nth_from_end(2)

print("Linked list after deleting the second last element:")
my_linked_list.print_list()