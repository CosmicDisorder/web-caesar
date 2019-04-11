from helpers import alphabet_position, rotate_character
import string
alphabet = string.ascii_lowercase

def encrypt(text, rot):
    new_text = ''
    for char in text:
        new_text += rotate_character(char, rot)
    return new_text

def main():
    from sys import argv, exit
    if argv[1].isdigit():
        text = input("Type a message:\n")
        print(encrypt(text,int(argv[1])))
    else:
        print("usage: python caesar.py n")
        exit()

if __name__ == "__main__":
    main()