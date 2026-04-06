def soundex(name):
    name = name.upper()

    soundex_mapping = {
        "B": "1", "F": "1", "P": "1", "V": "1",
        "C": "2", "G": "2", "J": "2", "K": "2", "Q": "2", "S": "2", "X": "2", "Z": "2",
        "D": "3", "T": "3",
        "L": "4",
        "M": "5", "N": "5",
        "R": "6"
    }

    first_letter = name[0]
    encoded = []

    for char in name[1:]:
        if char in soundex_mapping:
            code = soundex_mapping[char]
            encoded.append(code)
        else:
            encoded.append("0")  # For vowels/A, E, I, O, U, H, W, Y

    filtered = []
    previous = ""

    for code in encoded:
        if code != previous:
            filtered.append(code)
        previous = code

    filtered = [x for x in filtered if x != "0"]

    soundex_code = first_letter + "".join(filtered)

    soundex_code = soundex_code[:4].ljust(4, "0")

    return soundex_code


name = input("Enter a name: ")
print("Soundex Code:", soundex(name))



For Viva -
---

# 📘 IR Practical Viva Questions (Soundex & Phonetic Matching)

---

## 🔹 1. What is Soundex?

**Answer:**
Soundex is a phonetic algorithm used to index words based on their pronunciation rather than spelling.

---

## 🔹 2. Why is Soundex used in Information Retrieval?

**Answer:**
To find words that sound similar even if they are spelled differently (useful for spelling errors and name matching).

---

## 🔹 3. What is phonetic matching?

**Answer:**
It is a technique that compares words based on how they sound instead of how they are written.

---

## 🔹 4. Give examples where Soundex is useful.

**Answer:**

* Name matching (e.g., “Smith” and “Smyth”)
* Search engines
* Database record matching

---

## 🔹 5. What is the basic idea of Soundex?

**Answer:**
Convert a word into a code consisting of a letter and numbers representing similar sounding consonants.

---

## 🔹 6. How are letters grouped in Soundex?

**Answer:**
Letters with similar sounds are assigned the same numeric code (e.g., B, F, P, V → 1).

---

## 🔹 7. What happens to vowels in Soundex?

**Answer:**
Vowels are usually ignored (or treated as separators).

---

## 🔹 8. Why is the first letter kept unchanged?

**Answer:**
To preserve the initial sound of the word for better identification.

---

## 🔹 9. What is the standard length of a Soundex code?

**Answer:**
4 characters (1 letter + 3 digits).

---

## 🔹 10. What happens if the code is shorter than 4 characters?

**Answer:**
It is padded with zeros.

---

## 🔹 11. What happens if the code is longer than 4 characters?

**Answer:**
It is truncated to 4 characters.

---

## 🔹 12. Why are duplicate codes removed?

**Answer:**
To avoid redundancy when adjacent letters produce the same sound.

---

## 🔹 13. What is the role of consonants in Soundex?

**Answer:**
Consonants determine the numeric code based on pronunciation.

---

## 🔹 14. What are limitations of Soundex?

**Answer:**

* Not very accurate for all languages
* Different sounding words may get same code
* Limited to English-like names

---

## 🔹 15. What is approximate matching in IR?

**Answer:**
Matching similar words instead of exact matches.

---

## 🔹 16. Difference between Soundex and Edit Distance?

**Answer:**

* Soundex → based on pronunciation
* Edit Distance → based on character changes

---

## 🔹 17. What is indexing in IR?

**Answer:**
Organizing data to make searching faster.

---

## 🔹 18. How does Soundex help in indexing?

**Answer:**
It groups similar-sounding words under the same code.

---

## 🔹 19. What is normalization in this context?

**Answer:**
Converting text into a standard form (e.g., uppercase).

---

## 🔹 20. What is tokenization?

**Answer:**
Breaking text into individual words or tokens.

---

## 🔹 21. What is information retrieval system?

**Answer:**
A system that retrieves relevant information based on user queries.

---

## 🔹 22. What is fuzzy search?

**Answer:**
Searching for approximate matches instead of exact matches.

---

## 🔹 23. What is data matching?

**Answer:**
Comparing data to find similar or identical records.

---

## 🔹 24. What is phonetic encoding?

**Answer:**
Converting words into codes based on their sound.

---

## 🔹 25. What is the advantage of Soundex?

**Answer:**

* Simple
* Fast
* Useful for name matching

---

## 🔹 26. What is the disadvantage of Soundex?

**Answer:**

* Low accuracy for complex words
* Ignores spelling variations beyond sound

---

## 🔹 27. What is homophone?

**Answer:**
Words that sound the same but have different meanings (e.g., “right” and “write”).

---

## 🔹 28. How does Soundex handle homophones?

**Answer:**
It assigns them the same code.

---

## 🔹 29. What is data retrieval vs information retrieval?

**Answer:**

* Data retrieval → exact match
* Information retrieval → relevant match

---

## 🔹 30. What is search optimization?

**Answer:**
Improving search efficiency and accuracy.

---

## 🔹 31. What is a search query?

**Answer:**
Input given by the user to retrieve information.

---

## 🔹 32. What is relevance in IR?

**Answer:**
How well the retrieved data matches the query.

---

## 🔹 33. What is preprocessing in IR?

**Answer:**
Cleaning and preparing data before processing.

---

## 🔹 34. What is case folding?

**Answer:**
Converting all text to the same case (e.g., uppercase).

---

## 🔹 35. What is clustering in IR?

**Answer:**
Grouping similar items together.

---

## 🔹 36. What is classification in IR?

**Answer:**
Assigning data to predefined categories.

---

## 🔹 37. What is database matching?

**Answer:**
Matching records across databases.

---

## 🔹 38. What are real-world applications of Soundex?

**Answer:**

* Census data processing
* Contact search
* Library systems

---

## 🔹 39. What is ambiguity in IR?

**Answer:**
When a query has multiple meanings.

---

## 🔹 40. Why is phonetic matching important?

**Answer:**
Because users may not know the exact spelling but know how a word sounds.

---

## 🔥 Tip for Viva:

If examiner asks **“Explain Soundex in one line”**, say:
👉 *“Soundex is a phonetic algorithm that converts words into codes based on their pronunciation to enable approximate matching.”*

---

