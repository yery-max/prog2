import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

print("🎮 Bienvenido al juego de Limber Quispe 🎮\n")
print("🎮  ADIVINA LA PALABRA CORRECTA🎮\n")
# Jugador 1 escribe la palabra secreta (sin que la vea el otro jugador)
palabra_secreta = input("Jugador 1, Escribe la palabra secreta: ").lower().strip()
while not palabra_secreta.isalpha():
    palabra_secreta = input("Usa solo letras. Ingresa la palabra secreta: ").lower().strip()

limpiar_pantalla()  # Limpiar pantalla para que no la vea el otro jugador

print("Jugador 2, ¡Tienes 4 intentos adivina la palabra!\n")
print("-☠️---Que Comienze el Juego---☠️!\n")

# Inicializar variables
letras_adivinadas = []
intentos = 4

while intentos > 0:
    mostrar = [letra if letra in letras_adivinadas else '_' for letra in palabra_secreta]
    print("Palabra:", ' '.join(mostrar))
    print(f"Intentos restantes: {intentos}")
    print(f"Letras adivinadas: {' '.join(letras_adivinadas)}")

    intento = input("Ingresa una letra: ").lower().strip()

    if len(intento) != 1 or not intento.isalpha():
        print("Por favor, escribe solo una letra válida.\n")
        continue

    if intento in letras_adivinadas:
        print("Ya intentaste esa letra. Prueba otra.\n")
        continue

    letras_adivinadas.append(intento)

    if intento in palabra_secreta:
        print("✅ ¡Correcto!\n")
    else:
        intentos -= 1
        print("❌ ¡Incorrecto!\n")

    if all(letra in letras_adivinadas for letra in palabra_secreta):
        print(f"\n🎉 ¡Felicidades Campeon! Adivinaste la palabra: {palabra_secreta}")
        break
else:
    print(f"\n😢 ¡Siga Participando! La palabra era: {palabra_secreta}")
print("Limber David Quispe - FIN DEL PROGRAMA")
