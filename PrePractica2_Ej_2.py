#Crear un programa que permita al usuario ingresar una lista de numeros. De esa lista de numeros almacenar en otra lista los numeros impares.

#El programa debe de mostrar por pantalla la lista de numeros originales y la lista de numeros impares.

#INICIO
print("Ingrese tamaño de la lista:")
tam=int(input())
print("Ingrese los valores en números enteros:")
lista=[]
lista_impar=[]

while len(lista)!=tam:
    num=int(input())
    lista.append(num)
    if num%2!=0:
        lista_impar.append(num)

print("Lista original:" ,lista)
print("Lista de impares:", lista_impar)
#FIN