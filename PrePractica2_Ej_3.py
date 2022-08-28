#Crear un programa que utilice la estructura try - catch. El usuario debe de ingresar dos numeros y mostrar por pantalla
#el resultado de la división entre ambos numeros. 

#En caso de que el divisor sea 0 utilizar la excepción ZeroDivisionError y mostrar el error por pantalla.


#INICIO
primer_num = int(input("Ingrese el primer numero: "))
segundo_num = int(input("Ingrese el segundo numero: "))

division = primer_num / segundo_num

try:
    print(division)
except ZeroDivisionError as exception:
    print(f"Ha ocurrido un error | {exception}")

#FIN