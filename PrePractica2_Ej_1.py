#Crear un programa que permita ingresar una lista de numeros al usuario y muestre por pantalla el maximo entre ambos numeros.

#Nota : Hacerlo con la función max(a,b) y luego con una comparación

#INICIO

print("Ingrese el primero numero")
n1=int(input())
print("Ingrese el segundo numero")
n2=int(input())

# print("El máximo número es: ", max(n1,n2))

if n1 > n2:
    print("El mayor numero es:", n1)
elif n2 > n1:
    print("El mayor numero es:", n2)

#FIN