matriz =[[1,2,3],[4,5,6],[7,8,9]]

# Opcion 1: Recorrido con indices 
num_filas = len(matriz)
num_columnas = len(matriz[0])
for i in range(num_filas):      
    for j in range(num_columnas): 
        elemento = matriz[i][j]
        print(f"Elemento en la fila {i}, columna {j}: {elemento}")

# Opcion 2: Recorriendo por elemento (mas "pythonico")
for fila_actual in matriz:
    for elemento in fila_actual:
        print(elemento, end=" ")
    print()
