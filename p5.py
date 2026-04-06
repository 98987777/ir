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
