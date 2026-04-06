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
