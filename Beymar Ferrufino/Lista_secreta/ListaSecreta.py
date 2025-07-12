# Lista secreta predefinida por el profesor
lista_secreta = [7, 14, 3, 21, 9]
# Instrucciones para los estudiantes
print("🕵️‍♀️ ¡Bienvenidos al juego del Ahorcado Lógico con Listas!")
print("Debes descubrir qué números hay en la lista secreta de 5 elementos.")
print("Pero no puedes verla directamente. En cada turno puedes hacer una 'pregunta' en forma de código Python.")
print("Ejemplos: len(lista_secreta), lista_secreta[2], lista_secreta[0] > 10")
print("Cuando creas tener la lista completa, escribe: adivinar")
print("--------------------------------------------------------------")
# Bucle de interacción
while True:
    instruccion = input(">>> Escribe tu instrucción (o 'adivinar'): ")
    if instruccion.strip().lower() == "adivinar":
        intento = input(" Escribe tu intento de lista (separa por comas): ")
        try:
            intento_lista = [int(x.strip()) for x in intento.split(",")]
            if intento_lista == lista_secreta:
                print(" ¡Correcto! Has descubierto la lista secreta.")
                break
            else:
                print(" Esa no es la lista correcta. Sigue preguntando.")
        except ValueError:
            print(" Error: asegúrate de escribir solo números separados por comas.")
    else:
        try:
            # Evaluar la instrucción del alumno en un entorno controlado
            resultado = eval(instruccion, {"lista_secreta": lista_secreta})
            print("Resultado:", resultado)
        except Exception as e:
            print(" Error en tu instrucción:", e)
