letters = input("Text to code> ")
key = 10  # secret code

for i in range(len(letters)):
    letter = letters[i]

    #print(letter)


    code = ord(letter)
    new_code = ord(letter) + key
    if 97 <= code <= 122:
        if new_code > 122:
            new_code = new_code - 26
    elif 65 <= code <= 90:  # Capital letter
        if new_code > 90:
            new_code = new_code - 26
    else:
        new_code = code

    new_letter = chr(new_code)
    print(new_letter, end="")
