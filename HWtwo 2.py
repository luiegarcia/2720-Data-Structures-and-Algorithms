# Luis Garcia
# CSC 2720 Homework One
# Lab Time: Friday, 1:00 - 1:50 
# Due Time: Feb 20, 2024

def sort_flowers(n, flowers):
    # Insertion sort algorithm
    for i in range(1, len(flowers)):
        key = flowers[i]
        j = i - 1
        while j >= 0 and flowers[j] > key:
            flowers[j + 1] = flowers[j]
            j -= 1
        flowers[j + 1] = key
    
    return flowers

# Example usage
n = int(input("Enter the number of flowers: "))
flowers = input("Enter the flower names separated by spaces: ").split()

sorted_flowers = sort_flowers(n, flowers)
print(sorted_flowers)