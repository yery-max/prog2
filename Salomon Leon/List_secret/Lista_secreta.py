import getpass

# Ingreso oculto de la lista secreta por parte del profesor
print("Ingresa la lista secreta (5 números separados por comas). No se mostrará en pantalla.")
oculto = getpass.getpass("Lista secreta: ")

try:
    lista_secreta = [int(x.strip()) for x in oculto.split(",")]
    if len(lista_secreta) != 5:
        raise ValueError("La lista debe contener exactamente 5 números.")
except Exception as e:
    print(f"⚠ Error al procesar la lista secreta: {e}")
    exit()

# Instrucciones para los estudiantes
print("\n🕵‍♀ ¡Bienvenidos al juego del Ahorcado Lógico con Listas!")
print("Debes descubrir qué números hay en la lista secreta de 5 elementos.")
print("Pero no puedes verla directamente. En cada turno puedes hacer una 'pregunta' en forma de código Python.")
print("Ejemplos: len(lista_secreta), lista_secreta[2], lista_secreta[0] > 10")
print("Cuando creas tener la lista completa, escribe: adivinar")
print("--------------------------------------------------------------")

# Contador de intentos
intentos = 0
preguntas_realizadas = 0

# Bucle de interacción
while True:
    instruccion = input(">>> Escribe tu instrucción (o 'adivinar'): ")

    if instruccion.strip().lower() == "adivinar":
        intento = input("🧠 Escribe tu intento de lista (separa por comas): ")
        intentos += 1
        try:
            intento_lista = [int(x.strip()) for x in intento.split(",")]
            if intento_lista == lista_secreta:
                print(f"🎉 ¡Correcto! Has descubierto la lista secreta en {intentos} intento(s).")
                print(f"🧪 Además hiciste {preguntas_realizadas} pregunta(s) antes de adivinar.")
                print("---Fin del programa---Salomon Leon")
                break
            else:
                print("❌ Esa no es la lista correcta. Sigue preguntando.")
        except ValueError:
            print("⚠ Error: asegúrate de escribir solo números separados por comas.")
    else:
        preguntas_realizadas += 1
        try:
            # Evaluar la instrucción del alumno en un entorno controlado y seguro
            resultado = eval(
                instruccion,
                {"__builtins__": None},
                {
                    "lista_secreta": lista_secreta,
                    "len": len,
                    "sum": sum,
                    "max": max,
                    "min": min
                }
            )
            print("Resultado:", resultado)
        except Exception as e:
            print("⚠ Error en tu instrucción:", e)
