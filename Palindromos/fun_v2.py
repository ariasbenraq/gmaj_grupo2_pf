def d_count(d):
    d = d.split()
    d_len = len(d)
    return d_len

def runPalindromeCheck(straightList):
    reversedList = straightList[::-1] 
    if reversedList == straightList: 
        return "El texto ingresdo es un palindromo" 
    else: 
        return "El texto ingresado no es un palindromo" 

def p_count(p):
    si_palindromo = 0
    no_palindromo = 0

    if si_palindromo == "El texto ingresdo es un palindromo":
        si_palindromo += 1
    elif no_palindromo == "El texto ingresado no es un palindromo":
        no_palindromo += 1

def filtro(x):
    if x == "shalom":
        return "shalom"


    
