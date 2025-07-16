matriz =[[1,2,3],[4,5,6],[7,8,9]]
# Opción 1: Recorriendo con índice
num_filas = len(matriz)
num_columnas = len(matriz[0])
for i in range(num_filas):
    for j in range(num_columnas):
        elemento = matriz[i][j]
        print(f"Elemento en la fila {i}, columna {j}: {elemento}")
# Opción 2: Recorriendo por elemento (mas "pythonico")
for fila_actual in matriz:
    for elemento in fila_actual:
        print(elemento, end=" ")
    print()
print("Limber David - FIN DEL PROGRAMA")
