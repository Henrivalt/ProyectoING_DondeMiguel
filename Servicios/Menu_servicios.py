import tkinter as tk
from Servicios.Gestion import TiendaApp
from Servicios.Inventario import InventarioTiendaApp
from Servicios.Venta import VentasApp
from Servicios.Estadisticas import ReportesEstadisticasApp

class Menu_servicios:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1100x800')
        self.root.title('Donde Miguel')
        #self.root.resizable(False, False)
        self.root.columnconfigure(0,weight=200)
        self.root.columnconfigure(1, weight=900)
        self.root.rowconfigure(0,weight=50)
        self.root.rowconfigure(1,weight=450)
        self.root.attributes('-zoomed', True)

        estilo_frame = {'bg': "white", 'highlightbackground': "#dfe3ee", 'highlightthickness': 1, 'bd': 0}

        estilo_etiqueta = {'font': ('Segoe UI', 12, 'bold'), 'fg': '#1c1e21', 'bg': 'white'}

        estilo_entrada = {'width': 30, 'bg': "#f0f2f5", 'fg': "#1c1e21", 'relief': "flat", 'font': ('Segoe UI', 10),
                          'justify': 'center'}

        estilo_boton = {'bg': "#1877f2", 'fg': "white", 'activebackground': "#145dbf",
                        'activeforeground': "white", 'relief': "flat", 'font': ('Segoe UI', 10, 'bold'),
                        'cursor': "hand2", 'width': 1}

        #------------Frame superior
        frame1 = tk.Frame(self.root,**estilo_frame)
        frame1.grid(row=0,column=0,columnspan=2,sticky='NSEW',padx=1,pady=1)
        frame1.columnconfigure(0,weight=1)
        frame1.rowconfigure(0,weight=1)
        frame1.grid_propagate(False)
        tk.Label(frame1,text='Donde Miguel',font=("Courier New", 30,'bold'),bg='#2e86c1',fg='#f2f4f4').grid(row=0,column=0,sticky='NSEW')

        #------------Frame lateral izquiero
        frame2 = tk.Frame(self.root,**estilo_frame)
        frame2.grid(row=1,rowspan=2,column=0,sticky='NSEW',padx=1,pady=1)
        frame2.columnconfigure(0,weight=1)
        frame2.grid_propagate(False)

        #-----------Botones frame lateral izquierdo
        tk.Button(frame2,text='Gestion de productos',**estilo_boton,command=lambda: self.operaciones(1)).grid(row=0,sticky='NSEW')
        tk.Button(frame2,text='Control de inventario',**estilo_boton,command=lambda: self.operaciones(2)).grid(row=1,sticky='NSEW')
        tk.Button(frame2,text='Compras y ventas',**estilo_boton,command=lambda: self.operaciones(3)).grid(row=2,sticky='NSEW')
        tk.Button(frame2,text='Reportes y estadisticas',**estilo_boton,command=lambda: self.operaciones(4)).grid(row=3,sticky='NSEW')
        tk.Button(frame2,text='Salir',**estilo_boton,command=lambda: self.operaciones(5)).grid(row=4,sticky='NSEW')

        #------------Frame Central -> Funcionalidades
        self.frame3 = tk.Frame(self.root,**estilo_frame)
        self.frame3.grid(row=1,column=1,sticky='NSEW')
        self.frame3.columnconfigure(0,weight=1)
        #self.frame3.columnconfigure(1,weight=1)
        self.frame3.grid_propagate(False)

    def operaciones(self,opcion):
        self.opcion = opcion
        if self.opcion == 1:
            print('opcion1')
            for widget in self.frame3.winfo_children():
                widget.destroy()
            TiendaApp(self.frame3)
        elif self.opcion == 2:
            print('opcion2')
            for widget in self.frame3.winfo_children():
                widget.destroy()
            InventarioTiendaApp(self.frame3)
        elif self.opcion == 3:
            print('opcion3')
            for widget in self.frame3.winfo_children():
                widget.destroy()
            VentasApp(self.frame3)
        elif self.opcion == 4:
            print('opcion4')
            for widget in self.frame3.winfo_children():
                widget.destroy()
            ReportesEstadisticasApp(self.frame3)
        elif self.opcion == 5:
            print('opcion5')
            self.root.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    aplicacion = Menu_servicios(root)
    root.mainloop()