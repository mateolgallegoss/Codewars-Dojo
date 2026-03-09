# Complementary DNA #7 kyu
# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells
# and carries the "instructions" for the development and functioning of living organisms.
# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G".
# Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side.
# DNA strand is never empty or there is no DNA at all (again, except for Haskell).
# More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)
# Example: (input --> output)
# "ATTGC" --> "TAACG"
# "GTAT" --> "CATA"
# Strings, Fundamentals

from os import system
if system("clear") != 0: system("cls")

import string

entry = ""
def log_dna(entry):
    global dna
    entry = input('Introduzca uno de los lados del DNA registrado: ')
    system("cls")
    entry.upper
    alphabet_set = set(string.ascii_uppercase)
    aplhabet_set = [i for i in alphabet_set if i not in ["A", "C", "G", "T"]]
    if any(i in aplhabet_set for i in entry):
        entry = input('Introduzca uno de los lados del DNA registrado: ')
        system("cls")
    else:
        entry.upper
        print(f'El primer lado de DNA es: {entry}')
    dna = entry

def dna_strand(dna):  # For Codewars, set first word function with mayus, like: DNA_strand
    chain = list(dna)
    for i in range(len(chain)):
        if chain[ i] == "A":
            chain[i] = "T"
        elif chain[i] == "T":
            chain[i] = "A"
        elif chain[i] == "C":
            chain[i] = "G"
        elif chain[i] == "G":
            chain[i] = "C"
    dna_1 = ''.join(chain)
    print(f'El otro lado del DNA es: {dna_1}')  #For Codewars, set only: return dna_1
    
log_dna(entry)
dna_strand(dna)