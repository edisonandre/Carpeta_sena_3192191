import tkinter as tk

contador = 0

def contar():
    global contador
    contador += 1
    label_contador.config(text=f"Clics: {contador}")

root = tk.Tk()
root.title("Contador de Clics")
root.geometry("200x150")

label_contador = tk.Label(root, text="Clics: 0", font=("Arial", 14))
label_contador.pack(pady=10)

tk.Button(root, text="Haz clic aquí", command=contar).pack()

root.mainloop()
