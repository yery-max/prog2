def Area_rectangulo(base, altura):
  return base * altura

while True:
  try:
    base = float(input("Ingresa la base del rectangulo: "))
    altura = float(input("Ingresa la altura del rectangulo: "))
    print(f"El area del rectangulo es: {Area_rectangulo(base, altura)}")
  except  ValueError:
    print("Debes ingresar un numero valido")
    continue
  continuar = input("¿Desea ingresar otros datos? (Y/N): "). strip().lower()
  if continuar != 'y':
    break
