matriz = [
  [1,2,7,8,9],
  [3,4,5,6,7],
  [5,6,7,8,9],
  [7,8,9,10,11],
  [9,10,11,12,13]
]

Suma = 0
sumatotal = sum([elemento for fila in matriz for elemento in fila])
print(f"La suma de todos los elementos de la matriz es: {sumatotal}")
for fila in matriz:
  for elemento in fila:
    Suma += elemento
print(f"La suma de todos los elementos de la matriz es: {Suma}")
print("---Fin del programa---Salomon Leon")
