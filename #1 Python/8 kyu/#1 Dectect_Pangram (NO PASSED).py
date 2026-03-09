from os import system
if system("clear") != 0: system("cls")

import string

def detect_pangram(pangram):
    pangram_lower = pangram.lower()
    alphabet_set = set(string.ascii_lowercase)
    pangram_set = set(pangram_lower)
    if alphabet_set.issubset(pangram_set):
        print('This phrase:')
        print(pangram)
        print('is a pangram.')
        return True
    else:
        missing = alphabet_set - pangram_set
        print('This phrase:')
        print(pangram)
        print('is not a pangram.')
        print('Missing letters:', sorted(missing))
        return False

pangram = input("Please, send a text to check if it's a pangram: ")
system("cls")
detect_pangram(pangram)