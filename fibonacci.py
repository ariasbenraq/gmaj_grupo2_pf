print ("Gracias por utilizar este programa disenado por")
print ("alumnos de GMACJ - Curso de Programacion PYTHON")
print ("Tema : Sucesion de FIBONACCI")
print ("****************************")
final = int (input ( "Ingrese numero entero mayor que 0 : "))
    
while final < 1 :
    print ("Numero invalido - Por favor reingrese ")
    final = int (input ( "Ingrese numero entero mayor que 0 : "))
num1=1
num2=1
if final==1:
    print('1')
elif final==2:
    print('1','1')
else:
    print(num1)
    print(num2)
    for i in range(final-2):
        total = num1 + num2
        num2=num1
        num1= total
        print(total)
