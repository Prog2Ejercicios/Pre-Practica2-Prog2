#Crear un programa que permita ingresar una lista de numeros al usuario y muestre por pantalla el maximo entre ambos numeros.

#Nota : Hacerlo con la función max(a,b) y luego con una comparación

#INICIO
lista=[]
print("Ingrese varios números, para finalizar presione 0.")
while True:
    print("Ingresar número:")
    numero=int(input())
    if numero!=0:
        lista.append(numero)
    else:
        break
maximo = max(lista)
print('El mayor número es: ', maximo)

#CON COMPARACIÓN:
lista=[]
print("Ingrese varios números, para finalizar presione 0.")
while True:
    print("Ingresar número:")
    numero=int(input())
    if numero!=0:
        lista.append(numero)
    else:
        break
val_max = None
for num in lista:
    if (val_max is None or num > val_max):
        val_max = num
print('El mayor número es: ', val_max)

#FIN