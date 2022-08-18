#Crear un programa que utilice la estructura try - catch. El usuario debe de ingresar dos numeros y mostrar por pantalla
#el resultado de la división entre ambos numeros. 

#En caso de que el divisor sea 0 utilizar la excepción ZeroDivisionError y mostrar el error por pantalla.


#INICIO
from logging import exception


a=int(input("Escribe un numero: "))
b=int(input("Escribe otro numero: "))
try:
    division=a/b
except ZeroDivisionError:
        print(f"No puede dividirse por 0 | {exception}")
        division=0
else: 
    print("La division es: " + str(division))
#FIN