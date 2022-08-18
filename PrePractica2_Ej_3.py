#Crear un programa que utilice la estructura try - catch. El usuario debe de ingresar dos numeros y 
# mostrar por pantalla el resultado de la división entre ambos numeros. 

#En caso de que el divisor sea 0 utilizar la excepción ZeroDivisionError y mostrar el error por pantalla.


#INICIO
try:
    print("Ingrese ambos numeros a dividir: ")
    n1 = int(input())
    n2 = int(input())

    division = n1/n2
    print("La division de ambos numeros es: " + str(division))
except ZeroDivisionError:
    print("Error de division, no se divide por 0")
#FIN