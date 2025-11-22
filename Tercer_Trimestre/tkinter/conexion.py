# ---------------------------------------------------------------
# Aplicación GUI (Tkinter) con base de datos PostgreSQL (psycopg2)
# Funcionalidad: Registro y visualización de personas (nombre, apellido, edad)
# Autor: [Tu nombre]
# ---------------------------------------------------------------

import tkinter as tk                # Módulo para crear interfaces gráficas
from tkinter import messagebox      # Para mostrar cuadros de mensaje emergentes
import psycopg2                     # Librería para conectar Python con PostgreSQL


# ===============================================================
# --- CONFIGURACIÓN DE LA BASE DE DATOS ---
# ===============================================================

# Datos de conexión (ajústalos según tu entorno)
DB_NAME = "bd_sena"
DB_USER = "postgres"
DB_PASS = "123456"
DB_HOST = "localhost"
DB_PORT = "5432"


# ===============================================================
# --- FUNCIÓN DE CONEXIÓN A LA BASE DE DATOS ---
# ===============================================================
def conectar():
    """
    Establece una conexión con la base de datos PostgreSQL.
    Retorna el objeto conexión si es exitosa, o None si ocurre un error.
    """
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
        # Si ocurre un error (por ejemplo, base de datos no encontrada),
        # se muestra un mensaje de error en una ventana emergente.
        messagebox.showerror("Error", f"No se pudo conectar a la base de datos:\n{e}")
        return None


# ===============================================================
# --- CREAR TABLA (si no existe) ---
# ===============================================================
def crear_tabla():
    """
    Crea la tabla 'personas' si aún no existe.
    La tabla tiene los campos: id, nombre, apellido y edad.
    """
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
        conexion.commit()  # Guarda los cambios en la base de datos
        conexion.close()   # Cierra la conexión


# ===============================================================
# --- GUARDAR DATOS EN LA BASE DE DATOS ---
# ===============================================================
def guardar_datos():
    """
    Obtiene los valores de las entradas de texto (nombre, apellido, edad),
    valida los datos y los inserta en la tabla 'personas'.
    """
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    edad = entry_edad.get()

    # Verifica si hay campos vacíos
    if not (nombre and apellido and edad):
        messagebox.showwarning("Campos vacíos", "Por favor complete todos los campos.")
        return

    # Valida que la edad sea un número entero
    try:
        edad = int(edad)
    except ValueError:
        messagebox.showerror("Error", "La edad debe ser un número entero.")
        return

    # Conecta con la base de datos e inserta los datos
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO personas (nombre, apellido, edad) VALUES (%s, %s, %s)",
            (nombre, apellido, edad)
        )
        conexion.commit()
        conexion.close()

        # Muestra mensaje de éxito y actualiza la lista
        messagebox.showinfo("Éxito", "Datos guardados correctamente.")
        limpiar_campos()
        mostrar_datos()


# ===============================================================
# --- MOSTRAR DATOS EN EL LISTBOX ---
# ===============================================================
def mostrar_datos():
    """
    Recupera los registros de la tabla 'personas' y los muestra
    en el Listbox de la interfaz gráfica.
    """
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM personas ORDER BY id ASC")  # Trae todos los registros ordenados por ID
        filas = cursor.fetchall()  # Obtiene todas las filas
        conexion.close()

        # Limpia el Listbox antes de mostrar los nuevos datos
        listbox.delete(0, tk.END)
        for fila in filas:
            # Muestra cada persona con su id, nombre, apellido y edad
            listbox.insert(tk.END, f"{fila[0]} - {fila[1]} {fila[2]}, {fila[3]} años")


# ===============================================================
# --- LIMPIAR CAMPOS DE ENTRADA ---
# ===============================================================
def limpiar_campos():
    """
    Limpia los campos de texto del formulario.
    """
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_edad.delete(0, tk.END)


# ===============================================================
# --- INTERFAZ GRÁFICA (Tkinter) ---
# ===============================================================

# Creación de la ventana principal
ventana = tk.Tk()
ventana.title("Registro de Personas")     # Título de la ventana
ventana.geometry("400x400")               # Tamaño de la ventana
ventana.config(padx=15, pady=15)          # Márgenes interiores

# Etiquetas y campos de texto para ingresar datos
tk.Label(ventana, text="Nombre:").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Apellido:").pack()
entry_apellido = tk.Entry(ventana)
entry_apellido.pack()

tk.Label(ventana, text="Edad:").pack()
entry_edad = tk.Entry(ventana)
entry_edad.pack()

# Botones para ejecutar funciones
tk.Button(ventana, text="Guardar", command=guardar_datos, bg="lightgreen").pack(pady=5)
tk.Button(ventana, text="Mostrar Datos", command=mostrar_datos, bg="lightblue").pack(pady=5)

# Listbox para mostrar los registros almacenados
listbox = tk.Listbox(ventana, width=50, height=10)
listbox.pack(pady=10)

# Crear la tabla si no existe antes de abrir la interfaz
crear_tabla()

# Mantiene la ventana abierta hasta que el usuario la cierre
ventana.mainloop()
