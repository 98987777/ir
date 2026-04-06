#Text Pre-processing: Stop Word Removal using NLTK
#a. Direct text
Code: - 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
nltk.download('stopwords')


example_sent = "This is a sample sentence, show off the stop words filtration."


stop_words = set (stopwords.words('english'))


word_tokens = word_tokenize (example_sent)
print (word_tokens)


filtered_sentence = [w for w in word_tokens if not w in stop_words]
print (filtered_sentence)


for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
        print (filtered_sentence)



# b. reading text from a text file & importing it in a text file
Code: - 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
nltk.download('stopwords')


stop_words = set (stopwords.words('english'))


f = open ('to_filt_text.txt', "r")


words = f.read()


words_list = words.split()


filtered_sentence = [ ]
write_file = open ('to_write_data.txt', "w")


for w in words_list:
    if w not in stop_words:
        filtered_sentence.append(w)
        print (filtered_sentence)
        write_file.write(w + " ")





For Viva -

# 📘 IR Practical Viva Questions (Stopword Removal & Text Preprocessing)

---

## 🔹 1. What is Information Retrieval (IR)?
**Answer:**  
Information Retrieval is the process of obtaining relevant information from large collections of data.

---

## 🔹 2. What is text preprocessing?
**Answer:**  
Text preprocessing is the process of cleaning and preparing raw text before analysis.

---

## 🔹 3. What are stopwords?
**Answer:**  
Stopwords are common words like “the”, “is”, “and” that do not add significant meaning.

---

## 🔹 4. Why are stopwords removed?
**Answer:**  
To reduce noise and improve the efficiency and accuracy of text analysis.

---

## 🔹 5. What is tokenization?
**Answer:**  
Tokenization is the process of breaking text into individual words or tokens.

---

## 🔹 6. What is normalization?
**Answer:**  
Normalization converts text into a standard format (e.g., lowercase).

---

## 🔹 7. What is the role of stopword removal in IR?
**Answer:**  
It improves search performance by focusing on meaningful words.

---

## 🔹 8. What is noise in text data?
**Answer:**  
Irrelevant or unnecessary data that does not contribute to analysis.

---

## 🔹 9. What is data cleaning?
**Answer:**  
Removing unwanted or incorrect data from a dataset.

---

## 🔹 10. What is corpus?
**Answer:**  
A collection of text documents used for processing.

---

## 🔹 11. What is feature extraction?
**Answer:**  
Converting text into useful features for analysis.

---

## 🔹 12. What is bag-of-words model?
**Answer:**  
A representation of text as a collection of words without considering order.

---

## 🔹 13. What is the advantage of removing stopwords?
**Answer:**  
- Reduces data size  
- Improves processing speed  
- Enhances meaningful analysis  

---

## 🔹 14. What is the disadvantage of removing stopwords?
**Answer:**  
It may remove important context in some cases.

---

## 🔹 15. What is Natural Language Processing (NLP)?
**Answer:**  
A field of computer science that deals with processing human language.

---

## 🔹 16. What is stemming?
**Answer:**  
Reducing words to their root form (e.g., “running” → “run”).

---

## 🔹 17. What is lemmatization?
**Answer:**  
Converting words to their base dictionary form.

---

## 🔹 18. What is case folding?
**Answer:**  
Converting all text to the same case (usually lowercase).

---

## 🔹 19. What is text filtering?
**Answer:**  
Removing unwanted elements from text data.

---

## 🔹 20. What is indexing in IR?
**Answer:**  
Organizing data to enable fast retrieval.

---

## 🔹 21. What is search query?
**Answer:**  
Input given by the user to retrieve information.

---

## 🔹 22. What is relevance in IR?
**Answer:**  
How well a document matches the user query.

---

## 🔹 23. What is document processing?
**Answer:**  
Preparing documents for analysis or retrieval.

---

## 🔹 24. What is structured vs unstructured data?
**Answer:**  
- Structured → organized (tables)  
- Unstructured → raw text  

---

## 🔹 25. What is text mining?
**Answer:**  
Extracting useful information from text.

---

## 🔹 26. What is word frequency?
**Answer:**  
Number of times a word appears in text.

---

## 🔹 27. What is vocabulary in IR?
**Answer:**  
Set of unique words in a corpus.

---

## 🔹 28. What is dimensionality reduction?
**Answer:**  
Reducing number of features for efficiency.

---

## 🔹 29. What is efficiency in IR?
**Answer:**  
How fast results are retrieved.

---

## 🔹 30. What is effectiveness in IR?
**Answer:**  
How relevant the retrieved results are.

---

## 🔹 31. What is preprocessing pipeline?
**Answer:**  
Sequence of steps applied to clean and prepare text.

---

## 🔹 32. What is file handling in IR?
**Answer:**  
Reading and writing text data from files.

---

## 🔹 33. What is encoding in text files?
**Answer:**  
Format used to represent characters (e.g., UTF-8).

---

## 🔹 34. What is scalability in IR?
**Answer:**  
Ability to handle large datasets efficiently.

---

## 🔹 35. What is automation in text processing?
**Answer:**  
Automatically processing large text data.

---

## 🔹 36. What is feature selection?
**Answer:**  
Choosing important features for analysis.

---

## 🔹 37. What is text representation?
**Answer:**  
Converting text into numerical or structured form.

---

## 🔹 38. What is real-world use of stopword removal?
**Answer:**  
- Search engines  
- Chatbots  
- Text classification  

---

## 🔹 39. What is information filtering?
**Answer:**  
Selecting relevant information from large data.

---

## 🔹 40. Why is preprocessing important in IR?
**Answer:**  
Because it improves accuracy, efficiency, and quality of results.

---

## 🔥 Tip for Viva:
If asked **“Explain stopword removal in one line”**, say:  
👉 *“Stopword removal is the process of eliminating common words that do not add meaningful information to improve text processing efficiency.”*

---
f.close()
write_file.close()


