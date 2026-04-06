import nltk
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import defaultdict


nltk.download("punkt")
nltk.download("stopwords")


def process(file):
    raw = open(file).read().lower()
    tokens = word_tokenize(raw)


    stop_words = set(stopwords.words("english"))
    words = [w for w in tokens if w.isalpha() and w not in stop_words]


    count = defaultdict(int)
    for word in words:
        count[word] += 1


    return count


def cs_sim(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def getSimilarity(dict1, dict2):
    all_words = list(set(dict1.keys()).union(dict2.keys()))


    v1 = np.zeros(len(all_words))
    v2 = np.zeros(len(all_words))


    for i, word in enumerate(all_words):
        v1[i] = dict1.get(word, 0)
        v2[i] = dict2.get(word, 0)


    return cs_sim(v1, v2)


if __name__ == "__main__":
    dict1 = process("text1.txt")
    dict2 = process("text2.txt")


    print("Similarity between two text documents:",
          getSimilarity(dict1, dict2))





For Viva - 

# 📘 IR Practical Viva Questions (Cosine Similarity & Text Processing)

---

## 🔹 1. What is Information Retrieval (IR)?
**Answer:**  
Information Retrieval is the process of obtaining relevant information from large collections of data based on user queries.

---

## 🔹 2. What is text similarity?
**Answer:**  
Text similarity measures how similar two documents are based on their content.

---

## 🔹 3. What is Cosine Similarity?
**Answer:**  
Cosine Similarity measures the similarity between two vectors by calculating the cosine of the angle between them.

---

## 🔹 4. What is the range of Cosine Similarity?
**Answer:**  
It ranges from **0 to 1**:
- 1 → identical documents  
- 0 → completely different documents  

---

## 🔹 5. Why is Cosine Similarity used in IR?
**Answer:**  
Because it is efficient and works well with high-dimensional text data.

---

## 🔹 6. What is vector representation in IR?
**Answer:**  
It represents documents as numerical vectors based on term frequencies.

---

## 🔹 7. What is a term frequency (TF)?
**Answer:**  
The number of times a word appears in a document.

---

## 🔹 8. What is tokenization?
**Answer:**  
Breaking text into smaller units such as words.

---

## 🔹 9. What is stopword removal?
**Answer:**  
Removing common words like “the”, “is”, “and” that do not add meaningful information.

---

## 🔹 10. Why are stopwords removed?
**Answer:**  
To reduce noise and improve efficiency of text processing.

---

## 🔹 11. What is normalization in text processing?
**Answer:**  
Converting text into a standard form (e.g., lowercase).

---

## 🔹 12. What is preprocessing in IR?
**Answer:**  
Cleaning and preparing text before analysis.

---

## 🔹 13. What is bag-of-words model?
**Answer:**  
A model that represents text as a collection of words without considering order.

---

## 🔹 14. What is a feature vector?
**Answer:**  
A numerical representation of document features.

---

## 🔹 15. What is dimensionality in IR?
**Answer:**  
The number of unique terms used to represent documents.

---

## 🔹 16. What is Euclidean norm?
**Answer:**  
The length or magnitude of a vector.

---

## 🔹 17. What is dot product?
**Answer:**  
A mathematical operation used to measure similarity between vectors.

---

## 🔹 18. What is the advantage of Cosine Similarity?
**Answer:**  
- Ignores document length  
- Works well with sparse data  

---

## 🔹 19. What is the limitation of Cosine Similarity?
**Answer:**  
- Ignores word order  
- Does not capture semantics  

---

## 🔹 20. What is sparse data?
**Answer:**  
Data where most values are zero.

---

## 🔹 21. What is document similarity used for?
**Answer:**  
- Search engines  
- Plagiarism detection  
- Recommendation systems  

---

## 🔹 22. What is corpus?
**Answer:**  
A collection of documents used for analysis.

---

## 🔹 23. What is feature extraction?
**Answer:**  
Converting text into numerical features.

---

## 🔹 24. What is TF-IDF?
**Answer:**  
Term Frequency-Inverse Document Frequency, a weighting technique to measure importance of words.

---

## 🔹 25. Difference between TF and TF-IDF?
**Answer:**  
- TF → counts frequency  
- TF-IDF → weighs importance of words  

---

## 🔹 26. What is similarity vs distance?
**Answer:**  
- Similarity → measures closeness  
- Distance → measures difference  

---

## 🔹 27. What is vector space model?
**Answer:**  
A model that represents documents as vectors in multidimensional space.

---

## 🔹 28. What is indexing in IR?
**Answer:**  
Organizing data to enable fast searching.

---

## 🔹 29. What is relevance in IR?
**Answer:**  
How well a document matches a query.

---

## 🔹 30. What is document ranking?
**Answer:**  
Ordering documents based on similarity or relevance.

---

## 🔹 31. What is machine learning in IR?
**Answer:**  
Using algorithms to improve retrieval and ranking.

---

## 🔹 32. What is NLP?
**Answer:**  
Natural Language Processing — processing human language using computers.

---

## 🔹 33. What is stemming?
**Answer:**  
Reducing words to their root form.

---

## 🔹 34. What is lemmatization?
**Answer:**  
Converting words to their base dictionary form.

---

## 🔹 35. What is noise in text data?
**Answer:**  
Unnecessary or irrelevant information.

---

## 🔹 36. What is data cleaning?
**Answer:**  
Removing errors and unwanted data.

---

## 🔹 37. What is similarity threshold?
**Answer:**  
A value above which documents are considered similar.

---

## 🔹 38. What is clustering?
**Answer:**  
Grouping similar documents together.

---

## 🔹 39. What is classification?
**Answer:**  
Assigning documents to predefined categories.

---

## 🔹 40. Why is Cosine Similarity important?
**Answer:**  
Because it efficiently measures document similarity in high-dimensional text data.

---

## 🔥 Tip for Viva:
If asked **“Explain Cosine Similarity in one line”**, say:  
👉 *“Cosine similarity measures the similarity between two documents by calculating the cosine of the angle between their vector representations.”*

---
