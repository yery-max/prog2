def clasificar_pelicula(edad):
  #Clasificacion de peliculas
  if edad < 0:
    return "Edad no valida"
  elif edad < 13:
    return "Te recomendamos peliculas clasificadas G o PG"
  elif edad < 18:
    return "puedas ver peliculas clasificadas PG-13"
  else:
    return "¡puedas ver peliculas clasificadas R!"
#===== Pruebas unitarias =====
assert clasificar_pelicula(20) == "¡puedas ver peliculas clasificadas R!","Error para edad 20"
assert clasificar_pelicula(15) == "puedas ver peliculas clasificadas PG-13","Error para edad 15"
assert clasificar_pelicula(10) == "Te recomendamos peliculas clasificadas G o PG","Error para edad 10"
assert clasificar_pelicula(-5) == "Edad no valida","Error para edad negativa"

print ("Pruebas unitarias completadas")

while True:
  try:
    edad = int(input("Ingresa tu edad: "))
    resultado = clasificar_pelicula(edad)
    print(f"{resultado}")
    break  
  except ValueError:
    print("Debes ingresar un numero entero. Intentalo de nuevo")
    continue
    #Preguntar si desea clasificar otra pelicula
  continuar = input("¿Deseas clasificar otra pelicula? (Y/N): ").strip().lower()
  if continuar != "Y":
    break

print("---Fin del programa---Salomon Leon")
