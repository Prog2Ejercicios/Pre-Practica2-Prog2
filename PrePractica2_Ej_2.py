#Crear un programa que permita al usuario ingresar una lista de numeros. De esa lista de numeros almacenar en otra lista los numeros impares.

#El programa debe de mostrar por pantalla la lista de numeros originales y la lista de numeros impares.

#INICIO

#FIN
lista0 = []
listaImp = []

print("Ingrese 7 numeros")

for i in range(7):
    lista0.append(int(input()))

    if (lista0[i] % 2 != 0):
        listaImp.append(lista0[i])

print("Lista original: " + str(lista0))
print("Lista Impares: " + str(listaImp))