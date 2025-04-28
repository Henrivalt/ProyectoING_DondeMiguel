import tkinter as tk
from tkinter import ttk, messagebox

class InventarioTiendaApp:
    def __init__(self, root):
        self.root = root
        self.root.columnconfigure(0,weight=1)
        self.root.rowconfigure(0,weight=1)

        estilo_frame = {'bg': "white", 'highlightbackground': "#dfe3ee", 'highlightthickness': 1, 'bd': 0}

        estilo_etiqueta = {'font': ('Segoe UI', 12, 'bold'), 'fg': '#1c1e21', 'bg': 'white'}

        estilo_entrada = {'width': 30, 'bg': "#f0f2f5", 'fg': "#1c1e21", 'relief': "flat", 'font': ('Segoe UI', 10),
                          'justify': 'center'}

        estilo_boton = {'bg': "#1877f2", 'fg': "white", 'activebackground': "#145dbf",
                        'activeforeground': "white", 'relief': "flat", 'font': ('Segoe UI', 10, 'bold'),
                        'cursor': "hand2"}

        # Inventario en formato: {nombre: {'cantidad': int, 'costo': float}}
        self.inventario = {}

        # ==== Sección: Agregar producto ====
        frame_agregar = tk.LabelFrame(root, text="Agregar producto",bg='white')
        frame_agregar.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        tk.Label(frame_agregar, text="Nombre",**estilo_etiqueta).grid(row=0, column=0)
        self.nombre_var = tk.StringVar()
        tk.Entry(frame_agregar, textvariable=self.nombre_var,**estilo_entrada).grid(row=0, column=1)

        tk.Label(frame_agregar, text="Cantidad",**estilo_etiqueta).grid(row=1, column=0)
        self.cantidad_var = tk.StringVar()
        tk.Entry(frame_agregar, textvariable=self.cantidad_var,**estilo_entrada).grid(row=1, column=1)

        tk.Label(frame_agregar, text="Costo",**estilo_etiqueta).grid(row=2, column=0)
        self.costo_var = tk.StringVar()
        tk.Entry(frame_agregar, textvariable=self.costo_var,**estilo_entrada).grid(row=2, column=1)

        tk.Button(frame_agregar, text="Agregar", command=self.agregar_producto,**estilo_boton).grid(row=3, column=0, columnspan=2, pady=5)

        # ==== Tabla de Inventario ====
        self.tabla = ttk.Treeview(root, columns=("Nombre", "Cantidad", "Costo"), show='headings')
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Cantidad", text="Cantidad")
        self.tabla.heading("Costo", text="Costo unitario")
        self.tabla.grid(row=1, column=0, padx=10, pady=10)

        # ==== Sección: Modificar producto ====
        frame_modificar = tk.LabelFrame(root, text="Modificar producto",bg='white')
        frame_modificar.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        tk.Label(frame_modificar, text="Nombre",**estilo_etiqueta).grid(row=0, column=0)
        self.nombre_mod_var = tk.StringVar()
        tk.Entry(frame_modificar, textvariable=self.nombre_mod_var,**estilo_entrada).grid(row=0, column=1)

        tk.Label(frame_modificar, text="Cantidad (+/-)",**estilo_etiqueta).grid(row=1, column=0)
        self.cantidad_mod_var = tk.StringVar()
        tk.Entry(frame_modificar, textvariable=self.cantidad_mod_var,**estilo_entrada).grid(row=1, column=1)

        tk.Label(frame_modificar, text="Nuevo costo (opcional)",**estilo_etiqueta).grid(row=2, column=0)
        self.costo_mod_var = tk.StringVar()
        tk.Entry(frame_modificar, textvariable=self.costo_mod_var,**estilo_entrada).grid(row=2, column=1)

        tk.Button(frame_modificar, text="Actualizar", command=self.modificar_producto,**estilo_boton).grid(row=3, column=0, columnspan=2, pady=5)

        # ==== Botón: Eliminar producto ====
        tk.Button(root, text="Eliminar producto seleccionado", command=self.eliminar_producto, bg="red", fg="white").grid(row=3, column=0, pady=10)

    def agregar_producto(self):
        nombre = self.nombre_var.get().strip()
        try:
            cantidad = int(self.cantidad_var.get())
            costo = float(self.costo_var.get())
        except ValueError:
            messagebox.showerror("Error", "Cantidad debe ser un entero y costo un número.")
            return

        if nombre in self.inventario:
            messagebox.showwarning("Advertencia", "El producto ya existe.")
            return

        self.inventario[nombre] = {"cantidad": cantidad, "costo": costo}
        self.actualizar_tabla()
        self.nombre_var.set("")
        self.cantidad_var.set("")
        self.costo_var.set("")

    def modificar_producto(self):
        nombre = self.nombre_mod_var.get().strip()
        if nombre not in self.inventario:
            messagebox.showerror("Error", "El producto no existe.")
            return

        try:
            cantidad_delta = int(self.cantidad_mod_var.get())
        except ValueError:
            cantidad_delta = 0

        nuevo_costo = self.costo_mod_var.get()
        if nuevo_costo:
            try:
                nuevo_costo = float(nuevo_costo)
                self.inventario[nombre]["costo"] = nuevo_costo
            except ValueError:
                messagebox.showerror("Error", "El costo debe ser un número.")
                return

        nueva_cantidad = self.inventario[nombre]["cantidad"] + cantidad_delta
        if nueva_cantidad < 0:
            messagebox.showerror("Error", "Stock no puede ser negativo.")
            return

        self.inventario[nombre]["cantidad"] = nueva_cantidad
        self.actualizar_tabla()
        self.nombre_mod_var.set("")
        self.cantidad_mod_var.set("")
        self.costo_mod_var.set("")

    def eliminar_producto(self):
        seleccionado = self.tabla.selection()
        if not seleccionado:
            messagebox.showinfo("Info", "Selecciona un producto de la tabla.")
            return

        nombre = self.tabla.item(seleccionado[0], "values")[0]
        confirm = messagebox.askyesno("Eliminar", f"¿Eliminar '{nombre}' del inventario?")
        if confirm:
            del self.inventario[nombre]
            self.actualizar_tabla()

    def actualizar_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        for nombre, data in self.inventario.items():
            self.tabla.insert("", "end", values=(nombre, data["cantidad"], f"${data['costo']:.2f}"))

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = InventarioTiendaApp(root)
    root.mainloop()