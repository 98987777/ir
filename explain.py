# 📘 Information Retrieval Practicals – Code Explanation (Markdown)

---

# 🔹 Practical 1: Boolean Retrieval using Incidence Matrix

### 📌 Explanation

This program demonstrates **Boolean retrieval using bitwise operations (AND, OR, NOT)**. It creates an incidence matrix where rows represent words and columns represent documents. Each cell contains 1 if the word is present in that document, otherwise 0. Then, Boolean queries are evaluated using bitwise operators on binary representations of these rows.

### 💻 Code Explanation (Line-by-Line)

* `plays = {...}`
  Stores documents (plays) as key-value pairs.

* `words = [...]`
  List of words to search in documents.

* `vector_matrix = [[0...]]`
  Creates a matrix initialized with 0s (rows = words, columns = documents).

* `text_list = list(plays.values())`
  Converts dictionary values into a list for easy processing.

* `tokens = text.lower().replace(...).split()`
  Converts text to lowercase, removes punctuation, and splits into words.

* `if words[i].lower() in tokens:`
  Checks if a word exists in the document.

* `vector_matrix[i][j] = 1`
  Marks presence of word.

* `mystring = "".join(str(d) for d in vector_matrix[i])`
  Converts row into binary string.

* `int(mystring, 2)`
  Converts binary string to integer for bitwise operations.

* `condition = input()`
  Takes Boolean query from user.

* `condition1.replace(word, vector)`
  Replaces words with their binary values.

* `condition1.replace("not", "~")`
  Converts NOT to bitwise NOT.

* `eval(condition1)`
  Evaluates Boolean expression.

* `format(result_bits, "0...b")`
  Converts result back to binary.

* `if bit == "1"`
  Prints matching documents.

---

# 🔹 Practical 2: Edit Distance & Levenshtein Distance

## 📌 Explanation

This program calculates the **minimum number of operations (insert, delete, substitute)** required to convert one string into another. It uses both **recursive method** and **dynamic programming (matrix-based)** for efficient computation.

---

## 🔹 1) Recursive Edit Distance

### 💻 Explanation

* `def editdistance(str1, str2, m, n):`
  Function to compute edit distance.

* `if m == 0: return n`
  If first string empty → insert all characters.

* `if n == 0: return m`
  If second string empty → delete all characters.

* `if str1[m-1] == str2[n-1]:`
  If last characters match → no cost.

* `return editdistance(...)`
  Move to next characters.

* `1 + min(...)`
  Take minimum of:

  * insertion
  * deletion
  * substitution

---

## 🔹 2) Levenshtein Distance (DP)

### 💻 Explanation

* `import numpy as np`
  Used to create matrix.

* `matrix = np.zeros((size_x, size_y))`
  Creates 2D matrix.

* `matrix[x,0] = x`
  Initializes first column (deletions).

* `matrix[0,y] = y`
  Initializes first row (insertions).

* `if seq1[x-1] == seq2[y-1]: cost = 0`
  No cost if same.

* `else: cost = 1`
  Cost for substitution.

* `matrix[x,y] = min(...)`
  Chooses minimum operation.

* `return matrix[last cell]`
  Final edit distance.

---

## 🔹 3) Word-Level Edit Distance

### 💻 Explanation

* `str.split()`
  Converts sentence into words.

* Same recursive logic applied
  But now operations are on **words instead of characters**

---

# 🔹 Practical 3: Soundex Algorithm

### 📌 Explanation

Soundex converts words into codes based on pronunciation, useful for matching similar sounding words.

### 💻 Explanation

* `first_letter = word[0].upper()`
  Keeps first letter.

* `mappings = {...}`
  Maps letters to digits.

* Loop through remaining letters
  Converts each letter to digit.

* `if digit != code[-1]`
  Avoid duplicates.

* `code[:3].ljust(3,"0")`
  Ensures 3 digits.

* `return first_letter + code`
  Final Soundex code.

---

# 🔹 Practical 4: N-gram Model

### 📌 Explanation

This program generates **N-grams (sequence of N words)** and computes similarity using **Jaccard coefficient**.

### 💻 Explanation

* `text.lower()`
  Converts text to lowercase.

* `re.sub(...)`
  Removes punctuation.

* `tokens = text.split()`
  Tokenization.

* `generate_ngrams()`
  Creates sequences of N words.

* `set()`
  Removes duplicates.

* `intersection = set_a ∩ set_b`
  Common n-grams.

* `union = set_a ∪ set_b`
  Total unique n-grams.

* `Jaccard = intersection / union`
  Similarity score.

---

# 🔹 Practical 5: PageRank Algorithm

### 📌 Explanation

This program calculates importance of web pages based on incoming links using iterative formula.

### 💻 Explanation

* `d = 0.85`
  Damping factor.

* `links = {...}`
  Stores page connections.

* `outdegree = len(links[page])`
  Number of outgoing links.

* `pagerank = {page:1.0}`
  Initial values.

* Loop iterations
  Updates PageRank values.

* `if p in links[q]`
  Checks incoming links.

* `incoming_sum += pagerank[q]/outdegree[q]`
  Contribution from other pages.

* `new_pagerank[p] = (1-d) + d*incoming_sum`
  PageRank formula.

---

# 🔹 Practical 6: Document Similarity

### 📌 Explanation

Calculates similarity between documents using **Cosine Similarity**.

### 💻 Explanation

* `nltk.download()`
  Downloads tokenizer and stopwords.

* `word_tokenize()`
  Splits text into words.

* `stopwords.words()`
  Removes common words.

* `defaultdict(int)`
  Stores word frequency.

* `np.zeros()`
  Creates vectors.

* `np.dot(a,b)`
  Dot product.

* `np.linalg.norm()`
  Vector magnitude.

* `cosine = dot / (norms)`
  Similarity measure.

---

# 🔹 Practical 7: Stop Word Removal

### 📌 Explanation

Removes common words like “is”, “the” to improve processing.

### 💻 Explanation

* `word_tokenize()`
  Tokenizes text.

* `stop_words = set(...)`
  Stores stopwords.

* `[w for w in words if w not in stop_words]`
  Filters meaningful words.

* File version:

  * `open()` → read file
  * `write()` → save filtered text

---

# 🔹 Practical 8: Web Crawler

### 📌 Explanation

This program extracts links from a webpage and searches for a word across pages.

### 💻 Explanation

* `HTMLParser`
  Parses HTML content.

* `handle_starttag()`
  Detects `<a>` tags.

* `parse.urljoin()`
  Converts relative links to absolute.

* `urlopen()`
  Fetches webpage.

* `self.feed(html)`
  Parses HTML.

* `crawl(url, word)`
  Main crawling logic.

* `visitedURL`
  Avoids revisiting pages.

* `if word in data`
  Searches word in page.

---

# 🔹 Practical 9: Inverted Index

## 📌 Explanation

Maps words → documents for fast retrieval.

---

## 🔹 Index Creation

* `tokens = text.lower().split()`
  Tokenization.

* `terms = set(...)`
  Unique words.

* `if term in tokens:`
  Checks presence.

* `inverted_index[term] = documents`
  Maps word → docs.

---

## 🔹 Query Search

* `preprocess_text()`
  Cleans text.

* `defaultdict(set)`
  Stores doc IDs.

* `intersection()`
  Finds common documents.

---

## 🔹 Sorting & Count

* `sorted(inverted_index.keys())`
  Alphabetical order.

* `len(inverted_index)`
  Total unique terms.

---

# 🔹 Practical 10: XML Parsing & Web Graph

### 📌 Explanation

Parses XML (RSS feeds), extracts data, and builds graph.

### 💻 Explanation

* `requests.get(url)`
  Fetch XML data.

* `ET.parse()`
  Parses XML.

* `root.findall('.//item')`
  Extracts items.

* `child.tag.split('}')[-1]`
  Removes namespace.

* `csv`
  Writes data to Excel.

* `networkx`
  Creates graph.

* `matplotlib`
  Displays graph.

---














# 📘 IR Practical Exam – Code Explanation (Viva Ready)

---

# 🔹 Practical 1: Boolean Retrieval

### 📌 Explanation (Viva)

This program implements Boolean retrieval using an incidence matrix. Each word is represented as a binary vector indicating its presence in documents. Boolean queries like AND, OR, and NOT are evaluated using bitwise operations to retrieve matching documents.

### 💻 Key Code Explanation

* Dictionary → stores documents
* List of words → terms to search
* Matrix → word vs document (0/1)
* Tokenization → clean and split text
* Convert row → binary number
* Replace words → binary values in query
* Use `eval()` → evaluate Boolean expression
* Output → documents with result = 1

---

# 🔹 Practical 2: Edit Distance

### 📌 Explanation (Viva)

Edit distance calculates the minimum number of operations (insert, delete, substitute) required to convert one string into another. Recursive and dynamic programming approaches are used.

### 💻 Key Code Explanation

* Base case → if string empty
* Compare last characters
* If same → no cost
* Else → take minimum of:

  * insertion
  * deletion
  * substitution

---

## 🔹 Levenshtein (DP)

### 📌 Explanation

Uses matrix to efficiently compute edit distance.

### 💻 Key Points

* Matrix initialized
* First row/column → insert/delete cost
* Fill matrix using min formula
* Last cell → answer

---

# 🔹 Practical 3: Soundex Algorithm

### 📌 Explanation (Viva)

Soundex converts words into phonetic codes so similar sounding words have same code.

### 💻 Key Points

* Keep first letter
* Map letters → digits
* Remove vowels
* Remove duplicates
* Pad with zeros → 4 characters

---

# 🔹 Practical 4: N-gram Model

### 📌 Explanation (Viva)

Generates sequences of N words and computes similarity using Jaccard coefficient.

### 💻 Key Points

* Preprocess → lowercase, remove punctuation
* Tokenize → split text
* Generate N-grams
* Convert to set
* Jaccard = Intersection / Union

---

# 🔹 Practical 5: PageRank

### 📌 Explanation (Viva)

PageRank calculates importance of web pages based on incoming links using iterative formula.

### 💻 Key Points

* Damping factor (0.85)
* Initialize rank = 1
* Check incoming links
* Apply formula:
  PR = (1-d) + d × sum
* Repeat iterations

---

# 🔹 Practical 6: Document Similarity

### 📌 Explanation (Viva)

Computes similarity between documents using cosine similarity.

### 💻 Key Points

* Tokenization
* Remove stopwords
* Count word frequency
* Create vectors
* Dot product / magnitude
* Output similarity value

---

# 🔹 Practical 7: Stop Word Removal

### 📌 Explanation (Viva)

Removes common words (like “is”, “the”) to improve text processing.

### 💻 Key Points

* Tokenize sentence
* Load stopwords
* Filter words
* File version → read & write

---

# 🔹 Practical 8: Web Crawler

### 📌 Explanation (Viva)

Extracts links from a webpage and searches for a specific word.

### 💻 Key Points

* HTMLParser → parse HTML
* Extract `<a>` tags
* Convert relative → absolute URL
* Visit links
* Search word in page
* Store results

---

# 🔹 Practical 9: Inverted Index

### 📌 Explanation (Viva)

Stores mapping of words to documents for fast searching.

### 💻 Key Points

* Tokenize documents
* Remove stopwords
* Store word → document list
* Query → intersection of sets
* Sort terms alphabetically
* Count unique words

---

# 🔹 Practical 10: XML Parsing & Web Graph

### 📌 Explanation (Viva)

Parses XML data (RSS feeds), extracts information, and builds a graph.

### 💻 Key Points

* Fetch XML using requests
* Parse using ElementTree
* Extract tags (title, link, etc.)
* Store in CSV
* Use NetworkX → create graph
* Use Matplotlib → display graph

---

