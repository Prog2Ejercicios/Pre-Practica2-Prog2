#Crear un programa que permita ingresar una lista de numeros al usuario y muestre por pantalla el maximo entre ambos numeros.

#Nota : Hacerlo con la función max(a,b) y luego con una comparación

#INICIO

num1 = input("Ingrese el primer numero: ")
num2 = input("Ingrese el segundo numero: ")

print("El numero mayor es: ", max(num1, num2))

if num1 < num2:
    print("El meayor es: " + str(num2))
else:    
    if num2 < num1:
        print("El mayor es: " + str(num1))


#FIN