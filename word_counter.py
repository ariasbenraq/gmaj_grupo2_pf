print ("BIENVENIDOS AL CONTADOR DE PALABRAS DEL GRUPO 2!!!!")

frase = 0
palabras = 0

hola = True

while hola:
    Frase= input("ingrese una frase para contar y si quiere salir del contador de palabras escriba abra cadabra: ")
    
    archivo = open ("phrases.txt", "a")
    archivo.write (Frase + '\n'),
    archivo.close()

    
    if Frase == "abra cadabra":
    
        print("gracias por esatr en el contador de palabras del grupo 2 ")
    
        hola = False
    
    else:
    
        frase = frase + 1 
    
        palabras = palabras + len(Frase.split(" "))
        
        print (f"tenes {frase} frases")
    
        print(f"y {palabras} palabras")
