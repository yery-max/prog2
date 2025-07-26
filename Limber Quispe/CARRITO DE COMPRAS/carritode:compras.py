# Lista de productos disponibles
productos = {
    "1": {"nombre": "Laptop", "precio": 2000},
    "2": {"nombre": "Celular", "precio": 2300},
    "3": {"nombre": "Audífonos", "precio": 150},
    "4": {"nombre": "Mouse", "precio": 100},
    "5": {"nombre": "Teclado", "precio": 210}
}

# Carrito de compras
carrito = []

def mostrar_productos():
    print("\nProductos disponibles:")
    for clave, producto in productos.items():
        print(f"{clave}. {producto['nombre']} - Bs. {producto['precio']}")

def agregar_al_carrito():
    mostrar_productos()
    eleccion = input("Ingrese el número del producto que desea agregar al carrito: ")
    if eleccion in productos:
        carrito.append(productos[eleccion])
        print(f"✅ {productos[eleccion]['nombre']} fue agregado al carrito.")
    else:
        print("❌ Opción inválida.")

def mostrar_carrito():
    if not carrito:
        print("🛒 Tu carrito está vacío.")
        return
    print("\n🛒 Carrito de compras:")
    total = 0
    for i, producto in enumerate(carrito, 1):
        print(f"{i}. {producto['nombre']} - Bs. {producto['precio']}")
        total += producto['precio']
    print(f"💰 Total a pagar: Bs. {total}")

def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Ver productos")
        print("2. Agregar producto al carrito")
        print("3. Ver carrito")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            agregar_al_carrito()
        elif opcion == "3":
            mostrar_carrito()
        elif opcion == "4":
            print("Gracias por usar el carrito de compras. ¡Hasta pronto!")
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")

# Ejecutar el programa
menu()
print("Limber David Quispe - FIN DEL PROGRAMA")
