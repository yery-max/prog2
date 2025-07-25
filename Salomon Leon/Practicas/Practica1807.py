class Producto:
  def __init__(self, nombre, precio, disponible=True):
      """
      Inicializa un nuevo producto.

      Args:
          nombre (str): El nombre del producto.
          precio (float): El precio del producto.
          disponible (bool): True si el producto está en stock, False de lo contrario.
      """
      self.nombre = nombre
      self.precio = precio
      self.disponible = disponible

  def mostrar_info(self):
      """
      Muestra información detallada del producto.
      """
      estado = "Disponible" if self.disponible else "Agotado"
      print(f"--- Información del Producto ---")
      print(f"Nombre: {self.nombre}")
      print(f"Precio: ${self.precio:.2f}")
      print(f"Estado: {estado}")
      print("-" * 25)

class CarritoDeCompras:
  def __init__(self):
      """
      Inicializa un nuevo carrito de compras vacío.
      """
      self.productos = []

  def agregar_producto(self, producto):
      """
      Agrega un producto al carrito si está disponible.

      Args:
          producto (Producto): El objeto Producto a agregar.
      """
      if producto.disponible:
          self.productos.append(producto)
          print(f"'{producto.nombre}' agregado al carrito.")
      else:
          print(f"Lo sentimos, '{producto.nombre}' no está disponible actualmente.")

  def mostrar_carrito(self):
      """
      Muestra los productos actualmente en el carrito.
      """
      if not self.productos:
          print("El carrito de compras está vacío.")
          return

      print("\n--- Contenido del Carrito ---")
      for i, producto in enumerate(self.productos):
          print(f"{i + 1}. {producto.nombre} - ${producto.precio:.2f}")
      print("-" * 25)

  def calcular_total(self):
      """
      Calcula el precio total de todos los productos en el carrito.

      Returns:
          float: El precio total del carrito.
      """
      total = sum(producto.precio for producto in self.productos)
      return total

  def vaciar_carrito(self):
      """
      Vacía todos los productos del carrito.
      """
      self.productos = []
      print("El carrito de compras ha sido vaciado.")

class Cliente:
  def __init__(self, nombre, direccion):
      """
      Inicializa un nuevo cliente.

      Args:
          nombre (str): El nombre del cliente.
          direccion (str): La dirección del cliente.
      """
      self.nombre = nombre
      self.direccion = direccion
      self.carrito = CarritoDeCompras() # Cada cliente tiene su propio carrito

  def ver_carrito(self):
      """
      Muestra los productos en el carrito del cliente.
      """
      print(f"\n--- Carrito de {self.nombre} ---")
      self.carrito.mostrar_carrito()

  def realizar_compra(self):
      """
      Calcula el total de la compra, muestra un resumen y vacía el carrito.
      """
      if not self.carrito.productos:
          print(f"{self.nombre}, no hay productos en tu carrito para comprar.")
          return

      print(f"\n--- Realizando compra para {self.nombre} ---")
      self.carrito.mostrar_carrito()
      total_compra = self.carrito.calcular_total()
      print(f"Total a pagar: ${total_compra:.2f}")

      # Aquí podríamos añadir lógica de pago real, confirmación, etc.
      print(f"Compra realizada con éxito. ¡Gracias por tu compra, {self.nombre}!")
  
      self.carrito.vaciar_carrito()
      print("-" * 25)

# --- EJEMPLO DE USO ---

if __name__ == "__main__":
  # 1. Crear algunos productos
  tv = Producto("Smart TV 50 pulgadas", 499.99)
  auriculares = Producto("Auriculares Bluetooth", 75.50)
  teclado = Producto("Teclado Mecánico", 120.00, disponible=False) # Producto no disponible
  raton = Producto("Ratón Ergonómico", 30.25)

  # 2. Mostrar información de los productos
  print("--- Productos Disponibles ---")
  tv.mostrar_info()
  auriculares.mostrar_info()
  teclado.mostrar_info()
  raton.mostrar_info()

  # 3. Crear un cliente
  cliente1 = Cliente("Ana López", "Calle Falsa 123, Ciudad")
  cliente2 = Cliente("Juan Pérez", "Avenida Siempre Viva 456, Pueblo")

  # 4. Cliente 1 agrega productos a su carrito
  print(f"\n>>> {cliente1.nombre} va a comprar <<<")
  cliente1.carrito.agregar_producto(tv)
  cliente1.carrito.agregar_producto(auriculares)
  cliente1.carrito.agregar_producto(teclado) # Intentar agregar un producto no disponible
  cliente1.carrito.agregar_producto(raton)

  # 5. Cliente 1 ve su carrito
  cliente1.ver_carrito()

  # 6. Cliente 1 realiza la compra
  cliente1.realizar_compra()

  # 7. Intentar ver el carrito después de la compra (debería estar vacío)
  cliente1.ver_carrito()

  print(f"\n>>> {cliente2.nombre} va a comprar <<<")
  # 8. Cliente 2 agrega productos a su carrito
  cliente2.carrito.agregar_producto(auriculares)
  cliente2.carrito.agregar_producto(raton)
  cliente2.ver_carrito()
  cliente2.realizar_compra()
