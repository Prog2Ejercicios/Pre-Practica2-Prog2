#Crear un programa que permita ingresar una lista de numeros al usuario y muestre por pantalla el maximo entre ambos numeros.

#Nota : Hacerlo con la función max(a,b) y luego con una comparación

#INICIO


#FIN
print("Ingrese un numero")
n1=int(input())
print("Ingrese otro numero")
n2=int(input())

print("Mayor por funcion: ", max(n1,n2))

if n1 > n2:
    print("Mayor por if:", n1)
elif n2 > n1:
    print("Mayor por if:", n2)