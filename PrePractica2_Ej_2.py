#Crear un programa que permita al usuario ingresar una lista de numeros. De esa 
# lista de numeros almacenar en otra lista los numeros impares.

#El programa debe de mostrar por pantalla la lista de numeros originales y la lista de numeros impares.
   
#INICIO
print("Ingrese 4 numeros")
lista = []
listaImpar = []
for i in range(4):
    lista.append(int(input()))

    if (lista[i] % 2 != 0):
        listaImpar.append(lista[i])


print("Lista par original: " + str(lista))
print("Lista impar copia: " + str(listaImpar)) 

#FIN