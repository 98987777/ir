🔹 1. Bigram Display
Code:
# BIGRAM DISPLAY

def preprocess(text):
    text = text.lower()
    tokens = text.split()
    return tokens

def display_bigrams(text):
    tokens = preprocess(text)
    bigrams = []

    for i in range(len(tokens) - 1):
        bigram = (tokens[i], tokens[i+1])
        bigrams.append(bigram)

    print("\nBigrams:")
    for bg in bigrams:
        print(bg)

# -------- MAIN --------
text = input("Enter text for bigram display: ")
display_bigrams(text)

🔹 2. Trigram Display
Code:
# TRIGRAM DISPLAY

def preprocess(text):
    text = text.lower()
    tokens = text.split()
    return tokens

def display_trigrams(text):
    tokens = preprocess(text)
    trigrams = []

    for i in range(len(tokens) - 2):
        trigram = (tokens[i], tokens[i+1], tokens[i+2])
        trigrams.append(trigram)

    print("\nTrigrams:")
    for tg in trigrams:
        print(tg)

# -------- MAIN --------
text = input("Enter text for trigram display: ")
display_trigrams(text)

🔹 3. Jaccard Coefficient using N-gram Model
Code:
import re

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]+', '', text)
    tokens = text.split()
    return tokens

def generate_ngrams(tokens, n):
    ngrams = []
    for i in range(len(tokens) - n + 1):
        ngram = tuple(tokens[i:i+n])
        ngrams.append(ngram)
    return ngrams

def jaccard_coefficient(set_a, set_b):
    intersection = set_a.intersection(set_b)
    union = set_a.union(set_b)
    if len(union) == 0:
        return 0.0, intersection, union
    jacc = len(intersection) / len(union)
    return jacc, intersection, union

# Take input from user
text1 = input("Enter first text: ")
text2 = input("Enter second text: ")
n = int(input("Enter N for N-gram: "))

# Preprocess
tokens1 = preprocess(text1)
tokens2 = preprocess(text2)

print("\nTokens of Text 1:", tokens1)
print("Tokens of Text 2:", tokens2)

# N-GRAMS
ngrams1 = set(generate_ngrams(tokens1, n))
ngrams2 = set(generate_ngrams(tokens2, n))

print(f"\n{n}-grams of Text 1:")
for ng in ngrams1:
    print(ng)

print(f"\n{n}-grams of Text 2:")
for ng in ngrams2:
    print(ng)

# Jaccard for N-grams
jacc_n, inter_n, union_n = jaccard_coefficient(ngrams1, ngrams2)

print(f"\n=== {n}-GRAM JACCARD COEFFICIENT ===")
print("Intersection:", inter_n)
print("Union size:", len(union_n))
print(f"Jaccard Coefficient ({n}-grams) = {len(inter_n)}/{len(union_n)} = {jacc_n}")

# BIGRAMS
bigrams1 = set(generate_ngrams(tokens1, 2))
bigrams2 = set(generate_ngrams(tokens2, 2))

print("\nBigrams of Text 1:")
for bg in bigrams1:
    print(bg)

print("\nBigrams of Text 2:")
for bg in bigrams2:
    print(bg)

# Jaccard for bigrams
jacc_bigram, inter_bi, union_bi = jaccard_coefficient(bigrams1, bigrams2)

print("\n=== BIGRAM JACCARD COEFFICIENT ===")
print("Intersection (common bigrams):", inter_bi)
print("Union size:", len(union_bi))
print(f"Jaccard Coefficient (bigrams) = {len(inter_bi)}/{len(union_bi)} = {jacc_bigram}")

# TRIGRAMS
trigrams1 = set(generate_ngrams(tokens1, 3))
trigrams2 = set(generate_ngrams(tokens2, 3))

print("\nTrigrams of Text 1:")
for tg in trigrams1:
    print(tg)

print("\nTrigrams of Text 2:")
for tg in trigrams2:
    print(tg)

# Jaccard for trigrams
jacc_trigram, inter_tri, union_tri = jaccard_coefficient(trigrams1, trigrams2)

print("\n=== TRIGRAM JACCARD COEFFICIENT ===")
print("Intersection (common trigrams):", inter_tri)
print("Union size:", len(union_tri))
print(f"Jaccard Coefficient (trigrams) = {len(inter_tri)}/{len(union_tri)} = {jacc_trigram}")
Output:
(Write output based on your input)



For Viva -
# 📘 IR Practical Viva Questions (N-grams & Jaccard Coefficient)

---

## 🔹 1. What is an N-gram?

**Answer:**
An N-gram is a sequence of *N consecutive words or tokens* from a text.

---

## 🔹 2. What is a Bigram?

**Answer:**
A bigram is a sequence of **2 consecutive words** (N = 2).

---

## 🔹 3. What is a Trigram?

**Answer:**
A trigram is a sequence of **3 consecutive words** (N = 3).

---

## 🔹 4. Why are N-grams used in Information Retrieval?

**Answer:**
They help in:

* Text analysis
* Similarity detection
* Language modeling

---

## 🔹 5. What is tokenization?

**Answer:**
Breaking text into smaller units like words or tokens.

---

## 🔹 6. What is preprocessing in IR?

**Answer:**
Cleaning and preparing text (lowercasing, removing punctuation).

---

## 🔹 7. What is the purpose of lowercasing text?

**Answer:**
To ensure uniformity and avoid treating same words differently.

---

## 🔹 8. What is similarity measurement?

**Answer:**
It measures how similar two texts are.

---

## 🔹 9. What is Jaccard Coefficient?

**Answer:**
It is a similarity measure defined as:
👉 **Intersection / Union of two sets**

---

## 🔹 10. What does Jaccard similarity value indicate?

**Answer:**

* 0 → no similarity
* 1 → identical

---

## 🔹 11. What is intersection in Jaccard?

**Answer:**
Common elements between two sets.

---

## 🔹 12. What is union in Jaccard?

**Answer:**
All unique elements from both sets combined.

---

## 🔹 13. Why use sets in Jaccard similarity?

**Answer:**
To remove duplicate elements and focus on unique features.

---

## 🔹 14. What is the difference between unigram, bigram, trigram?

**Answer:**

* Unigram → single word
* Bigram → 2 words
* Trigram → 3 words

---

## 🔹 15. How does increasing N affect results?

**Answer:**

* Higher N → more context, less matching
* Lower N → less context, more matching

---

## 🔹 16. What is text similarity used for?

**Answer:**

* Plagiarism detection
* Search engines
* Document clustering

---

## 🔹 17. What is approximate matching?

**Answer:**
Matching similar text rather than exact matches.

---

## 🔹 18. What is the role of N-grams in NLP?

**Answer:**
They help in predicting word sequences and understanding context.

---

## 🔹 19. What is language modeling?

**Answer:**
Predicting the probability of a sequence of words.

---

## 🔹 20. What is the advantage of bigrams?

**Answer:**
They capture context better than single words.

---

## 🔹 21. What is the limitation of N-grams?

**Answer:**

* Large storage requirement
* Data sparsity for large N

---

## 🔹 22. What is data sparsity?

**Answer:**
When many possible N-grams do not appear in the dataset.

---

## 🔹 23. What is cosine similarity vs Jaccard similarity?

**Answer:**

* Cosine → considers frequency
* Jaccard → considers presence/absence

---

## 🔹 24. What is feature extraction?

**Answer:**
Converting text into measurable features (like N-grams).

---

## 🔹 25. What is document similarity?

**Answer:**
Measuring how close two documents are in content.

---

## 🔹 26. What is set theory in IR?

**Answer:**
Using mathematical sets for operations like union and intersection.

---

## 🔹 27. What is normalization?

**Answer:**
Standardizing text (e.g., lowercase conversion).

---

## 🔹 28. What is stop word removal?

**Answer:**
Removing common words like “the”, “is”, “and”.

---

## 🔹 29. What is vector representation?

**Answer:**
Representing text as numerical features.

---

## 🔹 30. What is clustering in IR?

**Answer:**
Grouping similar documents together.

---

## 🔹 31. What is classification?

**Answer:**
Assigning documents to predefined categories.

---

## 🔹 32. What is text mining?

**Answer:**
Extracting useful information from text data.

---

## 🔹 33. What is corpus?

**Answer:**
A collection of text documents.

---

## 🔹 34. What is feature space?

**Answer:**
All possible features used to represent data.

---

## 🔹 35. What is similarity threshold?

**Answer:**
A value above which two documents are considered similar.

---

## 🔹 36. What is IR system?

**Answer:**
A system that retrieves relevant information based on queries.

---

## 🔹 37. What is the advantage of Jaccard similarity?

**Answer:**

* Simple
* Effective for set comparison

---

## 🔹 38. What is limitation of Jaccard similarity?

**Answer:**

* Ignores frequency of terms
* Less effective for large datasets

---

## 🔹 39. What is real-world use of N-grams?

**Answer:**

* Search engines
* Chatbots
* Auto-suggestions

---

## 🔹 40. Why are N-grams important in IR?

**Answer:**
Because they capture context and improve text similarity analysis.

---

## 🔥 Tip for Viva:

If examiner asks **“Explain Jaccard in one line”**, say:
👉 *“Jaccard similarity measures how similar two sets are by dividing the number of common elements by the total unique elements.”*

---


