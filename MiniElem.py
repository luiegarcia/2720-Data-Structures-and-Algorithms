# Luis Garcia
# CSC 2720 Lab 9
# Lab Time: Friday, 1:00 - 1:50 
# Due Time: Mar 10, 2024

class MinStack:
    def __init__(self):
        
        # Initialize two stacks: one for storing elements and one for storing minimum values.
        
        self.stack = []      # Stack to store elements
        self.min_stack = []  # Stack to store minimum values

    def push(self, val: int) -> None:
        
        # Push the value onto the main stack.
        # Update the min_stack if the new value is smaller or equal to the current minimum.
        
        self.stack.append(val)
        # If the min_stack is empty or the new value is smaller or equal to the current minimum,
        # push the new value onto the min_stack.
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        
        # Pop the top element from the main stack.
        # If the top element of stack is equal to the top element of min_stack, pop the top element from min_stack.
        
        # If the top element of stack is equal to the top element of min_stack, pop the top element from min_stack.
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        # Pop the top element from the main stack.
        self.stack.pop()

    def top(self) -> int:
        
        # Get the top element of the main stack.
        
        return self.stack[-1]

    def getMin(self) -> int:
        
        # Retrieve the minimum element in the stack.
        
        return self.min_stack[-1]

# Test case with a random stack
# Create a MinStack object
min_stack = MinStack()

# Push elements onto the stack
min_stack.push(3)
min_stack.push(5)
min_stack.push(2)
min_stack.push(7)

# Test top and getMin
print("Top element:", min_stack.top())   # Output: 7
print("Minimum element:", min_stack.getMin())   # Output: 2

# Pop elements from the stack
min_stack.pop()
min_stack.pop()

# Test top and getMin after popping
print("Top element after popping:", min_stack.top())   # Output: 5
print("Minimum element after popping:", min_stack.getMin())   # Output: 3

# Push another element
min_stack.push(1)

# Test getMin after pushing a smaller element
print("Minimum element after pushing a smaller element:", min_stack.getMin())   # Output: 1