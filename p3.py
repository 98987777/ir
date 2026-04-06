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
