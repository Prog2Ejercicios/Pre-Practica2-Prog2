#Crear un programa que permita al usuario ingresar una lista de numeros. 
# De esa lista de numeros almacenar en otra lista los numeros impares.

#El programa debe de mostrar por pantalla la lista de numeros originales 
#y la lista de numeros impares.

#INICIO
list(range(100))

print("La lista es: ")

for i in range(100):
    print(" ",i)

print("La lista de los numeros impares es: ")

for i in range(100):  
    if i % 2 == 1:
        print(" ",i)
#FIN