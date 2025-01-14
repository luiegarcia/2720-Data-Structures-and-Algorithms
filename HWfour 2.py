# Luis Garcia
# CSC 2720 Homework Four
# Lab Time: Friday, 1:00 - 1:50 
# Due Time: Apr 9, 2024

def findRepeatedDnaSequences(s):
    """
    Given a DNA sequence represented as a string, returns all 10-letter-long sequences that occur more than once.
    """
    if len(s) <= 10:
        return []

    # Store the sequences and their counts in a dictionary
    sequences = {}
    for i in range(len(s) - 9):
        sequence = s[i:i + 10]
        sequences[sequence] = sequences.get(sequence, 0) + 1

    # Filter out the repeated sequences
    repeated_sequences = [sequence for sequence, count in sequences.items() if count > 1]
    return repeated_sequences

# Test cases:
# Case 1: Example input
s1 = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(findRepeatedDnaSequences(s1))  # Expected output: ['AAAAACCCCC', 'CCCCCAAAAA']

# Case 2: Input with no repeated sequences
s2 = "AAAAAAAAAAAAA"
print(findRepeatedDnaSequences(s2))  # Expected output: ['AAAAAAAAAA']

# Case 3: Input with no sequences
s3 = ""
print(findRepeatedDnaSequences(s3))  # Expected output: []

# Case 4: Input with only one sequence
s4 = "ACGTACGTAC"
print(findRepeatedDnaSequences(s4))  # Expected output: []

# Case 5: Input with multiple repeated sequences
s5 = "AAAAAAAAAAACCCCCCCCCCAAAAAACCCCCCCCTTTTTTTTTT"
print(findRepeatedDnaSequences(s5))  # Expected output: ['AAAAAAAAAA', 'CCCCCCCCCC', 'TTTTTTTTTT']