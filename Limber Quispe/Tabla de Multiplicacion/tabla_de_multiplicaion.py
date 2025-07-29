print("📚 TABLAS DE MULTIPLICAR Y DIVISION 📚")

while True:
    entrada = input("Introduce el número de la tabla (ej. 5): ")
    if entrada.isdigit():
        num_tabla = int(entrada)
        break
    else:
        print("⚠️ Por favor, ingresa un número entero válido.")

# Tabla de multiplicar
print(f"\n----- Tabla de multiplicar del {num_tabla} -----")
for i in range(1, 11):
    resultado = num_tabla * i
    print(f"{num_tabla} x {i} = {resultado}")

# Tabla inversa (división)
print(f"\n----- Tabla inversa (división) del {num_tabla} -----")
for i in range(1, 11):
    resultado = num_tabla * i
    division = resultado / num_tabla
    print(f"{resultado} ÷ {num_tabla} = {int(division)}")

print("\n---- Fin del programa ---- Limber David Quispe ----")

