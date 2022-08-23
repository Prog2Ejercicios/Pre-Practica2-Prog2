#Crear un programa que permita ingresar una lista de numeros al usuario y muestre por pantalla el maximo entre ambos numeros.

#Nota : Hacerlo con la función max(a,b) y luego con una comparación

#INICIO
a=int(input("Escribe un numero: "))
b=int(input("Escribe otro numero: "))
print("El mayor es: " + str(max(a,b)))

if a>b: 
    print("El mayor es: " +str (a))
else:
    print("El mayor es: " +str (b))

#FIN