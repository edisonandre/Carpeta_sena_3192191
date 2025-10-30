import tkinter as tk

def agregar_tarea():
    tarea = entry_tarea.get()
    if tarea != "":
        listbox_tareas.insert(tk.END, tarea)
        entry_tarea.delete(0, tk.END)

def eliminar_tarea():
    seleccion = listbox_tareas.curselection()
    if seleccion:
        listbox_tareas.delete(seleccion)

root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("300x300")

entry_tarea = tk.Entry(root, width=25)
entry_tarea.pack(pady=5)

tk.Button(root, text="Agregar", command=agregar_tarea).pack(pady=5)
tk.Button(root, text="Eliminar", command=eliminar_tarea).pack(pady=5)

listbox_tareas = tk.Listbox(root, width=30, height=10)
listbox_tareas.pack(pady=10)

root.mainloop()
