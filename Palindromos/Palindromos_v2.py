from fun_v2 import runPalindromeCheck
from fun_v2 import d_count
from fun_v2 import filtro
import time

count_sip = 0
count_nop = 0
word = 0
shir = 0


while shir != "shalom":
    davar = str(input("\nIngrese una palabra, para verificar si es palindromo \n(No escriba shalom): "))
    contar = davar
    contar = contar.split()
    if not list(filter(filtro, contar)):

        reversedList = davar[::-1]
        if reversedList == davar:
            si_p = "El texto ingresdo es un palindromo"
            count_sip += 1
        else: 
             no_p = "El texto ingresado no es un palindromo"
             count_nop += 1

        palin_check = runPalindromeCheck(davar)
        contar_1 = d_count(davar)
        time.sleep(0.5)
        print()
        print(palin_check)   
        print(f"Cantidad de palindromos: {count_sip}")
        print(f"Cantidad de no palindromos: {count_nop}")
        print(f"Cantidad de palabras ingresadas: {contar_1}")
        
    else:
        print("\nShalom lach eretz nehederet \nAvdech hadal nosei lach shir mizmor\nGam im leitim noded ani al derech - \nMah tov lindod ach tov yoter lachzor")
        print("Yehoram Gaon")
        print("Muchas gracias")

    
    shir = list(filter(filtro, contar))
    shir = "".join(shir)
