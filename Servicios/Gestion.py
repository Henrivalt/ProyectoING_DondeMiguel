import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class TiendaApp:
    def __init__(self, root):
        self.root = root
        self.root.columnconfigure(0,weight=1)
        self.root.rowconfigure(0,weight=1)

        frame = tk.Frame(self.root,bg='white')
        frame.grid(row=0,column=0)

        estilo_etiqueta = {'font': ('Segoe UI', 12, 'bold'), 'fg': '#1c1e21', 'bg': 'white'}

        estilo_entrada = {'width': 30, 'bg': "#f0f2f5", 'fg': "#1c1e21", 'relief': "flat", 'font': ('Segoe UI', 10),
                          'justify': 'center'}

        estilo_boton = {'bg': "#1877f2", 'fg': "white", 'activebackground': "#145dbf",
                        'activeforeground': "white", 'relief': "flat", 'font': ('Segoe UI', 10, 'bold'),
                        'cursor': "hand2"}

        self.productos = []
        tk.Label(frame,text='Gestion de productos',font=('Segoe UI', 20, 'bold'),bg='white',fg='darkblue').grid(row=0,column=0,columnspan=2,pady=10,padx=10)
        # Entradas de producto
        tk.Label(frame, text="Nombre del producto",**estilo_etiqueta).grid(row=1, column=0)
        self.nombre_var = tk.StringVar()
        tk.Entry(frame, textvariable=self.nombre_var,**estilo_entrada).grid(row=1, column=1)

        tk.Label(frame, text="Precio",**estilo_etiqueta).grid(row=2, column=0)
        self.precio_var = tk.StringVar()
        tk.Entry(frame, textvariable=self.precio_var,**estilo_entrada).grid(row=2, column=1)

        tk.Label(frame, text="Cantidad",**estilo_etiqueta).grid(row=3, column=0)
        self.cantidad_var = tk.StringVar()
        tk.Entry(frame, textvariable=self.cantidad_var,**estilo_entrada).grid(row=3, column=1)

        # Botón para agregar producto
        tk.Button(frame, text="Agregar Producto", command=self.agregar_producto,**estilo_boton).grid(row=4, column=0, columnspan=2, pady=10)

        # Tabla de productos
        self.tabla = ttk.Treeview(frame, columns=("Nombre", "Precio", "Cantidad"), show='headings')
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Precio", text="Precio")
        self.tabla.heading("Cantidad", text="Cantidad")
        self.tabla.grid(row=5, column=0, columnspan=2)

        # Botón para eliminar producto
        tk.Button(frame, text="Eliminar Producto Seleccionado", command=self.eliminar_producto,**estilo_boton).grid(row=6, column=0, columnspan=2, pady=10)

    def agregar_producto(self):
        nombre = self.nombre_var.get().strip()
        try:
            precio = float(self.precio_var.get())
            cantidad = int(self.cantidad_var.get())
        except ValueError:
            messagebox.showerror("Error", "Precio debe ser un número y cantidad un entero.")
            return

        if nombre and precio >= 0 and cantidad >= 0:
            self.tabla.insert("", "end", values=(nombre, f"${precio:.2f}", cantidad))
            self.nombre_var.set("")
            self.precio_var.set("")
            self.cantidad_var.set("")
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios y deben ser válidos.")

    def eliminar_producto(self):
        seleccionado = self.tabla.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Selecciona un producto para eliminar.")
            return
        for item in seleccionado:
            self.tabla.delete(item)

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = TiendaApp(root)
    root.mainloop()