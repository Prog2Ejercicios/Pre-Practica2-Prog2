#Crear un programa que permita ingresar dos numeros al usuario y muestre por pantalla el maximo entre ambos numeros.

#Nota : Hacerlo con la función max(a,b) y luego con una comparación

#INICIO
print("Ingrese dos números: ")
num1=int(input())
num2=int(input())
mayor=max(num1, num2)
print(f"El mayor es: {mayor}")

if num2>num1:
    print(f"El mayor número es: {num2}")
elif num2<num1:
    print(f"El mayor número es: {num1}")
else:
    print("Ambos números son iguales")
#FIN
