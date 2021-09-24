def encrypt(text, key):
    result = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    text = text.lower()
    for letter in text:
        if letter == " ":
            result += " "
            continue
        index = alphabet.index(letter)
        result += alphabet[index+key if index+key < 26 else index+key-26]
    return result

def decrypt(text, key):
    result=""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    text = text.lower()
    for letter in text:
        if letter == " ":
            result += " "
            continue
        index = alphabet.index(letter)
        result += alphabet[index-key if index-key > 0 else index-key+26]
    return result