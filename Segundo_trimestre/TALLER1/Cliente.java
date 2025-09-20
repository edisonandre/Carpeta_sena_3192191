public class Cliente {
    public static void cliente(String[] args) {

        // Crear un cliente
        Cliente cliente1 = new Cliente(1, "Andrés", "andres@email.com", "Calle 123", "3001234567");
        
        cliente1.registrar();
        cliente1.iniciarSesion();

        // Crear un producto
        Producto producto1 = new Producto(101, "Laptop", "Laptop Gamer", 3500.50, 5);
        producto1.verDetalles();
        producto1.actualizarStock(3); // aumenta el stock

        // Crear un pago
        Pago pago1 = new Pago(5001, 3500.50, "Tarjeta de Crédito", "26/08/2025");
        pago1.mostrarPago();

        // Simular historial del cliente
        cliente1.verHistorial();
    System.out.println("--- Simulación completada ---");
    }
}
