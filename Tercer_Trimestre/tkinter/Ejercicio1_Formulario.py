import tkinter as tk
from tkinter import messagebox

def guardar_datos():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    correo = entry_correo.get()
    messagebox.showinfo("Datos Guardados", f"Nombre: {nombre}\nEdad: {edad}\nCorreo: {correo}")

root = tk.Tk()
root.title("Formulario de Registro")
root.geometry("300x200")

tk.Label(root, text="Nombre:").pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

tk.Label(root, text="Edad:").pack()
entry_edad = tk.Entry(root)
entry_edad.pack()

tk.Label(root, text="Correo electrónico:").pack()
entry_correo = tk.Entry(root)
entry_correo.pack()

tk.Button(root, text="Guardar", command=guardar_datos).pack(pady=10)

root.mainloop()
