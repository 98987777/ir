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







---

# 📘 IR Practicals – Logic (Exam Ready)

---

# 🔹 Practical 1: Boolean Retrieval

### 📌 Logic

1. Store documents in a dictionary
2. Define list of words (terms)
3. Create incidence matrix (rows = words, columns = documents)
4. For each document:

   * Convert text to lowercase
   * Remove punctuation
   * Split into tokens
5. Check if each word exists in document → mark 1 or 0
6. Convert each row into binary number
7. Take Boolean query as input
8. Replace words with their binary values
9. Apply bitwise operations (AND, OR, NOT)
10. Convert result into binary
11. Display documents where result = 1

---

# 🔹 Practical 2: Edit Distance

## 📌 Logic (Recursive)

1. If one string is empty → return length of other
2. Compare last characters:

   * If same → ignore and move forward
   * Else → perform operations:

     * Insert
     * Delete
     * Substitute
3. Take minimum of all operations
4. Return final value

---

## 🔹 Levenshtein (DP)

### 📌 Logic

1. Create matrix of size (m+1 × n+1)
2. Initialize:

   * First row → insertion
   * First column → deletion
3. For each cell:

   * If characters same → cost = 0
   * Else → cost = 1
4. Fill matrix using:

   * Min(insert, delete, substitute)
5. Final answer = last cell

---

## 🔹 Word-Level Edit Distance

### 📌 Logic

1. Take two sentences
2. Convert into word lists
3. Apply same edit distance logic
4. Compare words instead of characters
5. Return minimum operations

---

# 🔹 Practical 3: Soundex Algorithm

### 📌 Logic

1. Keep first letter of word
2. Convert remaining letters into digits using mapping
3. Remove vowels and ignored letters
4. Remove duplicate consecutive digits
5. Keep only first 3 digits
6. Pad with 0 if needed
7. Return final 4-character code

---

# 🔹 Practical 4: N-gram Model

### 📌 Logic

1. Take two input texts
2. Convert to lowercase
3. Remove punctuation
4. Tokenize into words
5. Generate N-grams (sequence of N words)
6. Convert N-grams into sets
7. Find:

   * Intersection (common N-grams)
   * Union (all N-grams)
8. Compute Jaccard similarity:

   * Intersection / Union
9. Repeat for bigrams and trigrams

---

# 🔹 Practical 5: PageRank

### 📌 Logic

1. Define pages and their links
2. Initialize PageRank of each page = 1
3. Set damping factor (d = 0.85)
4. For each iteration:

   * For each page:

     * Find pages linking to it
     * Compute contribution
5. Apply formula:
   PR = (1 - d) + d × (incoming links contribution)
6. Update values
7. Repeat for multiple iterations
8. Display final ranks

---

# 🔹 Practical 6: Document Similarity

### 📌 Logic

1. Read both documents
2. Convert text to lowercase
3. Tokenize words
4. Remove stopwords
5. Count frequency of each word
6. Create vectors for both documents
7. Compute:

   * Dot product
   * Magnitude of vectors
8. Apply cosine similarity formula
9. Return similarity value

---

# 🔹 Practical 7: Stop Word Removal

### 📌 Logic

1. Take input text
2. Tokenize into words
3. Load stopwords list
4. Remove words present in stopwords
5. Store filtered words
6. Print or write output to file

---

# 🔹 Practical 8: Web Crawler

### 📌 Logic

1. Input URL and search word
2. Fetch webpage using URL
3. Parse HTML content
4. Extract all links (`<a>` tags)
5. Convert relative links to absolute
6. Visit each link
7. Check if word exists in page
8. Store matching URLs
9. Avoid revisiting same URLs
10. Print results

---

# 🔹 Practical 9: Inverted Index

## 📌 Logic (Indexing)

1. Take documents
2. Convert to lowercase
3. Tokenize words
4. Remove stopwords
5. For each word:

   * Store document ID
   * Count occurrences
6. Create mapping:
   word → list of documents

---

## 📌 Logic (Retrieval)

1. Take query input
2. Preprocess query
3. Find documents for each word
4. Apply intersection (AND logic)
5. Return matching documents

---

## 📌 Logic (Extras)

* Sort terms alphabetically
* Count total unique terms

---

# 🔹 Practical 10: XML Parsing & Web Graph

### 📌 Logic

1. Fetch XML data from URL
2. Save XML file
3. Parse XML using ElementTree
4. Extract required fields (title, link, etc.)
5. Store data in list
6. Write data to CSV (Excel)
7. Create graph using NetworkX
8. Add nodes and edges
9. Display graph using Matplotlib

---

