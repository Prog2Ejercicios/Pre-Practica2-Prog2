#Crear un programa que permita al usuario ingresar una lista de numeros. De esa lista de numeros almacenar en otra lista los numeros impares.

#El programa debe de mostrar por pantalla la lista de numeros originales y la lista de numeros impares.

#INICIO

listaOriginal = []
listaImpar = []

while True:
    print("Ingrese un numero distinto de cero ")
    valor = int(input())
    if valor != 0:
        listaOriginal.append(valor)
    else:
        break

for numero in listaOriginal:
    if numero % 2 != 0:
        listaImpar.append(numero)
    
       
print(listaOriginal)
print(listaImpar)

#FIN