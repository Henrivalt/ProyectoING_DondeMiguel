import tkinter as tk
from tkinter import ttk, messagebox

class VentasApp:
    def __init__(self, root):
        self.root = root
        self.root.columnconfigure(0,weight=1)
        self.root.rowconfigure(0,weight=1)

        frame = tk.Frame(self.root,bg='white')
        frame.grid(row=0,column=0)

        # Productos disponibles (simulados, normalmente vendrían de una base de datos o inventario)
        self.productos = {
            "Pan": {"precio": 0.50, "stock": 100},
            "Leche": {"precio": 1.20, "stock": 50},
            "Arroz": {"precio": 0.90, "stock": 75},
            "Azúcar": {"precio": 1.10, "stock": 40}
        }

        # Carrito de compras
        self.carrito = []

        # Menú desplegable de productos
        tk.Label(frame, text="Producto",bg='white').grid(row=0, column=0)
        self.producto_var = tk.StringVar()
        self.producto_menu = ttk.Combobox(frame, textvariable=self.producto_var, values=list(self.productos.keys()), state="readonly")
        self.producto_menu.grid(row=0, column=1)

        # Cantidad
        tk.Label(frame, text="Cantidad",bg='white').grid(row=1, column=0)
        self.cantidad_var = tk.StringVar()
        tk.Entry(frame, textvariable=self.cantidad_var).grid(row=1, column=1)

        # Botón para agregar al carrito
        tk.Button(frame, text="Agregar al Carrito", command=self.agregar_al_carrito).grid(row=2, column=0, columnspan=2, pady=5)

        # Tabla del carrito
        self.tabla = ttk.Treeview(frame, columns=("Producto", "Cantidad", "Precio", "Total"), show='headings')
        self.tabla.heading("Producto", text="Producto")
        self.tabla.heading("Cantidad", text="Cantidad")
        self.tabla.heading("Precio", text="Precio Unitario")
        self.tabla.heading("Total", text="Total")
        self.tabla.grid(row=3, column=0, columnspan=2, pady=10)

        # Total de la venta
        self.total_var = tk.StringVar(value="Total: $0.00")
        tk.Label(frame, textvariable=self.total_var, font=("Arial", 12, "bold"),bg='white').grid(row=4, column=0, columnspan=2)

        # Botón para confirmar venta
        tk.Button(frame, text="Confirmar Venta", command=self.confirmar_venta, bg="green", fg="white").grid(row=5, column=0, columnspan=2, pady=10)

    def agregar_al_carrito(self):
        producto = self.producto_var.get()
        try:
            cantidad = int(self.cantidad_var.get())
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número entero.")
            return

        if producto == "" or cantidad <= 0:
            messagebox.showerror("Error", "Selecciona un producto y una cantidad válida.")
            return

        if cantidad > self.productos[producto]["stock"]:
            messagebox.showerror("Error", f"No hay suficiente stock. Disponible: {self.productos[producto]['stock']}")
            return

        precio = self.productos[producto]["precio"]
        total = precio * cantidad

        self.carrito.append({
            "producto": producto,
            "cantidad": cantidad,
            "precio": precio,
            "total": total
        })

        self.actualizar_tabla()

        self.cantidad_var.set("")

    def actualizar_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        total_venta = 0
        for item in self.carrito:
            self.tabla.insert("", "end", values=(
                item["producto"],
                item["cantidad"],
                f"${item['precio']:.2f}",
                f"${item['total']:.2f}"
            ))
            total_venta += item["total"]

        self.total_var.set(f"Total: ${total_venta:.2f}")

    def confirmar_venta(self):
        if not self.carrito:
            messagebox.showinfo("Información", "No hay productos en el carrito.")
            return

        # Descontar stock
        for item in self.carrito:
            self.productos[item["producto"]]["stock"] -= item["cantidad"]

        resumen = "\n".join([
            f"{item['producto']} x{item['cantidad']} - ${item['total']:.2f}"
            for item in self.carrito
        ])
        total = sum([item["total"] for item in self.carrito])
        messagebox.showinfo("Venta Confirmada", f"Resumen:\n{resumen}\n\nTOTAL: ${total:.2f}")

        # Limpiar carrito
        self.carrito.clear()
        self.actualizar_tabla()

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = VentasApp(root)
    root.mainloop()
