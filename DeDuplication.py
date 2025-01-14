# Luis Garcia
# CSC 2720 Lab 2
# Lab Time: Friday, 1:00 - 1:50 
# Due Time: Jan 19, 2024

def DeDupe(input_list):
    # Initialize a counting list to keep track of element frequencies
    counting_list = {}
    
    # Iterate through the input list to count element frequencies
    for num in input_list:
        counting_list[num] = counting_list.get(num, 0) + 1
    
    # Create the output list with unique elements, removing duplicates
    output_list = [key for key, value in counting_list.items() if value > 0]
    
    # Sort the output list manually (without using library functions)
    for i in range(len(output_list)):
        for j in range(i + 1, len(output_list)):
            if output_list[i] > output_list[j]:
                output_list[i], output_list[j] = output_list[j], output_list[i]
    
    return output_list

# Test the program with the given testcase and additional testcases
testcase1 = [50, 11, 33, 21, 40, 50, 40, 40, 21]
testcase2 = [10, 20, 10, 30, 40, 30, 50, 60]
testcase3 = [5, 5, 5, 5, 5, 5]

result1 = DeDupe(testcase1)
result2 = DeDupe(testcase2)
result3 = DeDupe(testcase3)

print("DeDuplication Testcase 1:", result1)
print("DeDuplication Testcase 2:", result2)
print("DeDuplication Testcase 3:", result3)