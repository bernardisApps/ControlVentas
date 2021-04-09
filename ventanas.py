from tkinter import Toplevel
from libVariables import variables

class Ventana (Toplevel):
    def __init__(self,master,seccion):
        self.seccion = seccion
        super().__init__(master,bg="lightgrey")
        self.resizable(False,False)
        self.minsize(width=640, height=480)
        self.title(self.seccion)
        self.protocol("WM_DELETE_WINDOW", self.cerrar)
        self.bind('<Escape>', self.on_closing)
        self.crearWidgets()

    def cerrar (self):
        self.on_closing(self.seccion)

    def on_closing(self,event):
        if self.seccion == "productos":
            variables.estadoProductos = 0
            self.destroy()
        elif self.seccion == "venta":
            variables.estadoVenta = 0
            self.destroy()
        elif self.seccion == "clientes":
            variables.estadoClientes = 0
            self.destroy()

    def crearWidgets(self):
        pass