#Crear un programa que utilice la estructura try - catch. El usuario debe de ingresar dos numeros y mostrar por pantalla
#el resultado de la división entre ambos numeros. 

#En caso de que el divisor sea 0 utilizar la excepción ZeroDivisionError y mostrar el error por pantalla.


#INICIO
print("Ingrese dos números")
print("Primer número:")
numero1 = float(input())
print("Segundo número:")
numero2 = float(input())
try:
    division = numero1/numero2
    print(f'El resultado de la división es: {division}')
except ZeroDivisionError:
    print("No se puede dividir por cero.")
#FIN