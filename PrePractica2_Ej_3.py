#Crear un programa que utilice la estructura try - catch. El usuario debe de ingresar dos numeros y mostrar por pantalla
#el resultado de la división entre ambos numeros. 

#En caso de que el divisor sea 0 utilizar la excepción ZeroDivisionError y mostrar el error por pantalla.


#INICIO

#FIN
try:
    print("Ingrese un numero: ")
    num1 = int(input())

    print("Ingrese otro numero: ")
    num2 = int(input())

    resultado = num1 / num2

except ZeroDivisionError as exception:
 print(f"Ha ocurrido un error | {exception} ")

print(f"Resultado de la division= {resultado}")