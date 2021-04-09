from tkinter import Frame,Button,Label,Toplevel
#from frameMain import FrameMain
from libVariables import variables
from ventanas import Ventana

class FrameVenta(Ventana):
    
    def __init__(self,master):
        super().__init__(master,"venta")
        
    def crearWidgets(self):
        Label(self,
        text="Control de clientes y stock v1.0\nVentas",
        font=("Consolas",20),
        bg="lightyellow").pack(fill="x",side='top',pady=5,padx=5)

        self.fr2interno = Frame(self,bg="lightgrey")
        self.fr2interno.pack(expand=True,fill="both")