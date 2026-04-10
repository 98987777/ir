# -------------------- DATA --------------------
plays = {
    "Anthony and Cleopatra": "Anthony is there, Brutus is Caeser is with Cleopatra mercy worser.",  # Dictionary storing play names and their text
    "Julius Ceaser": "Anthony is there, Brutus is Caeser is but Calpurnia is.",  # Each play mapped to its content
    "The Tempest": "mercy worser",  # Short text for this play
    "Hamlet": "Caeser and Brutus are present with mercy and worser",  # Text containing keywords
    "Othello": "Caeser is present with mercy and worser",  # Another play text
    "Macbeth": "Anthony is there, Caeser, mercy."  # Another play text
}

words = ["Anthony", "Brutus", "Caeser", "Calpurnia", "Cleopatra", "mercy", "worser"]  # List of keywords to search

# -------------------- STEP 1: CREATE VECTOR MATRIX --------------------
vector_matrix = [[0 for _ in range(len(plays))] for _ in range(len(words))]  
# Create a 2D matrix initialized with 0 → rows = words, columns = plays

text_list = list(plays.values())  
# Extract all play texts into a list

for i in range(len(words)):  # Loop through each word
    for j in range(len(text_list)):  # Loop through each play text
        if words[i].lower() in text_list[j].lower():  # Check if word exists in play text (case insensitive)
            vector_matrix[i][j] = 1  # Mark presence with 1

print("Vector Matrix:")
for i in range(len(words)):  # Loop through words
    print(words[i], ":", vector_matrix[i])  # Print word with its presence vector

# -------------------- STEP 2: CONVERT TO BIT PATTERNS --------------------
vector_dict = {}  # Dictionary to store word → bit representation

for i in range(len(words)):  # Loop through each word
    bit_string = ""  # Initialize empty string for bits
    for bit in vector_matrix[i]:  # Loop through row values (0/1)
        bit_string += str(bit)  # Convert each bit to string and append
    vector_dict[words[i]] = int(bit_string, 2)  
    # Convert binary string to integer (base 2) and store

print("\nBit Representation:")
for k, v in vector_dict.items():  # Loop through dictionary
    print(k, ":", bin(v))  # Print word and its binary form

# -------------------- FUNCTION TO PROCESS QUERY --------------------
def process_query(query):
    q = query  # Store query in variable q

    # Fix common mistakes
    q = q.replace("Caesar", "Caeser")  # Replace spelling variations
    q = q.replace("Antony", "Anthony")  # Fix name spelling
    q = q.replace("Calpurni", "Calpurnia")  # Fix incomplete spelling

    # Replace words with numbers
    for word in words:  # Loop through all keywords
        if word in q:  # If word exists in query
            q = q.replace(word, str(vector_dict[word]))  
            # Replace word with its bit integer value

    # Replace logical operators
    q = q.replace("AND", "&").replace("and", "&")  # Replace AND with bitwise AND
    q = q.replace("OR", "|").replace("or", "|")  # Replace OR with bitwise OR
    q = q.replace("NOT", "~").replace("not", "~")  # Replace NOT with bitwise NOT

    print("\nConverted Query:", q)  # Show converted numeric query

    # Evaluate
    result = eval(q)  # Evaluate the expression (bitwise operations)

    # Convert to binary
    result_bin = bin(result)[2:].zfill(len(plays))  
    # Convert result to binary string, remove '0b', pad with zeros

    print("Result (Binary):", result_bin)  # Print binary result

    # Display result
    print("Matching Plays:")
    play_names = list(plays.keys())  # Get play names

    for i in range(len(result_bin)):  # Loop through binary result
        if result_bin[i] == '1':  # If bit is 1 → match found
            print("-", play_names[i])  # Print corresponding play name


# -------------------- USER INPUT --------------------
while True:  # Infinite loop to keep taking queries
    query = input("\nEnter query (or type EXIT to stop): ")  # Take user input

    if query.lower() == "exit":  # Check if user wants to exit
        break  # Stop loop

    print("\n====================================")
    print("Query:", query)  # Print entered query
    process_query(query)  # Call function to process query
