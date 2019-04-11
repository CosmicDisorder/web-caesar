import string
alphabet = string.ascii_lowercase

def alphabet_position(letter):
    letter = letter.lower()
    return alphabet.index(letter)

def rotate_character(char, rot):
    if char not in string.ascii_letters:
        return char
    new_index = alphabet_position(char) + rot
    new_char = alphabet[new_index%26]
    if char.isupper():
        return new_char.upper()
    else:
        return alphabet[new_index%26]
