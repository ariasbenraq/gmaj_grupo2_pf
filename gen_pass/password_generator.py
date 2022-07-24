import string
import random

mayu = list(string.ascii_uppercase)
minus = list(string.ascii_lowercase)
numeros = list(string.digits)
caracteres_especiales = list("+-%$&#")
caracteres = list(string.ascii_uppercase + string.ascii_lowercase + string.digits + "+-%$&#")
#ascii_letters considera letras mayusculas y minusculas
#string.digits considera numeros '0123456789'

def generador_pass():
    q1 = input("¿Desea ingresar la longitud de la contraseña? s/n:")
    
    if q1 == "s":
        length = int(input("ingrese la longitud: "))
    else:
        length = 16
        
    mayu2 = input("¿Desea que la contraseña tenga mayusculas? s/n:")
    minus2 = input("¿Desea que la contraseña tenga minusculas? s/n:")
    cespeciales = input("¿Desea que la contraseña contenga caracteres especiales? s/n:")
    
    
    password = []
        
    if mayu2 == "s":
        random.shuffle(mayu)
        for i in range(length):
            password.append(random.choice(mayu))
            
    if minus2 == "s":
        random.shuffle(minus)
        for i in range(length):
            password.append(random.choice(minus))
            
    if cespeciales == "s":
        random.shuffle(caracteres_especiales)
        for i in range(length):
            password.append(random.choice(caracteres_especiales))
    
    

    random.shuffle(password)

    print("".join(password))



generador_pass()