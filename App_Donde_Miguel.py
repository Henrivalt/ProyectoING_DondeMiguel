import tkinter as tk
from tkinter import messagebox
from Servicios.Menu_servicios import Menu_servicios

class DondeMiguel:
    def __init__(self, root):
        self.root = root
        self.root.title('Login')
        self.root.resizable(False, False)
        width = 400
        height = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        self.root.geometry(f'{width}x{height}+{x}+{y}')

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

        estilo_frame = {'bg': "white", 'highlightbackground': "#dfe3ee", 'highlightthickness': 1, 'bd': 0}

        estilo_etiqueta = {'font': ('Segoe UI', 12, 'bold'), 'fg': '#1c1e21', 'bg': 'white'}

        estilo_entrada = {'width': 30, 'bg': "#f0f2f5", 'fg': "#1c1e21", 'relief': "flat", 'font': ('Segoe UI', 10),
                          'justify': 'left'}

        estilo_boton = {'bg': "#1877f2", 'fg': "white", 'activebackground': "#145dbf",
                        'activeforeground': "white", 'relief': "flat", 'font': ('Segoe UI', 10, 'bold'),
                        'cursor': "hand2", 'width': 20}

        frame1 = tk.Frame(self.root,**estilo_frame)
        frame1.grid(row=0, sticky=tk.NSEW)
        frame1.columnconfigure(0, weight=1)
        frame1.rowconfigure(0,weight=1)

        tk.Label(frame1,text='Donde Miguel',bg='#145dbf',font=('Segoe UI', 30,'bold'),fg='white').grid(sticky='NSEW')

        frame2 = tk.Frame(self.root,**estilo_frame)
        frame2.grid(row=1, sticky=tk.NSEW)
        frame2.columnconfigure(0, weight=1)
        frame2.columnconfigure(1, weight=1)

        tk.Label(frame2, text='Usuario',**estilo_etiqueta).grid(row=0, column=0)
        tk.Label(frame2, text='Password',**estilo_etiqueta).grid(row=1, column=0)

        self.usuario = tk.Entry(frame2,**estilo_entrada)
        self.usuario.grid(row=0,column=1,padx=5,pady=5)
        self.usuario.focus()
        self.contrasenia = tk.Entry(frame2,show='*',**estilo_entrada)
        self.contrasenia.grid(row=1,column=1,padx=5,pady=5)

        # Evento para presionar Enter
        root.bind('<Return>', self.evento_ingresar)

        # ---Botones
        btn1 = tk.Button(frame2,text='Ingresar',command=self.evento_ingresar,**estilo_boton)
        btn1.grid(row=2,column=0,pady=5,padx=5,columnspan=2)

    def evento_ingresar(self, event=None):
        # Diccionario de usuarios válidos
        usuarios_validos = {
            "admin": "1234",
            "henry": "pass123",
            "juan": "clave456",
            "sergio": "abc123",
        }

        usuario = self.usuario.get()
        clave = self.contrasenia.get()

        # Verifica si el usuario existe y la clave coincide
        if usuario in usuarios_validos and usuarios_validos[usuario] == clave:
            messagebox.showinfo("Bienvenido", f"Hola {usuario}, acceso concedido.")
            root.destroy()
            # pasamos al menu
            menu = tk.Tk()
            aplicacion = Menu_servicios(menu)
            menu.mainloop()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")


if __name__ == '__main__':
    root = tk.Tk()
    aplicacion = DondeMiguel(root)
    root.mainloop()