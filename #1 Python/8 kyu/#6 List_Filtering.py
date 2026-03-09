'''
#List Filtering #7 kyu
In this kata you will create a function that takes a list of non-negative integers and strings
and returns a new list with the strings filtered out.
#Example
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
ListsFilteringData StructuresFundamentals
'''

from os import system
if system("clear") != 0: system("cls")

def log_list():
    global list_0

    entry = input('Introduzca una lista con mínimo 3 elementos (solo se admiten enteros positivos o texto): ')
    system("cls")
    entry = entry.split()

    if len(entry) < 3:
        entry = input('Introduzca una lista con mínimo 3 elementos (solo se admiten enteros positivos o texto): ')
        system("cls")
        entry = entry.split()
    list_0 = []

    for element in entry:
        try:
            num = int(element)
            if num < 0:
                print("Error: solo enteros positivos.")
                return
            list_0.append(num)
        except:
            list_0.append(element)
    print(f'La lista válida es: {list_0}')

def filter_list(list_0):  # For Codewars, reeplace list_0 to: l
    
    filtered_list = [i for i in list_0 if not isinstance(i, str)]  # For Codewards, 'reeplace filtered_list =' with: return 
    print(f'La lista filtrada solo con enteros positivos es: {filtered_list}')  #For Codewards, remove this codeline
    
log_list()
filter_list(list_0)