from tkinter import Frame,Label,Button,Toplevel
from libVariables import variables
from ventanas import Ventana

class FrameClientes(Ventana):
    def __init__(self,master):
        super().__init__(master,"clientes")

    def crearWidgets(self):
        Label(self,
        text="Control de clientes y stock v1.0\nClientes",
        font=("Consolas",20),
        bg="lightyellow").pack(fill="x",side='top',pady=5,padx=5)

        self.fr4interno = Frame(self,bg="lightgrey")
        self.fr4interno.pack(expand=True,fill="both")
