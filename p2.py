#1) Edit Distance between two strings
def editdistance(str1, str2, m, n):
    # Base cases
    if m == 0:
        return n
    if n == 0:
        return m

    # If last characters are same
    if str1[m-1] == str2[n-1]:
        return editdistance(str1, str2, m-1, n-1)

    # If last characters are different
    return 1 + min(
        editdistance(str1, str2, m, n-1),     # Insert
        editdistance(str1, str2, m-1, n),     # Remove
        editdistance(str1, str2, m-1, n-1)    # Replace
    )

# Input
str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")

# Output
print("Edit Distance is:", editdistance(str1, str2, len(str1), len(str2)))

#2) Weighted Edit Distance (Levenshtein Distance)
Code:
import numpy as np

def levenshtein(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1

    # Create matrix
    matrix = np.zeros((size_x, size_y))

    # Initialize first row and column
    for x in range(size_x):
        matrix[x][0] = x
    for y in range(size_y):
        matrix[0][y] = y

    # Fill matrix
    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]:
                cost = 0
            else:
                cost = 1

            matrix[x][y] = min(
                matrix[x-1][y] + 1,      # Deletion
                matrix[x][y-1] + 1,      # Insertion
                matrix[x-1][y-1] + cost  # Substitution
            )

    print("Matrix:\n", matrix)
    return int(matrix[size_x-1][size_y-1])

# Input
str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")


# 3) Word-Level Edit Distance (Sentence Level)
Code:
def editdistance(words1, words2, m, n):
    # Base cases
    if m == 0:
        return n
    if n == 0:
        return m

    # If last words match
    if words1[m-1] == words2[n-1]:
        return editdistance(words1, words2, m-1, n-1)

    # Insert, Delete, Substitute
    return 1 + min(
        editdistance(words1, words2, m, n-1),     # Insert
        editdistance(words1, words2, m-1, n),     # Delete
        editdistance(words1, words2, m-1, n-1)    # Substitute
    )

# Input
str1 = input("Enter Sentence 1: ")
str2 = input("Enter Sentence 2: ")
