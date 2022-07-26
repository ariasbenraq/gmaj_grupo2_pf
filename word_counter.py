import re
frase = input("escriba una frase: ").strip()
espacios = ''.join(re.findall("\s+", frase))
print("El nombre {}, tiene {} letras".format(frase, len(frase) - len(espacios)))

word = frase.split()
count = len(word)
ciclo = 1
print (f" y la frase tiene {count} palabras")

archivo = open ("phrases.txt", "w")
archivo.write (frase + '\n'),
archivo.close()
print ("si quiere salir del contador escriba THE END ")
Salir_del_contador= input("quiere salir del contador de palabras?")

if Salir_del_contador == "the end" or "THE END":
    print("el contador de palabras termino")
else:
    print(" sigue en el contador de palabras")