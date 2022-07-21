import string
import random

letras = list(string.ascii_letters)
numeros = list(string.digits)
caracteres_especiales = list("+-%$&#")
caracteres = list(string.ascii_letters + string.digits + "+-%$&#")
#ascii_letters considera letras mayusculas y minusculas
#string.digits considera numeros '0123456789'

def generador_pass():
    length = int(input("Ingrese el tamaño de la contraseña: "))
    letras_count = int(input("Ingrese la cantidad de letras: "))
    numeros_count = int(input("Ingrese la cantidad de numeros: "))
    caracteres_especiales_count = int(input("Ingrese la cantidad de caracteres especiales: "))
    caracteres_count = letras_count + numeros_count + caracteres_especiales_count

    
        
    if caracteres_count > length:
        print("Los caracters totales son mayores a la longitud ingresada")
        return
    
    

    password = []
    
    for i in range(letras_count):
        password.append(random.choice(letras))

    for i in range(numeros_count):
        password.append(random.choice(numeros))

    for i in range(caracteres_especiales_count):
        password.append(random.choice(caracteres_especiales))

    if caracteres_count < length:
        random.shuffle(caracteres)
        for i in range(length - caracteres_count):
        	password.append(random.choice(caracteres))

    random.shuffle(password)

    print("".join(password))



generador_pass()
