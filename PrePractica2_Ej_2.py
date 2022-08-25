#Crear un programa que permita al usuario ingresar una lista de numeros. De esa lista de numeros almacenar en otra lista los numeros impares.

#El programa debe de mostrar por pantalla la lista de numeros originales y la lista de numeros impares.

#INICIO


lista = []

while (True):
       
    lista.append(int(input("Ingrese un numero: ")))
    if len(lista) == 6:
        break
    
print(lista)    

impares = []

for i in range(6):
    if lista[i] % 2 != 0:
        impares.append(lista[i])

print(impares)




#FIN