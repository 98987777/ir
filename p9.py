1) Implement Inverted Index Concept
import nltk
from nltk.corpus import stopwords

# Download stopwords
nltk.download('stopwords')
stop_words = stopwords.words('english')

# Define the documents
document1 = "The quick brown fox jumped over the lazy dog"
document2 = "The lazy dog slept in the sun"

# Step 1: Tokenize
tokens1 = document1.lower().split()
tokens2 = document2.lower().split()

# Combine tokens into unique terms
terms = list(set(tokens1 + tokens2))

# Step 2: Build the inverted index
inverted_index = {}
occ_num_doc1 = {}
occ_num_doc2 = {}

for term in terms:
    if term in stop_words:
        continue

    documents = []

    if term in tokens1:
        documents.append("Document1")
        occ_num_doc1[term] = tokens1.count(term)

    if term in tokens2:
        documents.append("Document2")
        occ_num_doc2[term] = tokens2.count(term)

    inverted_index[term] = documents

# Step 3: Print the inverted index
for term, documents in inverted_index.items():
    print(term, "->", end=" ")
    for doc in documents:
        if doc == "Document1":
            print(f"{doc} ({occ_num_doc1.get(term, 0)})", end=" ")
        else:
            print(f"{doc} ({occ_num_doc2.get(term, 0)})", end=" ")
    print()
✅ 2) Retrieve Document based on Query
import os
import string
from collections import defaultdict

# 1. Preprocess text
def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.split()

# 2. Build Inverted Index
def build_inverted_index(documents):
    inverted_index = defaultdict(set)
    for doc_id, text in documents.items():
        words = preprocess_text(text)
        for word in words:
            inverted_index[word].add(doc_id)
    return inverted_index

# 3. Query the Inverted Index
def search(inverted_index, query):
    query_terms = preprocess_text(query)
    result_set = None

    for term in query_terms:
        if term in inverted_index:
            if result_set is None:
                result_set = inverted_index[term]
            else:
                result_set = result_set.intersection(inverted_index[term])
        else:
            return set()

    return result_set if result_set else set()

# 4. Documents
documents = {
    1: "Information retrieval is an essential aspect of search engines.",
    2: "The field of information retrieval focuses on algorithms.",
    3: "Search engines use retrieval techniques to improve performance.",
    4: "Deep learning models are used for information retrieval tasks."
}

# Build index
inverted_index = build_inverted_index(documents)

# Query
query = "retrieval"
result = search(inverted_index, query)

print(f"Documents containing the query '{query}': {sorted(result)}")
✅ 3) Display Inverted Index in Alphabetical Order
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = stopwords.words('english')

document1 = "The quick brown fox jumped over the lazy dog"
document2 = "The lazy dog slept in the sun"

tokens1 = document1.lower().split()
tokens2 = document2.lower().split()

terms = list(set(tokens1 + tokens2))

inverted_index = {}
occ_num_doc1 = {}
occ_num_doc2 = {}

for term in terms:
    if term in stop_words:
        continue

    documents = []

    if term in tokens1:
        documents.append("Document1")
        occ_num_doc1[term] = tokens1.count(term)

    if term in tokens2:
        documents.append("Document2")
        occ_num_doc2[term] = tokens2.count(term)

    inverted_index[term] = documents

# Print sorted index
for term in sorted(inverted_index.keys()):
    print(term, "->", end=" ")
    for doc in inverted_index[term]:
        if doc == "Document1":
            print(f"{doc} ({occ_num_doc1.get(term, 0)})", end=" ")
        else:
            print(f"{doc} ({occ_num_doc2.get(term, 0)})", end=" ")
    print()
✅ 4) Count Total Unique Terms
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = stopwords.words('english')

document1 = "The quick brown fox jumped over the lazy dog"
document2 = "The lazy dog slept in the sun"

tokens1 = document1.lower().split()
tokens2 = document2.lower().split()

terms = list(set(tokens1 + tokens2))

inverted_index = {}
occ_num_doc1 = {}
occ_num_doc2 = {}

for term in terms:
    if term in stop_words:
        continue

    documents = []

    if term in tokens1:
        documents.append("Document1")
        occ_num_doc1[term] = tokens1.count(term)

    if term in tokens2:
        documents.append("Document2")
        occ_num_doc2[term] = tokens2.count(term)

    inverted_index[term] = documents

print("Inverted Index (Alphabetical Order):\n")

for term in sorted(inverted_index.keys()):
    print(term, "->", end=" ")
    for doc in inverted_index[term]:
        if doc == "Document1":
            print(f"{doc} ({occ_num_doc1.get(term, 0)})", end=" ")
        else:
            print(f"{doc} ({occ_num_doc2.get(term, 0)})", end=" ")
    print()

# Count unique terms
total_unique_terms = len(inverted_index)
print("\nTotal number of unique terms indexed:", total_unique_terms)


