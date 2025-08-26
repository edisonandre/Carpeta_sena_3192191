class Cliente:
    def __init__(self, idCliente, nombre, email, direccion, telefono):
        self.idCliente = idCliente
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.telefono = telefono
        
    def registrar(self):
        print(f"El cliente {self.nombre} fue registrado")
    
    def actualizarDatos(self):
        print(f"Datos del cliente {self.nombre} actualizados")
        
    def iniciarSesion(self):
        print(f"Cliente {self.nombre} inició sesión")
        
    def verHistorial(self):
        print("Mostrando historial")

        
class Producto:
    def __init__(self, idProducto, nombre_pro, descripcion, precio, stock):
        self.idProducto = idProducto
        self.nombre_pro = nombre_pro
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        
    def mostrarDetalles(self):
        print(f"Producto: {self.nombre_pro} - Precio: {self.precio} - Stock: {self.stock}")

class Carrito_de_compra:
    def __init__(self, id_carrito, listaProducto, total):
        self.id_carrito = id_carrito
        self.listaProducto = listaProducto
        self.total = total
        
    def mostrarDetalles(self):
        print(f"Carrito #{self.id_carrito} con {len(self.listaProducto)} productos - Total: {self.total}")

        
class pago:
    def __init__(self, id_pago, monton, metodo, fechaPago):
        self.id_pago = id_pago
        self.monton = monton
        self.metodo = metodo
        self.fechaPago = fechaPago
        
    def procesarPago():
        print("esta procesando pago")
    
    def verificarPago():
        print("se verifico el pago")
        
class carrito_de_compra:
    def __init__(self, id_carrito, listaProducto, Total):
        self.id_carrito = id_carrito
        self.listaProducto = listaProducto
        self.total = Total
        
    def agregarProducto():
        print("se agrego un producto")
        
    def eliminarProducto():
        print("eliminando productos")
        
    def calcularTotal():
        print("calculando el total")
        
class Pedido:
    def __init__(self, id_pedido, fechaPedido, estado, listaProducto, total, cliente):
        self.id_pedido = id_pedido
        self.fechaPedido = fechaPedido
        self.estado = estado
        self.listaProducto = listaProducto
        self.total = total
        self.cliente = cliente   # asociación, no herencia
        
    def confirmarPedido(self):
        print("Se confirmó el pedido")
        
    def actualizarEstado(self):
        print("Se actualizó el estado")
        
    def calcularPedido(self):
        print("Se calculó el pedido")

# Creamos objetos
p1 = Producto(1, "Laptop", "Laptop gamer", 2500, 10)
p2 = Producto(2, "Mouse", "Mouse gamer", 150, 50)
carrito = Carrito_de_compra(101, [p1, p2], 2650)

# Lista polimórfica
objetos = [p1, p2, carrito]

for obj in objetos:
    obj.mostrarDetalles()   # polimorfismo en acción

