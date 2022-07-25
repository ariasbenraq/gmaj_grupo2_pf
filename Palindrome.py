def palindrome (palabra) :
palabra= palabra.lower (). replace('' , ' ')
palabra_reversa= ''.join(reversed(palabra))
return palabra==palabra_reversa 

ContadorPalindromos=0
Si_palindromo=0
No_palindromo=0
 
palabra = input ("Ingrese una palabra: ")
While  palabra != 'bye':
If Si_palindromo= Si_palindromo += 1
Else
No_palindromo= No_palindromo += 1

print ("La cantidad total de palabras ingresadas fue: " , ContadorPalindromos)
print ("La cantidad de palindromos fue: " , Si_palindromo)
print ("La cantidad de nl palindromos fue: " , No_palindromo)
