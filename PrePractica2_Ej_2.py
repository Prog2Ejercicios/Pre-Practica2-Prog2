#Crear un programa que permita al usuario ingresar una lista de numeros. De esa lista de numeros almacenar en otra lista los numeros impares.

#El programa debe de mostrar por pantalla la lista de numeros originales y la lista de numeros impares.

#INICIO
from ast import Num


lista=[]
lista_impar=[]
while True:
    print("Ingrese un numero distinto de cero: ")
    Num=int(input())
    if  Num!=0:
        lista.append(Num)
    else:
        break
for Num in lista:
    if Num %2!=0:
        lista_impar.append(Num)
print("La lista es: " + str(lista)) 
print("La lista impar  es: " + str(lista_impar)) 
#FIN