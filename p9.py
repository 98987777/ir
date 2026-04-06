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





For Viva - 

# 📘 IR Practical Viva Questions (Inverted Index & Query Processing)

📂 Reference Practical: :contentReference[oaicite:0]{index=0}

---

## 🔹 1. What is Information Retrieval (IR)?
**Answer:**  
Information Retrieval is the process of retrieving relevant documents from a large collection based on a user query.

---

## 🔹 2. What is an Inverted Index?
**Answer:**  
An inverted index is a data structure that maps each term to the list of documents in which it appears.

---

## 🔹 3. Why is an inverted index used?
**Answer:**  
It enables fast and efficient searching of documents.

---

## 🔹 4. What is indexing in IR?
**Answer:**  
Indexing is the process of organizing data to allow quick retrieval.

---

## 🔹 5. What is a term in IR?
**Answer:**  
A term is a word or token extracted from a document.

---

## 🔹 6. What is a posting list?
**Answer:**  
A posting list is the list of documents associated with a term.

---

## 🔹 7. What is term frequency (TF)?
**Answer:**  
The number of times a term appears in a document.

---

## 🔹 8. What is tokenization?
**Answer:**  
Breaking text into individual words or tokens.

---

## 🔹 9. What is preprocessing?
**Answer:**  
Cleaning and preparing text (lowercasing, removing punctuation, etc.).

---

## 🔹 10. What is stopword removal?
**Answer:**  
Removing common words that do not add meaningful value.

---

## 🔹 11. What is normalization?
**Answer:**  
Converting text into a standard format (e.g., lowercase).

---

## 🔹 12. What is a corpus?
**Answer:**  
A collection of documents used in IR.

---

## 🔹 13. What is document ID?
**Answer:**  
A unique identifier assigned to each document.

---

## 🔹 14. What is query processing?
**Answer:**  
Processing a user query to retrieve relevant documents.

---

## 🔹 15. What is Boolean retrieval?
**Answer:**  
Retrieving documents using logical operators like AND, OR, NOT.

---

## 🔹 16. What is intersection in query processing?
**Answer:**  
Finding common documents that contain all query terms.

---

## 🔹 17. What is union in query processing?
**Answer:**  
Finding documents that contain any of the query terms.

---

## 🔹 18. What is search efficiency?
**Answer:**  
How quickly relevant documents are retrieved.

---

## 🔹 19. What is scalability in IR?
**Answer:**  
Ability to handle large datasets efficiently.

---

## 🔹 20. What is vocabulary in IR?
**Answer:**  
The set of all unique terms in the corpus.

---

## 🔹 21. What is the advantage of inverted index?
**Answer:**  
- Fast search  
- Efficient storage  
- Scalable  

---

## 🔹 22. What is the limitation of inverted index?
**Answer:**  
- Requires preprocessing  
- Storage overhead  

---

## 🔹 23. What is document retrieval?
**Answer:**  
Fetching documents relevant to a query.

---

## 🔹 24. What is ranking in IR?
**Answer:**  
Ordering documents based on relevance.

---

## 🔹 25. What is relevance?
**Answer:**  
How well a document matches a query.

---

## 🔹 26. What is exact match retrieval?
**Answer:**  
Retrieving documents that exactly match the query terms.

---

## 🔹 27. What is approximate matching?
**Answer:**  
Retrieving documents that are similar but not exact matches.

---

## 🔹 28. What is data structure used in inverted index?
**Answer:**  
Dictionary or hash map.

---

## 🔹 29. What is frequency count in IR?
**Answer:**  
Counting occurrences of terms in documents.

---

## 🔹 30. What is alphabetical sorting in IR?
**Answer:**  
Arranging terms in order for easier access.

---

## 🔹 31. What is feature extraction?
**Answer:**  
Converting text into useful features for processing.

---

## 🔹 32. What is document similarity?
**Answer:**  
Measuring how similar two documents are.

---

## 🔹 33. What is bag-of-words model?
**Answer:**  
Representing text as a collection of words without order.

---

## 🔹 34. What is IR system?
**Answer:**  
A system that retrieves relevant information based on queries.

---

## 🔹 35. What is search engine?
**Answer:**  
A system that uses IR techniques to search the web.

---

## 🔹 36. What is data filtering?
**Answer:**  
Selecting relevant information from data.

---

## 🔹 37. What is text mining?
**Answer:**  
Extracting useful information from text.

---

## 🔹 38. What is unstructured data?
**Answer:**  
Data without a fixed format (e.g., text documents).

---

## 🔹 39. What is real-world use of inverted index?
**Answer:**  
- Search engines  
- Document retrieval systems  
- Digital libraries  

---

## 🔹 40. Why is inverted index important?
**Answer:**  
Because it allows fast and efficient retrieval of relevant documents.

---

## 🔥 Tip for Viva:
If asked **“Explain inverted index in one line”**, say:  
👉 *“An inverted index maps terms to the documents in which they appear to enable fast search.”*

---
