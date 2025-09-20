
public class cliente {
    
    int id_cliente;
    String nombre; // atributo
    int edad;
    String email;
    int direccion;
    int telefono;



    public cliente(int id_cliente, String nombre, int edad, String email, int direccion, int telefono) {
        this.id_cliente = id_cliente; // constructor
        this.nombre = nombre;
        this.edad = edad;
        this.email = email; // constructor
        this.direccion = direccion; //this es una referencia al objeto actual
        this.telefono = telefono;
    }

    public void registrar() { // método  //pub
        System.out.println("Nombre: " + nombre + ", Edad: " + edad, ", Email: " + email);
    }

    public void actualizarDatos() { // método
        System.out.println("Nombre: " + nombre + ", Edad: " + edad, ", Email: " + email);
    }

    public void iniarSesion() { // método
        System.out.println("Email: " + email);
    }

    public void VerHistorial() { // método
        System.out.println("Nombre: " + nombre + ", Edad: " + edad, ", Email: " + email);
    }
}

public class producto {

    int id_producto;
    String nombre; // atributo
    String descripcion;
    int precio;
    int stock;

    public producto(int id_producto, String nombre, String descripcion, int precio, int stock) {
        this.id_producto = id_producto; // constructor
        this.nombre = nombre;
        this.descripcion = descripcion; // constructor
        this.precio = precio;
        this.stock = stock;
    }

    public void actualizarStock() { // metodos
        System.out.println("Nombre: " + nombre + ", Precio: " + precio + ", Stock: " + stock);
    }

    public void verDetalles() { // metodos
        System.out.println("Nombre: " + nombre + ", Precio: " + precio + ", Stock: " + stock);
    }

    public void mostrarDetalles() { // metodos
        System.out.println("Nombre: " + nombre + ", Precio: " + precio);
    }
}

public class pago{
    int id_pago;
    int monton;
    String metodo;
    int fechaPago;

    public pago(int id_pago, int monton, string metodo, int fechaPago) {
        this.id_pago = id_pago; // constructor
        this.monton = monton;
        this.metodo = metodo; // constructor
        this.fechaPago = fechaPago;
    }

    public void procesarPago() { // metodos
        System.out.println("Monto: " + monton + ", Metodo: " + metodo + ", Fecha de Pago: " + fechaPago);
    }

    public void verificarPago() { // metodos
        System.out.println("Monto: " + monton + ", Metodo: " + metodo + ", Fecha de Pago: " + fechaPago);
    }
}

public class carrito_de_compra{
    
    int id_carrito;
    String listaProducto;
    int total;

    public carrito_de_compra(int id_carrito, String listaProducto, int total) {
        this.id_carrito = id_carrito; // constructor
        this.listaProducto = listaProducto;
        this.total = total; // constructor
    }

    public void agregarProducto() { // metodos
        System.out.println("Lista de Productos: " + listaProducto + ", Total: " + total);
    }

    public void eliminarProducto() { // metodos
        System.out.println("Lista de Productos: " + listaProducto + ", Total: " + total);
    }

    public void calcularTotal() { // metodos
        System.out.println("Total: " + total);
    }
} 

public class pedido{
    
    int id_padido;
    int fechaPedido;
    boolean estado;
    String listaProducto;
    int total;

    public pedido(int id_padido, int fechaPedido, boolean estado, String listaProducto, int total) {
        this.id_padido = id_padido; // constructor
        this.fechaPedido = fechaPedido;
        this.estado = estado; // constructor
        this.listaProducto = listaProducto;
        this.total = total;
    }

    public void confirmarPedido() { // metodos
        System.out.println("Fecha del Pedido: " + fechaPedido + ", Estado: " + estado + ", Total: " + total);
    }

    public void actualizarEstado() { // metodos
        System.out.println("Fecha del Pedido: " + fechaPedido + ", Estado: " + estado + ", Total: " + total);
    }

    public void calcularPedido() { // metodos
        System.out.println("Total: " + total);
    }
}