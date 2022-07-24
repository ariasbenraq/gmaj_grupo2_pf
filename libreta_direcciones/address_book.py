import csv
from datetime import date
from os import path
import uuid


print("ingrese su nombre:")
name = input()

print("ingrese su dirección:")
address = input()

print("ingrese su teléfono:")
num = input()

fecha_actual = date.today()

# Para el campo ID puede emplear la libreria integrada de python 'uuid'
identificador = uuid.uuid4()

reg_date = fecha_actual.strftime('%d/%m/%Y')
lista = [ ]
lista.append(name)
lista.append(address)
lista.append(num)
lista.append(identificador)
lista.append(reg_date)

# Utilicé el modulo "path" para fijar de forma absoluta el directorio donde se encuentra el archivo .csv.
# No es común pero ayudó a encontrarlo dentro de la misma carpeta.
directorio = path.dirname(path.abspath(__file__)) 
archivo = path.join(directorio, "addresses.csv")
with open(archivo, "a") as cvfile:
    writer = csv.writer(cvfile)
    writer.writerow(lista)

print(f"Nombre: {name}")
print(f"Dirección: {num}")
print(f"Fecha de registro: {fecha_actual}")
print(f"ID: {identificador}")   