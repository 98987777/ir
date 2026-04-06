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
