import time
import random

f = open("englishdict.txt", "r")

words = f.read()
words = words.lower()
words = words.split()


def encrypt(text, key):
    key = key % 26
    arr = []
    orded = []
    enc = []
    text = text.lower()
    for letter in text:
        arr.append(letter)
    for letter in arr:
        ordletter = ord(letter)
        if ord("a") <= ordletter <= ord("z"):
            ordletter += key
            if ordletter > ord("z"):
                ordletter -= 26
        orded.append(ordletter)
    for number in orded:
        enc.append(chr(number))
    return "".join(enc)


def decrypt(text, key):
    key = key % 26
    arr = []
    orded = []
    enc = []
    text = text.lower()
    for letter in text:
        arr.append(letter)
    for letter in arr:
        ordletter = ord(letter)
        if ord("a") <= ordletter <= ord("z"):
            ordletter -= key
            if ordletter < ord("a"):
                ordletter += 26
        orded.append(ordletter)
    for number in orded:
        enc.append(chr(number))
    return "".join(enc)


def crack(text):
    possible = []
    start = time.clock()
    for i in range(0, 26):
        possible.append(decrypt(text, i))

    startingPunctuation = "(&\"'/#{["
    endingPunctuation = "),./:;}]\"'"
    for candidate in possible:
        a = candidate.split()
        matches = 0
        length = len(a)
        for word in a:
            while word[0] in startingPunctuation:
                word = word[1:]
            while word[-1] in endingPunctuation:
                word = word[:-1]
            if word in words:
                matches += 1

        if (matches / length) > 0.5:
            print(matches, "/", length, "words found in the dictionary")
            print("Caesar shifted by", possible.index(candidate), "places.")
            end = time.clock()
            print("Cracking took", end - start, "seconds.")
            return candidate
    return "Text was not caesar ciphered or contained too many spelling errors or unrecognised words."


def bruteforce(text):
    for i in range(1, 26):
        print(decrypt(text, i))


def choice():
    choice = input("Choose action: (e)ncrypt, (r)andom encrypt, (d)ecrypt or (c)rack? ")
    q = choice[0]

    if q == "e":
        text = input("Enter text to encrypt: ")
        key = int(input("Enter key: "))
        print(encrypt(text, key))
        print()
        again()

    elif q == "r":
        text = input("Enter text to encrypt: ")
        key = random.randint(0, 25)
        print(encrypt(text, key))
        print()
        again()

    elif q == "d":
        text = input("Enter text to decrypt: ")
        key = int(input("Enter key: "))
        print(decrypt(text, key))
        print()
        again()

    elif q == "c":
        text = input("Enter text to crack: ")
        print(crack(text))
        print()
        again()

    else:
        print("Option not recognised.")
        print()
        choice()


def again():
    decision = input("Another (y/n): ")
    if decision[0] == "y" or decision[0] == "Y":
        choice()
    else:
        return


choice()
