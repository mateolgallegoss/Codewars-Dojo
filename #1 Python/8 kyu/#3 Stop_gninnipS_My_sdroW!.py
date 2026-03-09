# Stop gninnipS My sdroW! #6 kyu
# Write a function that takes in a string of one or more words, and returns the same string, 
# but with all words that have five or more letters reversed (just like the name of this kata).
# Strings passed in will consist of only letters and spaces. 
# Spaces will be included only when more than one word is present.
# Examples:
# "Hey fellow warriors"  --> "Hey wollef sroirraw" 
# "This is a test        --> "This is a test" 
# "This is another test" --> "This is rehtona test"
# Strings, Algorithms

from os import system
if system("clear") != 0: system("cls")

text = ""
def log_text(text):
    global sentence
    text = input('Introduzca un texto; no existe límite de palabras, pero al menos debe ser un texto de 5 letras: ')
    system("cls")
    while len(text) < 5:
        text = input('Introduzca un texto; no existe límite de palabras, pero al menos debe ser un texto de 5 letras: ')
        system("cls")
    else:
        print(f'El texto ingresado es: {text}')
    sentence = text     

def spin_words(sentence):
    words = sentence.split()
    for i in range(len(words)):
        if len(words[i]) >= 5:
            words[i] = words[i][::-1]
    new_sentence = ' '.join(words)
    print(f'La oración con las letras en reversa es: {new_sentence}')  # For Codewars, reeplace line33 with the codeline: return new_sentence
    
log_text(text)
spin_words(sentence)
