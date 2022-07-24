#palabra clave para salir "adios"

from pickle import TRUE
import time
from funcion import filtro
from os import path




print("Ingresa una frase: ")
frase = input()
word = frase.split()
count = len(word)
ciclo = 1
word_trick = ["adios"]

directorio = path.dirname(path.abspath(__file__)) 
archivo = path.join(directorio, "phrases.txt")
with open("contador\phrases.txt", "a") as archivo:
    archivo.write(frase + "\n")

print(f"Cantidad de frases: {ciclo}")
print(f"cantidad de palabras: {count}")

frase_1 = list(filter(filtro, word))
frase_1 ="".join(frase_1)

while frase_1 != "adios":
    print()
    print("Ingresa una nueva frase: ")
    frase = input()
    word = frase.split()
    count = len(word)
    ciclo = ciclo + 1
    directorio = path.dirname(path.abspath(__file__)) 
    archivo = path.join(directorio, "phrases.txt")
    with open("contador\phrases.txt", "a") as archivo:
        archivo.write(frase + "\n")

    print(f"Cantidad de frases: {ciclo}")
    print(f"cantidad de palabras: {count}")
    print()
    
    frase_1 = list(filter(filtro, word))
    
    
    frase_1 ="".join(frase_1)
    

   

else:
    print("Muchas gracias por compartir estas frases")
    time.sleep(1)
    print("Hasta pronto")
