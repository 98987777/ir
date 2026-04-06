# -------------------- DATA --------------------
plays = {
    "Anthony and Cleopatra": "Anthony is there, Brutus is Caeser is with Cleopatra mercy worser.",
    "Julius Ceaser": "Anthony is there, Brutus is Caeser is but Calpurnia is.",
    "The Tempest": "mercy worser",
    "Hamlet": "Caeser and Brutus are present with mercy and worser",
    "Othello": "Caeser is present with mercy and worser",
    "Macbeth": "Anthony is there, Caeser, mercy."
}

words = ["Anthony", "Brutus", "Caeser", "Calpurnia", "Cleopatra", "mercy", "worser"]

# -------------------- STEP 1: CREATE VECTOR MATRIX --------------------
vector_matrix = [[0 for _ in range(len(plays))] for _ in range(len(words))]
text_list = list(plays.values())

for i in range(len(words)):
    for j in range(len(text_list)):
        if words[i].lower() in text_list[j].lower():
            vector_matrix[i][j] = 1

print("Vector Matrix:")
for i in range(len(words)):
    print(words[i], ":", vector_matrix[i])

# -------------------- STEP 2: CONVERT TO BIT PATTERNS --------------------
vector_dict = {}

for i in range(len(words)):
    bit_string = ""
    for bit in vector_matrix[i]:
        bit_string += str(bit)
    vector_dict[words[i]] = int(bit_string, 2)

print("\nBit Representation:")
for k, v in vector_dict.items():
    print(k, ":", bin(v))

# -------------------- FUNCTION TO PROCESS QUERY --------------------
def process_query(query):
    q = query

    # Fix common mistakes
    q = q.replace("Caesar", "Caeser")
    q = q.replace("Antony", "Anthony")
    q = q.replace("Calpurni", "Calpurnia")

    # Replace words with numbers
    for word in words:
        if word in q:
            q = q.replace(word, str(vector_dict[word]))

    # Replace logical operators
    q = q.replace("AND", "&").replace("and", "&")
    q = q.replace("OR", "|").replace("or", "|")
    q = q.replace("NOT", "~").replace("not", "~")

    print("\nConverted Query:", q)

    # Evaluate
    result = eval(q)

    # Convert to binary
    result_bin = bin(result)[2:].zfill(len(plays))
    print("Result (Binary):", result_bin)

    # Display result
    print("Matching Plays:")
    play_names = list(plays.keys())
    for i in range(len(result_bin)):
        if result_bin[i] == '1':
            print("-", play_names[i])


# -------------------- USER INPUT --------------------
while True:
    query = input("\nEnter query (or type EXIT to stop): ")

    if query.lower() == "exit":
        break

    print("\n====================================")
    print("Query:", query)
    process_query(query)









# For Viva -


# 📘 IR Practical Viva Questions (Boolean Retrieval Model)

---

## 🔹 1. What is Information Retrieval (IR)?

**Answer:**
Information Retrieval is the process of obtaining relevant information or documents from a large collection based on a user query.

---

## 🔹 2. What is the Boolean Retrieval Model?

**Answer:**
The Boolean Retrieval Model is an IR technique where documents are retrieved using logical operators like **AND, OR, NOT** to match query terms exactly.

---

## 🔹 3. What are Boolean operators used in IR?

**Answer:**

* **AND** → Returns documents containing all terms
* **OR** → Returns documents containing at least one term
* **NOT** → Excludes documents containing a term

---

## 🔹 4. What is a term-document matrix?

**Answer:**
It is a matrix where rows represent terms and columns represent documents, and values indicate the presence (1) or absence (0) of a term in a document.

---

## 🔹 5. What is vector representation in IR?

**Answer:**
It represents documents and terms as vectors (arrays of numbers), allowing efficient computation and comparison.

---

## 🔹 6. What is a bit vector?

**Answer:**
A bit vector is a binary representation (0s and 1s) indicating whether a term is present in each document.

---

## 🔹 7. Why is binary representation used in Boolean IR?

**Answer:**
Because it simplifies operations using bitwise logic, making retrieval faster and memory-efficient.

---

## 🔹 8. What are bitwise operations?

**Answer:**
Bitwise operations perform logical operations on binary numbers:

* `&` → AND
* `|` → OR
* `~` → NOT

---

## 🔹 9. How does AND operation work in IR?

**Answer:**
It returns only documents where **both terms are present** (1 & 1 = 1).

---

## 🔹 10. How does OR operation work in IR?

**Answer:**
It returns documents where **at least one term is present**.

---

## 🔹 11. How does NOT operation work?

**Answer:**
It excludes documents containing the specified term.

---

## 🔹 12. What is a query in IR?

**Answer:**
A query is a request given by the user to retrieve relevant documents.

---

## 🔹 13. What is query processing?

**Answer:**
It involves transforming the user query into a format that can be executed on the document representation.

---

## 🔹 14. What is indexing?

**Answer:**
Indexing is the process of organizing data (terms and documents) to enable fast searching.

---

## 🔹 15. What is an inverted index?

**Answer:**
It maps each term to the list of documents in which it appears.

---

## 🔹 16. What is the advantage of Boolean IR model?

**Answer:**

* Simple to implement
* Fast retrieval using bit operations
* Easy to understand

---

## 🔹 17. What are the limitations of Boolean IR?

**Answer:**

* No ranking of results
* Exact match required
* Cannot handle partial relevance

---

## 🔹 18. What is term normalization?

**Answer:**
It is converting terms into a standard form (e.g., lowercase, correcting spelling).

---

## 🔹 19. Why is case normalization important?

**Answer:**
To ensure consistency so that words like “Anthony” and “anthony” are treated the same.

---

## 🔹 20. What is tokenization?

**Answer:**
It is the process of breaking text into smaller units like words or terms.

---

## 🔹 21. What is stemming?

**Answer:**
It reduces words to their root form (e.g., "running" → "run").

---

## 🔹 22. What is precision in IR?

**Answer:**
Precision is the fraction of retrieved documents that are relevant.

---

## 🔹 23. What is recall in IR?

**Answer:**
Recall is the fraction of relevant documents that are retrieved.

---

## 🔹 24. Difference between precision and recall?

**Answer:**

* Precision → Accuracy of results
* Recall → Completeness of results

---

## 🔹 25. What is the difference between Boolean model and Vector Space Model?

**Answer:**

* Boolean → Exact match, no ranking
* Vector Space → Uses weights and ranks results

---

## 🔹 26. What is document ranking?

**Answer:**
It is ordering documents based on relevance to the query.

---

## 🔹 27. Why Boolean model does not support ranking?

**Answer:**
Because it only checks presence or absence (binary), not degree of relevance.

---

## 🔹 28. What is relevance in IR?

**Answer:**
It indicates how well a document satisfies a user’s query.

---

## 🔹 29. What is query optimization?

**Answer:**
It improves query execution efficiency, often by reordering operations.

---

## 🔹 30. What is the role of preprocessing in IR?

**Answer:**
It improves accuracy and efficiency by cleaning and standardizing data.

---

## 🔹 31. What is the importance of IR systems?

**Answer:**
They help users quickly find relevant information from large datasets (e.g., search engines).

---

## 🔹 32. Give real-world examples of IR systems.

**Answer:**

* Search engines (Google)
* Library search systems
* E-commerce search

---

## 🔹 33. What is the difference between data retrieval and information retrieval?

**Answer:**

* Data Retrieval → Exact data match
* Information Retrieval → Relevant information based on meaning

---

## 🔹 34. What is a corpus in IR?

**Answer:**
A corpus is a collection of documents used in IR systems.

---

## 🔹 35. Why is IR important in modern applications?

**Answer:**
Because of large data availability, IR helps in fast and relevant information access.

---

## 🔹 36. What is stop word removal?

**Answer:**
Removing common words like “is”, “the”, “and” that do not add much meaning.

---

## 🔹 37. What is scalability in IR systems?

**Answer:**
Ability to handle large datasets efficiently.

---

## 🔹 38. What is efficiency in IR?

**Answer:**
How fast the system retrieves results.

---

## 🔹 39. What is effectiveness in IR?

**Answer:**
How relevant the retrieved results are.

---

## 🔹 40. What is a search engine?

**Answer:**
A system that uses IR techniques to retrieve information from the web.


