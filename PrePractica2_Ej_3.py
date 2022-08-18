#Crear un programa que utilice la estructura try - catch. El usuario debe de ingresar dos numeros y mostrar por pantalla
#el resultado de la división entre ambos numeros. 

#En caso de que el divisor sea 0 utilizar la excepción ZeroDivisionError y mostrar el error por pantalla.


#INICIO

print("Ingrese dos números")
division = 0
n1=int(input())
n2=int(input())

try:
    division = n1 / n2
except ZeroDivisionError as exception:
    print(f"Ocurrió un error | {exception}")

if division != 0:
    print("La division es: ", division)

#FIN