def clasificar_peliculas(edad):
    if edad < 0:
      return "edad no validad"
    elif edad < 13:
      return "Te recomendamos peliculas clasificadas G o Pg"
    elif edad < 18:
      return "Te recomendamos peliculas clasificadas Pg-13"
    else:
      return "Puedes ver peliculas clasificadas R"
      
assert clasificar_peliculas(20) == "Puedes ver peliculas clasificadas R", "Error para edad 20"
assert clasificar_peliculas(15) == "Te recomendamos peliculas clasificadas Pg-13", "Error para edad 15"
assert clasificar_peliculas(10) == "Te recomendamos peliculas clasificadas G o Pg", "Error para edad 10"
assert clasificar_peliculas(-5) == "edad no validad", "Error para edad negativa"

print ("pruebas unitarias completadas")

  # === Vereficiador interactivo de edadades ===
while True:
  try:
    edad = int(input("Ingresa tu edad: "))
    resultado = clasificar_peliculas(edad)
    print(f"{resultado}")
  except ValueError:
    print("Debes ingresar un numero valido")
    continue

  continuar = input("¿Desear vereficar otra edad? (Y/N): "). strip().lower()
  if continuar != 'y':
    break
  print("Fin del programa --- Beymar Ferrufino")
