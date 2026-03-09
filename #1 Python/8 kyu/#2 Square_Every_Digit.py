# Square Every Digit #7 kyu
# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)
# Example #2: An input of 765 will/should return 493625 because 7-2 is 49, 6-2 is 36, and 5-2 is 25. (49-36-25)
# Note: The function accepts an integer and returns an integer.
# Happy Coding!
# Mathematics, Fundamentals

from os import system
if system("clear") != 0: system("cls")

inicial = 0
def log_num(inicial):
    global num
    inicial = input('Introduzca un número; no existe límite de cifras creciente pero al menos deben ser tres dígitos en el número: ')
    system("cls")
    while len(inicial) < 3:
        inicial = input('Introduzca un número; no existe límite de cifras creciente pero al menos deben ser tres dígitos en el número: ')
        system("cls")
    else:
        print(f'El número introducido es: {inicial}')
    num = inicial        
def concac_squares(num):    
    digits = [n for n in str(num)]
    square = ""
    for i in range(len(digits)):
        digits[i] = str(int(digits[i]) ** 2)
        square += digits[i]   
    print(f'La concatenación del cuadrado de los dígitos es: {square}')  # For Codewars reeplace line29 to return(int(square))
        
log_num(inicial)
concac_squares(num)