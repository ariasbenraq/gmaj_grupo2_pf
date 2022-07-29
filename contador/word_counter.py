#palabra clave para salir "adios"

import time
from funcion import filtro
from os import path

ciclo = 0
davar = 0
frase_1 = 0

while frase_1 != "adios":
    print()
    print("Ingresa una nueva frase: ")
    frase = input()
    word = frase.split()
    if not list(filter(filtro, word)):
        count = len(word)
        davar = davar + count
        ciclo = ciclo + 1
        directorio = path.dirname(path.abspath(__file__)) 
        archivo = path.join(directorio, "phrases.txt")
        with open("contador\phrases.txt", "a") as archivo:
            archivo.write(frase + "\n")

        print(f"Cantidad de frases: {ciclo}")
        print(f"cantidad de palabras: {davar}")
        print()
    
    else:
        print()
        print("Muchas gracias por compartir")

    
    frase_1 = list(filter(filtro, word))
    frase_1 ="".join(frase_1)
    
