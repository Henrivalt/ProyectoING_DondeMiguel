import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ReportesEstadisticasApp:
    def __init__(self, root):
        self.root = root
        self.root.columnconfigure(0,weight=1)
        self.root.rowconfigure(0,weight=1)

        self.inventario = {}  # Diccionario para productos: nombre -> (cantidad, precio)
        self.compras_realizadas = {}  # Historial de compras: nombre -> cantidad
        self.ventas_realizadas = {}  # Historial de ventas: nombre -> cantidad

        self.crear_widgets()

    def crear_widgets(self):
        style = ttk.Style()
        style.configure("White.TLabelframe", background="white")
        style.configure("White.TLabelframe.Label", background="white")
        style.configure("White.TLabel", background="white")
        # ----- FRAME PARA REPORTES -----
        frame_reportes = ttk.LabelFrame(self.root, text="Reportes y Estadísticas", padding=10, style="White.TLabelframe")
        frame_reportes.grid(row=0,column=0, padx=10, pady=10,sticky='NSEW')

        ttk.Label(frame_reportes, text="Total Compras:",style="White.TLabel").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.total_compras_label = ttk.Label(frame_reportes, text="$0.00",style="White.TLabel")
        self.total_compras_label.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(frame_reportes, text="Total Ventas:",style="White.TLabel").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.total_ventas_label = ttk.Label(frame_reportes, text="$0.00",style="White.TLabel")
        self.total_ventas_label.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(frame_reportes, text="Total Productos Vendidos:",style="White.TLabel").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.total_productos_vendidos_label = ttk.Label(frame_reportes, text="0",style="White.TLabel")
        self.total_productos_vendidos_label.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(frame_reportes, text="Total Productos Comprados:",style="White.TLabel").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.total_productos_comprados_label = ttk.Label(frame_reportes, text="0",style="White.TLabel")
        self.total_productos_comprados_label.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        # Botón para actualizar reportes
        ttk.Button(frame_reportes, text="Actualizar Reportes", command=self.actualizar_reportes).grid(row=4, column=0, columnspan=2, pady=10)

        # ----- FRAME PARA AGREGAR PRODUCTOS -----
        frame_form = ttk.LabelFrame(self.root, text="Agregar Producto", style="White.TLabelframe")
        frame_form.grid(row=1,column=0, padx=10, pady=10,sticky='NSEW')

        ttk.Label(frame_form, text="Nombre:",style="White.TLabel").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.nombre_entry = ttk.Entry(frame_form)
        self.nombre_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Cantidad:",style="White.TLabel").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.cantidad_entry = ttk.Entry(frame_form)
        self.cantidad_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Precio:",style="White.TLabel").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.precio_entry = ttk.Entry(frame_form)
        self.precio_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(frame_form, text="Agregar al inventario", command=self.agregar_producto).grid(row=3, column=0, columnspan=2, pady=10)

        # ----- FRAME PARA COMPRAS Y VENTAS -----
        frame_compras_ventas = ttk.LabelFrame(self.root, text="Operaciones de Compras y Ventas", style="White.TLabelframe")
        frame_compras_ventas.grid(row=2,column=0, padx=10, pady=10,sticky='NSEW')

        ttk.Label(frame_compras_ventas, text="Nombre del Producto:",style="White.TLabel").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.nombre_operacion_entry = ttk.Entry(frame_compras_ventas)
        self.nombre_operacion_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_compras_ventas, text="Cantidad:",style="White.TLabel").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.cantidad_operacion_entry = ttk.Entry(frame_compras_ventas)
        self.cantidad_operacion_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(frame_compras_ventas, text="Comprar", command=self.comprar_producto).grid(row=2, column=0, padx=5, pady=10)
        ttk.Button(frame_compras_ventas, text="Vender", command=self.vender_producto).grid(row=2, column=1, padx=5, pady=10)

    def agregar_producto(self):
        nombre = self.nombre_entry.get().strip()
        cantidad = self.cantidad_entry.get().strip()
        precio = self.precio_entry.get().strip()

        if not nombre or not cantidad or not precio:
            messagebox.showwarning("Campos vacíos", "Todos los campos son obligatorios.")
            return

        try:
            cantidad = int(cantidad)
            precio = float(precio)
        except ValueError:
            messagebox.showerror("Error", "Cantidad debe ser número entero y precio un número decimal.")
            return

        # Agregar o actualizar el producto en el inventario
        if nombre in self.inventario:
            self.inventario[nombre] = (self.inventario[nombre][0] + cantidad, precio)
        else:
            self.inventario[nombre] = (cantidad, precio)

        messagebox.showinfo("Producto agregado", f"Producto '{nombre}' agregado al inventario.")
        self.limpiar_campos()

    def comprar_producto(self):
        nombre = self.nombre_operacion_entry.get().strip()
        cantidad = self.cantidad_operacion_entry.get().strip()

        if not nombre or not cantidad:
            messagebox.showwarning("Campos vacíos", "Debes completar el nombre y la cantidad.")
            return

        try:
            cantidad = int(cantidad)
        except ValueError:
            messagebox.showerror("Error", "Cantidad debe ser un número entero.")
            return

        if nombre not in self.inventario:
            messagebox.showerror("Producto no encontrado", f"El producto '{nombre}' no existe en el inventario.")
            return

        # Aumentar cantidad en inventario
        cantidad_actual, precio = self.inventario[nombre]
        self.inventario[nombre] = (cantidad_actual + cantidad, precio)

        # Registrar compra
        if nombre in self.compras_realizadas:
            self.compras_realizadas[nombre] += cantidad
        else:
            self.compras_realizadas[nombre] = cantidad

        messagebox.showinfo("Compra exitosa", f"Se han comprado {cantidad} unidades de '{nombre}'.")
        self.actualizar_reportes()

    def vender_producto(self):
        nombre = self.nombre_operacion_entry.get().strip()
        cantidad = self.cantidad_operacion_entry.get().strip()

        if not nombre or not cantidad:
            messagebox.showwarning("Campos vacíos", "Debes completar el nombre y la cantidad.")
            return

        try:
            cantidad = int(cantidad)
        except ValueError:
            messagebox.showerror("Error", "Cantidad debe ser un número entero.")
            return

        if nombre not in self.inventario:
            messagebox.showerror("Producto no encontrado", f"El producto '{nombre}' no existe en el inventario.")
            return

        cantidad_actual, precio = self.inventario[nombre]
        if cantidad > cantidad_actual:
            messagebox.showerror("Cantidad insuficiente", f"No hay suficientes unidades de '{nombre}' para vender.")
            return

        # Disminuir cantidad en inventario
        self.inventario[nombre] = (cantidad_actual - cantidad, precio)

        # Registrar venta
        if nombre in self.ventas_realizadas:
            self.ventas_realizadas[nombre] += cantidad
        else:
            self.ventas_realizadas[nombre] = cantidad

        messagebox.showinfo("Venta exitosa", f"Se han vendido {cantidad} unidades de '{nombre}'.")
        self.actualizar_reportes()

    def actualizar_reportes(self):
        total_compras = sum([self.inventario[nombre][0] * self.inventario[nombre][1] for nombre in self.compras_realizadas])
        total_ventas = sum([self.ventas_realizadas[nombre] * self.inventario[nombre][1] for nombre in self.ventas_realizadas])

        # Actualizar las etiquetas de los reportes
        self.total_compras_label.config(text=f"${total_compras:.2f}")
        self.total_ventas_label.config(text=f"${total_ventas:.2f}")
        self.total_productos_vendidos_label.config(text=str(sum(self.ventas_realizadas.values())))
        self.total_productos_comprados_label.config(text=str(sum(self.compras_realizadas.values())))

    def limpiar_campos(self):
        self.nombre_entry.delete(0, tk.END)
        self.cantidad_entry.delete(0, tk.END)
        self.precio_entry.delete(0, tk.END)
        self.nombre_operacion_entry.delete(0, tk.END)
        self.cantidad_operacion_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ReportesEstadisticasApp(root)
    root.mainloop()
