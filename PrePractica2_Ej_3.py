#Crear un programa que utilice la estructura try - catch. El usuario debe de ingresar dos numeros y mostrar por pantalla
#el resultado de la división entre ambos numeros. 

#En caso de que el divisor sea 0 utilizar la excepción ZeroDivisionError y mostrar el error por pantalla.


#INICIO
while True:
    try:    
        Numero1=int(input("Ingrese primer valor:"))
        Numero2=int(input("Ingrese segundo valor:"))
        division=Numero1/Numero2
        print("La división es",division)
    except ValueError:
        print("debe ingresar números.")
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    respuesta=input("Desea ingresar otro par de valores?[s/n]")
    if respuesta=="n":
        break  

  
#FIN