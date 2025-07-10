# Definición de la función cursiva
def factorial(n):
  if n < 0:
    raise ValueError("El factorial no está definido para números negativos")
  elif n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n - 1)  

# Solicitar al usuario un número
try:
  numero = int(input("Ingresa un número para calcular su factorial: "))
  resultado = factorial(numero)
  print(f"El factorial de {numero} es {resultado}")
except ValueError as e:
  print(e)


