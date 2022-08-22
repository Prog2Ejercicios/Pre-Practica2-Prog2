#Crear un programa que permita al usuario ingresar una lista de numeros. De esa lista de numeros almacenar en otra lista los numeros impares.

#El programa debe de mostrar por pantalla la lista de numeros originales y la lista de numeros impares.

#INICIO
lista=[]
listaImpares=[]
print("Ingrese varios números enteros, para finalizar presione 0.")
while True:
    print("Ingresar número:")
    numero=int(input())
    if numero!=0:
        lista.append(numero)
        if numero%2!=0:
           listaImpares.append(numero)
    else:
        break
print("La lista de números originales es:")
print(lista)
print("La lista de números impares es:")
print(listaImpares)
#FIN