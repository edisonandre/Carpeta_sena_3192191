import tkinter as tk

def convertir():
    try:
        valor = float(entry_valor.get())
        if var.get() == 1:
            resultado = (valor * 9/5) + 32
            label_resultado.config(text=f"{resultado:.2f} °F")
        else:
            resultado = (valor - 32) * 5/9
            label_resultado.config(text=f"{resultado:.2f} °C")
    except ValueError:
        label_resultado.config(text="Error: valor inválido")

root = tk.Tk()
root.title("Conversor de Temperaturas")
root.geometry("300x200")

tk.Label(root, text="Ingrese el valor:").pack()
entry_valor = tk.Entry(root)
entry_valor.pack()

var = tk.IntVar()
tk.Radiobutton(root, text="Celsius a Fahrenheit", variable=var, value=1).pack()
tk.Radiobutton(root, text="Fahrenheit a Celsius", variable=var, value=2).pack()

tk.Button(root, text="Convertir", command=convertir).pack(pady=10)
label_resultado = tk.Label(root, text="")
label_resultado.pack()

root.mainloop()
