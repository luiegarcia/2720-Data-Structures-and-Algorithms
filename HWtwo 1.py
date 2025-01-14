# Luis Garcia
# CSC 2720 Homework Two
# Lab Time: Friday, 1:00 - 1:50 
# Due Time: Feb 20, 2024

def has_duplicates_word_finder(n, words):
    # Convert the list of words into a set to remove duplicates
    unique_words = set(words)
    
    # If the length of the set is less than the length of the original list,
    # it means there were duplicates
    if len(unique_words) < len(words):
        return True
    else:
        return False

# Example usage
n = int(input("Enter the number of words: "))
words = input("Enter the words separated by spaces: ").split()

print(has_duplicates_word_finder(n, words))