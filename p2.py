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



For Viva-

# 📘 IR Practical Viva Questions (Edit Distance & String Similarity)

---

## 🔹 1. What is Edit Distance?

**Answer:**
Edit Distance is the minimum number of operations required to convert one string into another.

---

## 🔹 2. What are the basic operations in Edit Distance?

**Answer:**

* Insertion
* Deletion
* Substitution (Replacement)

---

## 🔹 3. What is Levenshtein Distance?

**Answer:**
Levenshtein Distance is a type of edit distance where all operations (insert, delete, substitute) have equal cost (usually 1).

---

## 🔹 4. What is Weighted Edit Distance?

**Answer:**
It is a variation where different operations have different costs (e.g., substitution cost may differ from insertion).

---

## 🔹 5. Why is Edit Distance important in Information Retrieval?

**Answer:**
It helps in:

* Spell checking
* Query correction
* Fuzzy search
* Matching similar words

---

## 🔹 6. What is fuzzy matching?

**Answer:**
Fuzzy matching finds approximate matches instead of exact matches, useful for handling spelling errors.

---

## 🔹 7. What is the difference between exact matching and approximate matching?

**Answer:**

* Exact matching → Words must be identical
* Approximate matching → Words can be similar

---

## 🔹 8. What is dynamic programming in Edit Distance?

**Answer:**
It is an optimization technique that stores intermediate results in a matrix to avoid recomputation.

---

## 🔹 9. What is the time complexity of Edit Distance?

**Answer:**

* Recursive → Exponential
* Dynamic Programming → O(m × n)

---

## 🔹 10. Why is recursion inefficient for Edit Distance?

**Answer:**
Because it recalculates the same subproblems multiple times.

---

## 🔹 11. What is the role of the matrix in Levenshtein Distance?

**Answer:**
It stores distances between all prefixes of two strings.

---

## 🔹 12. What does each cell in the matrix represent?

**Answer:**
The minimum edit distance between substrings of two strings.

---

## 🔹 13. What is the base condition in Edit Distance?

**Answer:**

* If one string is empty → distance = length of the other string

---

## 🔹 14. What is substitution cost?

**Answer:**
The cost of replacing one character with another.

---

## 🔹 15. What happens if two characters are equal?

**Answer:**
No operation is needed → cost = 0

---

## 🔹 16. What is Word-Level Edit Distance?

**Answer:**
It computes edit distance based on words instead of characters (used for sentences).

---

## 🔹 17. Difference between character-level and word-level edit distance?

**Answer:**

* Character-level → compares letters
* Word-level → compares words

---

## 🔹 18. Where is Word-Level Edit Distance used?

**Answer:**

* Sentence similarity
* Plagiarism detection
* NLP applications

---

## 🔹 19. What is similarity vs distance?

**Answer:**

* Distance → measure of difference
* Similarity → measure of closeness

---

## 🔹 20. How is Edit Distance used in search engines?

**Answer:**
To suggest correct spellings and improve search results.

---

## 🔹 21. What is spell correction?

**Answer:**
Automatically correcting misspelled words using similarity measures like edit distance.

---

## 🔹 22. What is auto-complete?

**Answer:**
Suggesting possible word completions based on user input.

---

## 🔹 23. What is the advantage of dynamic programming over recursion?

**Answer:**

* Faster
* Avoids repeated calculations
* Uses memory efficiently

---

## 🔹 24. What is the space complexity of DP approach?

**Answer:**
O(m × n)

---

## 🔹 25. What is normalization in IR?

**Answer:**
Converting text into a standard form before processing.

---

## 🔹 26. What is tokenization in this context?

**Answer:**
Breaking sentences into words (used in word-level edit distance).

---

## 🔹 27. What is the significance of prefix comparison?

**Answer:**
Edit distance is computed using smaller prefixes of strings.

---

## 🔹 28. What is approximate string matching?

**Answer:**
Finding strings that match approximately rather than exactly.

---

## 🔹 29. Can Edit Distance be zero?

**Answer:**
Yes, when both strings are identical.

---

## 🔹 30. What does a higher edit distance indicate?

**Answer:**
More difference between the two strings.

---

## 🔹 31. What is the limitation of Edit Distance?

**Answer:**

* Does not consider semantic meaning
* Only measures syntactic similarity

---

## 🔹 32. What is NLP?

**Answer:**
Natural Language Processing — field dealing with human language processing.

---

## 🔹 33. How does Edit Distance help in NLP?

**Answer:**

* Text correction
* Similarity measurement
* Language processing

---

## 🔹 34. What is substitution vs insertion difference?

**Answer:**

* Substitution → replace character
* Insertion → add new character

---

## 🔹 35. What is deletion operation?

**Answer:**
Removing a character from the string.

---

## 🔹 36. What is minimum edit distance?

**Answer:**
The smallest number of operations required to convert one string to another.

---

## 🔹 37. What is greedy approach vs DP in this context?

**Answer:**

* Greedy → may not give optimal solution
* DP → guarantees optimal solution

---

## 🔹 38. Why is Edit Distance widely used?

**Answer:**
Because it is simple, effective, and applicable in many domains like search and NLP.

---

## 🔹 39. What is string similarity?

**Answer:**
A measure of how alike two strings are.

---

## 🔹 40. Give real-life applications of Edit Distance.

**Answer:**

* Google spell check
* Auto-correct in keyboards
* DNA sequence matching
* Chatbots

---

