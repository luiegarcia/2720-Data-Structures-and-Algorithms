# Luis Garcia
# CSC 2720 Homework Three
# Lab Time: Friday, 1:00 - 1:50 
# Due Time: Mar 21, 2024

def hasBalancedParentheses(s: str) -> bool:
    stack = []  # Stack to keep track of opening parentheses
    mapping = {')': '(', ']': '[', '}': '{'}  # Mapping of closing to opening parentheses
    for char in s:
        if char in mapping:  # If char is a closing parenthesis
            if not stack or stack.pop() != mapping[char]:  # If stack is empty or does not match the top of the stack
                return False  # Unbalanced parentheses
        else:
            stack.append(char)  # Push opening parenthesis onto the stack
    return not stack  # Return True if stack is empty, False otherwise


# Test cases
test_cases = [
    "()",       # True
    "([]{})",   # True
    "([{}])()", # True
    "(",        # False
    "([)",      # False
    "()(()]){)",# False
    ""          # True (empty string has balanced parentheses)
]

for test_case in test_cases:
    print(f"{test_case}: {hasBalancedParentheses(test_case)}")

# Time complexity: O(n)
# Space complexity: O(n)