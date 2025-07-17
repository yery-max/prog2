def es_matriz_simetrica(matriz):
  n = len(matriz)
  # Verificar si la matriz es cuadrada
  if any(len(fila) != n for fila in matriz):
      return False  
  # Verificar simetría usando comprensión de listas
  return all(matriz[i][j] == matriz[j][i] for i in range(n) for j in range(n))

#Fin Del Programa
print ("Fin del programa ---- Yery Torrico")
