'''
Reverse words #7 kyu
Complete the function that accepts a string parameter, and reverses each word in the string. 
All spaces in the string should be retained.
Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
StringsFundamentals
'''

from os import system
if system("clear") != 0: system("cls")

entry = ""
def log_text(entry):
    global text
    entry = input('Introduzca un texto, mínimo de 10 letras: ')
    system("cls")
    if len(entry) < 10:
        entry = input('Introduzca un texto, mínimo de 10 letras: ')
        system("cls")
    else:
        print(f'El texto ingresado es: {entry}')
    text = entry
    
def reverse_words(text):
    words = text.split(" ")
    for i in range(len(words)):
        words[i] = words[i][::-1]
    inverse_text = ' '.join(words)
    print(f'La oración con las letras en reversa es: {inverse_text}')  # For Codewars, reeplace with: return inverse_text
    
log_text(entry)
reverse_words(text)