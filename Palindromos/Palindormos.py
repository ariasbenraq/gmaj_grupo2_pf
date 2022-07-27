from time import time
from mid_funciones import count_word
from mid_funciones import main
import time
        
ciclo = 0
word = 1

while word != "n":
    
    ciclo += 1
    word = str(input("\nIngrese una palabra, frase u oración \npara verificar si es palindromo: ")) 
    main(word)
    count_word(word)
    print(f"Cantidad de frases: {ciclo}")

    print("¿Desea evaluar otra frase o palabra? (s/n)")
    word = input()

else:
    print("Muchas gracias por compartir")
    time.sleep(1)
    print("Hasta pronto")
