# Luis Garcia
# CSC 2720 Homework Three
# Lab Time: Friday, 1:00 - 1:50 
# Due Time: Mar 21, 2024

def evaluatePostfix(tokens):
    stack = []  # Stack to hold operands
    operators = set(['+', '-', '*', '/'])  # Set of supported operators
    for token in tokens:
        if token not in operators:  # If token is operand
            stack.append(int(token))  # Push operand onto stack
        else:
            operand2 = stack.pop()  # Pop the top two operands
            operand1 = stack.pop()
            if token == '+':
                stack.append(operand1 + operand2)  # Perform addition
            elif token == '-':
                stack.append(operand1 - operand2)  # Perform subtraction
            elif token == '*':
                stack.append(operand1 * operand2)  # Perform multiplication
            elif token == '/':
                stack.append(int(operand1 / operand2))  # Perform integer division for simplicity
    return stack.pop()  # Return the final result


# Test cases
test_cases = [
    ["10", "2", "*", "15", "+"],  # Output: 35
    ["2", "1", "+", "3", "*"],     # Output: 9
    ["4", "13", "5", "/", "+"],    # Output: 6
]

for tokens in test_cases:
    result = evaluatePostfix(tokens)
    print(f"Evaluation of {tokens}: {result}")

# Time complexity: O(n)
# Space complexity: O(n)