#Importamos la libreria random
import random
#se asigna un numero aleatorio del 1 al 100
num_secreto = random.randint(1,100)
intentos = 0
print("¡Adivina el numero secreto")
while True:
    #Adjuntamos el codigo que puede fallar
    try:
        #El usuario ingresa el numero
        print("Ingresa tu numero")
        adivinanza = int(input())
        intentos += 1
        if adivinanza < num_secreto:
            print("el numero ingresado es menor, intenta de nuevo")
        elif adivinanza > num_secreto:
            print("El numero ingresado es mayor, intenta de nuevo")
        else:
            print("¡felicidades! Adivinaste el numero...")
            print(f"En {intentos} intentos")
            print("---Fin del programa---Salomon Leon")
            break
    #Indica que hacer con el error posible
    except ValueError:
         print("Por favor ingresa un numero valido")
