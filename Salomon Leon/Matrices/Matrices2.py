matriz = [[col + fila *5 + 1 for col in range(5)]for fila in range(5)]
for fila in matriz:
    print(" ", join(str(elemento) for elemento in fila))
print()
