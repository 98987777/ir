# PageRank for 3 pages: A, B, C
# Using formula: PR(A) = (1-d) + d * Σ ( PR(Bi) / C(Bi) )

d = 0.85  # damping factor

# Outgoing links from each page
links = {
    'A': ['B', 'C'],  # A -> B, C
    'B': ['C'],       # B -> C
    'C': ['A']        # C -> A
}

pages = list(links.keys())

# Compute outdegree C(B) = number of outlinks from each page
outdegree = {page: len(links[page]) for page in pages}

# Initial PageRank values (0th iteration)
pagerank = {page: 1.0 for page in pages}

print("Iteration 0:")
for p in pages:
    print(f"PR({p}) = {pagerank[p]:.6f}")

# Perform 3 iterations (1, 2, 3)
for it in range(1, 3):
    new_pagerank = {}

    for p in pages:
        # Sum over all pages q that link TO p
        incoming_sum = 0.0

        for q in pages:
            if p in links[q]:  # if q -> p
                incoming_sum += pagerank[q] / outdegree[q]

        # Apply PageRank formula
        new_pagerank[p] = (1 - d) + d * incoming_sum

    pagerank = new_pagerank  # update PR for next iteration

    print(f"\nIteration {it}:")
    for p in pages:
        print(f"PR({p}) = {pagerank[p]:.6f}")




For Viva -


# 📘 IR Practical Viva Questions (PageRank Algorithm)

---

## 🔹 1. What is PageRank?

**Answer:**
PageRank is an algorithm used to rank web pages based on their importance using link structure.

---

## 🔹 2. Who developed PageRank?

**Answer:**
It was developed by Larry Page and Sergey Brin.

---

## 🔹 3. What is the basic idea behind PageRank?

**Answer:**
A page is important if it is linked by other important pages.

---

## 🔹 4. What is a hyperlink in PageRank?

**Answer:**
A hyperlink is a connection from one webpage to another.

---

## 🔹 5. What is the damping factor?

**Answer:**
It is a probability (usually 0.85) representing the chance that a user continues clicking links.

---

## 🔹 6. Why is the damping factor used?

**Answer:**
To model random user behavior and avoid infinite loops in ranking.

---

## 🔹 7. What is the PageRank formula?

**Answer:**
👉 PR(A) = (1 - d) + d × Σ (PR(B) / C(B))

---

## 🔹 8. What does PR(A) represent?

**Answer:**
The importance (rank) of page A.

---

## 🔹 9. What is C(B)?

**Answer:**
The number of outgoing links from page B.

---

## 🔹 10. What are incoming links?

**Answer:**
Links from other pages pointing to a page.

---

## 🔹 11. What are outgoing links?

**Answer:**
Links from a page pointing to other pages.

---

## 🔹 12. Why are incoming links important?

**Answer:**
They increase the importance (rank) of a page.

---

## 🔹 13. What is iteration in PageRank?

**Answer:**
Repeated calculation of PageRank values until they stabilize.

---

## 🔹 14. What is convergence?

**Answer:**
When PageRank values stop changing significantly after iterations.

---

## 🔹 15. What is the initial PageRank value?

**Answer:**
Usually all pages start with equal rank (e.g., 1).

---

## 🔹 16. What is a dangling node?

**Answer:**
A page with no outgoing links.

---

## 🔹 17. How are dangling nodes handled?

**Answer:**
Their rank is distributed equally among all pages.

---

## 🔹 18. What is the role of normalization in PageRank?

**Answer:**
To ensure total rank remains consistent.

---

## 🔹 19. What is web graph?

**Answer:**
A graph where pages are nodes and links are edges.

---

## 🔹 20. What is link analysis?

**Answer:**
Analyzing links between pages to determine importance.

---

## 🔹 21. What is authority in PageRank?

**Answer:**
A page with many important incoming links.

---

## 🔹 22. What is hub in IR?

**Answer:**
A page that links to many important pages.

---

## 🔹 23. Difference between hub and authority?

**Answer:**

* Hub → links to others
* Authority → linked by others

---

## 🔹 24. What is the importance of PageRank in IR?

**Answer:**
It improves search result ranking based on page importance.

---

## 🔹 25. What is relevance vs importance?

**Answer:**

* Relevance → matches query
* Importance → overall popularity

---

## 🔹 26. What is the limitation of PageRank?

**Answer:**

* Ignores content relevance
* Can be manipulated by link spam

---

## 🔹 27. What is link spam?

**Answer:**
Artificial links created to increase ranking.

---

## 🔹 28. What is SEO?

**Answer:**
Search Engine Optimization — improving website ranking.

---

## 🔹 29. What is the role of PageRank in search engines like Google?

**Answer:**
It helps rank webpages based on importance along with other factors.

---

## 🔹 30. What is random surfer model?

**Answer:**
A model where a user randomly clicks links or jumps to any page.

---

## 🔹 31. Why is PageRank iterative?

**Answer:**
Because ranks depend on other pages' ranks.

---

## 🔹 32. What is graph theory in PageRank?

**Answer:**
Mathematical representation of web pages and links.

---

## 🔹 33. What is adjacency in web graph?

**Answer:**
Connection between pages through links.

---

## 🔹 34. What is scalability in PageRank?

**Answer:**
Ability to handle billions of web pages efficiently.

---

## 🔹 35. What is matrix representation of PageRank?

**Answer:**
Using matrices to represent link structure and compute ranks.

---

## 🔹 36. What is transition probability?

**Answer:**
Probability of moving from one page to another.

---

## 🔹 37. What is steady-state distribution?

**Answer:**
Final stable PageRank values.

---

## 🔹 38. What is eigenvector in PageRank?

**Answer:**
Mathematical representation used to compute ranking.

---

## 🔹 39. What is real-world application of PageRank?

**Answer:**

* Search engines
* Social network analysis
* Recommendation systems

---

## 🔹 40. Why is PageRank important?

**Answer:**
Because it helps rank web pages effectively based on their importance.

---

## 🔥 Tip for Viva:

If examiner asks **“Explain PageRank in one line”**, say:
👉 *“PageRank is a link analysis algorithm that ranks web pages based on the number and quality of links pointing to them.”*

---


