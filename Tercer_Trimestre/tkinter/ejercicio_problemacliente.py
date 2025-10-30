import tkinter as tk
from tkinter import messagebox

# importa messagebox y tienda

productos = [
    {"nombre": "Pasta", "precio": 1500, "cantidad": 100},
    {"nombre": "Pollo", "precio": 3500, "cantidad": 200},
    {"nombre": "Arroz", "precio": 2000,"cantidad": 10},
    {"nombre": "Carne", "precio": 3000,"cantidad": 100},
]

# se hace la lista de los nombres

ventana = tk.Tk()
ventana.title("Tienda Mixy")
ventana.config(bg='green')
ventana.config(width="400", height="350")

listbox_productos = tk.Listbox(ventana, width=40)

def muestra_producto():
    for p in productos:
        texto = f"{p['nombre']} - ${p['precio']}, Cantidad: {p['cantidad']}"
        listbox_productos.insert(tk.END, texto)

    listbox_productos.pack(pady=10)


boton = tk.Button(
    ventana,
    text="Mostrar productos",
    command=muestra_producto
)
boton.pack(pady=20)

ventana.mainloop()