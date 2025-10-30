import tkinter as tk
from tkinter import messagebox
import psycopg2

# --- Configuración de la base de datos ---
DB_NAME = "bd_sena"
DB_USER = "postgres"
DB_PASS = "123456"
DB_HOST = "localhost"
DB_PORT = "5432"

# --- Conexión a la base de datos ---
def conectar():
    try:
        conexion = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT
        )
        return conexion
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo conectar a la base de datos:\n{e}")
        return None

# --- Crear tabla si no existe ---
def crear_tabla():
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS personas (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(50),
                apellido VARCHAR(50),
                edad INT
            );
        """)
        conexion.commit()
        conexion.close()

# --- Insertar datos ---
def guardar_datos():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    edad = entry_edad.get()

    if not (nombre and apellido and edad):
        messagebox.showwarning("Campos vacíos", "Por favor complete todos los campos.")
        return

    try:
        edad = int(edad)
    except ValueError:
        messagebox.showerror("Error", "La edad debe ser un número entero.")
        return

    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO personas (nombre, apellido, edad) VALUES (%s, %s, %s)",
                       (nombre, apellido, edad))
        conexion.commit()
        conexion.close()
        messagebox.showinfo("Éxito", "Datos guardados correctamente.")
        limpiar_campos()
        mostrar_datos()

# --- Mostrar datos en la lista ---
def mostrar_datos():
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM personas ORDER BY id ASC")
        filas = cursor.fetchall()
        conexion.close()

        listbox.delete(0, tk.END)
        for fila in filas:
            listbox.insert(tk.END, f"{fila[0]} - {fila[1]} {fila[2]}, {fila[3]} años")

# --- Limpiar entradas ---
def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_edad.delete(0, tk.END)

# --- Interfaz gráfica ---
ventana = tk.Tk()
ventana.title("Registro de Personas")
ventana.geometry("400x400")
ventana.config(padx=15, pady=15)

tk.Label(ventana, text="Nombre:").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Apellido:").pack()
entry_apellido = tk.Entry(ventana)
entry_apellido.pack()

tk.Label(ventana, text="Edad:").pack()
entry_edad = tk.Entry(ventana)
entry_edad.pack()

tk.Button(ventana, text="Guardar", command=guardar_datos, bg="lightgreen").pack(pady=5)
tk.Button(ventana, text="Mostrar Datos", command=mostrar_datos, bg="lightblue").pack(pady=5)

listbox = tk.Listbox(ventana, width=50, height=10)
listbox.pack(pady=10)

crear_tabla()
ventana.mainloop()
