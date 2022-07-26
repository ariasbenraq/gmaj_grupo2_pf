frase = input("Ingrese una frase: ")
count=0
for j in frase:
  if j in "abcdefghijklmnñopqrstuvwxyz" or "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ":
      count+=1 
      count = len("")
print("la frase {}, tiene {} letras".format(frase,count))

word = frase.split()
count = len(word)
ciclo = 1
print (f" y la frase tiene {count} palabras")

archivo = open ("phrases.txt", "w")
archivo.write (frase + '\n')
archivo.close()
print ("si quiere salir del contador escriba THE END ")
Salir_del_contador= input("quiere salir del contador de palabras?")

if Salir_del_contador == "the end" or "THE END":
    print("el contador de palabras termino")
else:
    print(" sigue en el contador de palabras")