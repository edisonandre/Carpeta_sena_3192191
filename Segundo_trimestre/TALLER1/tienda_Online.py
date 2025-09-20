# --- Modelo de tienda en línea con Programación Orientada a Objetos (POO)
#     Comentado línea por línea para explicar el propósito de cada instrucción.

class Cliente:  # Define la clase 'Cliente' para representar a un usuario/cliente del sistema.
    def __init__(self, idCliente, nombre, email, direccion, telefono):  # Constructor que inicializa los atributos del cliente.
        self.idCliente = idCliente  # Guarda el identificador único del cliente.
        self.nombre = nombre        # Guarda el nombre del cliente.
        self.email = email          # Guarda el correo electrónico del cliente.
        self.direccion = direccion  # Guarda la dirección del cliente.
        self.telefono = telefono    # Guarda el número de teléfono del cliente.
        
    def registrar(self):  # Método que simula el registro del cliente en el sistema.
        print(f"El cliente {self.nombre} fue registrado")  # Muestra un mensaje confirmando el registro.
    
    def actualizarDatos(self):  
        print(f"Datos del cliente {self.nombre} actualizados")  
        
    def iniciarSesion(self):  
        print(f"Cliente {self.nombre} inició sesión")  
        
    def verHistorial(self):  
        print("Mostrando historial")  

        
class Producto:  # Define la clase 'Producto' para representar un artículo que se puede vender.
    def __init__(self, idProducto, nombre_pro, descripcion, precio, stock):  # Constructor de Producto.
        self.idProducto = idProducto    # Identificador único del producto.
        self.nombre_pro = nombre_pro    # Nombre del producto.
        self.descripcion = descripcion  # Descripción del producto.
        self.precio = precio            # Precio unitario del producto.
        self.stock = stock              # Cantidad disponible en inventario.
        
    def mostrarDetalles(self):  # Método que muestra información resumida del producto.
        print(f"Producto: {self.nombre_pro} - Precio: {self.precio} - Stock: {self.stock}")  # Detalle del producto.

class Carrito_de_compra:  # Clase que modela un carrito de compra que contiene productos.
    def __init__(self, id_carrito, listaProducto, total):  # Constructor del carrito.
        self.id_carrito = id_carrito          # Identificador único del carrito.
        self.listaProducto = listaProducto    # Lista de objetos 'Producto' agregados al carrito.
        self.total = total                    # Monto total del carrito (suma de precios de los productos).
        
    def mostrarDetalles(self):  # Método que muestra un resumen del carrito.
        print(f"Carrito #{self.id_carrito} con {len(self.listaProducto)} productos - Total: {self.total}")  # Resumen.

        
class pago:  # Clase para modelar un pago. (Nota: por convención, el nombre de clase debería ser 'Pago').
    def __init__(self, id_pago, monton, metodo, fechaPago):  # Constructor del pago.
        self.id_pago = id_pago      # Identificador único del pago.
        self.monton = monton        # Monto pagado (cantidad de dinero)
        self.metodo = metodo        # Método de pago 
        self.fechaPago = fechaPago  # Fecha en la que se realizó el pago.
        
    def procesarPago(self):  
        print("esta procesando pago")  
    
    def verificarPago(self):  
        print("se verifico el pago")  
        
class Pedido:  # Clase que representa un pedido realizado por un cliente.
    def __init__(self, id_pedido, fechaPedido, estado, listaProducto, total, cliente):  # Constructor del pedido.
        self.id_pedido = id_pedido          # Identificador único del pedido.
        self.fechaPedido = fechaPedido      # Fecha en que se generó el pedido.
        self.estado = estado                # Estado actual del pedido (p. ej., 'pendiente', 'enviado', 'entregado').
        self.listaProducto = listaProducto  # Lista de productos incluidos en el pedido.
        self.total = total                  # Importe total del pedido.
        self.cliente = cliente              # Referencia al objeto 'Cliente' que hizo el pedido (asociación, no herencia).
        
    def confirmarPedido(self):  
        print("Se confirmó el pedido")  
        
    def actualizarEstado(self):  
        print("Se actualizó el estado")  
        
    def calcularPedido(self):  
        print("Se calculó el pedido")  

# --- Zona de prueba / ejemplo de uso ---
# Creamos objetos de ejemplo para demostrar el funcionamiento.
p1 = Producto(1, "Laptop", "Laptop gamer", 2500, 10)  # Crea un producto con id 1, nombre 'Laptop', descripción y precio/stock.
p2 = Producto(2, "Mouse", "Mouse gamer", 150, 50)     # Crea otro producto con id 2, nombre 'Mouse', etc.
carrito = Carrito_de_compra(101, [p1, p2], 2650)         # Crea un carrito con los productos p1 y p2 y un total pre-calculado.

# Lista polimórfica: contiene objetos de diferentes clases que comparten el método 'mostrarDetalles'.
objetos = [p1, p2, carrito]  # Crea una lista con instancias de 'Producto' y 'Carrito_de_compra'.

for obj in objetos:                 # Recorre cada objeto de la lista 'objetos'.
    obj.mostrarDetalles()           # Llama a 'mostrarDetalles' sin importar el tipo: esto es polimorfismo en acción.
