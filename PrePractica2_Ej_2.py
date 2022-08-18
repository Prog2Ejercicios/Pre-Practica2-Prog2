#Crear un programa que permita al usuario ingresar una lista de numeros. De esa lista de numeros almacenar en otra lista los numeros impares.

#El programa debe de mostrar por pantalla la lista de numeros originales y la lista de numeros impares.

#INICIO
lista=[]
lista_impar=[]
while True:
    print("Ingrese un numero distinto de 0: ")
    num=int(input())
    if num!=0:
        lista.append(num)
    else:
        break
for num in lista:
    if num %2!=0:
        lista_impar.append(num)


print("La lista es: " + str(lista))
print("La lista impar es " + str(lista_impar))

#FIN