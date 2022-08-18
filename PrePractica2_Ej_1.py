#Crear un programa que permita ingresar una lista de numeros al usuario 
#y muestre por pantalla el maximo entre ambos numeros.

#Nota : Hacerlo con la función max(a,b) y luego con una comparación

#INICIO
print("Ingrese el primer número: ")
a = input()
print("Ingrese el segundo número: ")
b = input()

if a > b:
    print("El numero mayor es: ", a)
else:
    print("El número mayor es: ", b)

resultado2 = max(a,b)

print("El resultado con la función MAX es: ", resultado2)
#FIN