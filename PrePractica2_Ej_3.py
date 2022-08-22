#Crear un programa que utilice la estructura try - catch. El usuario debe de ingresar dos numeros y mostrar por pantalla
#el resultado de la división entre ambos numeros. 

#En caso de que el divisor sea 0 utilizar la excepción ZeroDivisionError y mostrar el error por pantalla.


#INICIO
from logging import exception

print("Ingrese dos números para una división:")
num1=float(input())
num2=float(input())
try:
    resultado=num1/num2
    print("El resultado de la división es:", resultado)
except ZeroDivisionError as exception:
    print(f"No se puede dividir por 0 | {exception}")
#FIN