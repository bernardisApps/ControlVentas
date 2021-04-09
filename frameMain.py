from tkinter import Frame,Label,Button,Tk
from frameVenta import FrameVenta
from frameProductos import FrameProductos
from frameClientes import FrameClientes
from libVariables import variables

class FrameMain (Frame):

    def __init__(self,master=None):
        super().__init__(master,bg="lightgrey")
        self.master = master
        self.pack(expand=True,fill="both",pady=5,padx=5)
        self.crearWidgets()


    def accionMenu (self,arg):
        if(arg=="venta"):
            if variables.estadoVenta == 0:
                self.frVenta = FrameVenta(self.master)
                variables.estadoVenta = 1
        elif(arg=="productos"):
            if variables.estadoProductos == 0:
                self.frProductos = FrameProductos(self.master)
                variables.estadoProductos = 1
        elif(arg=="clientes"):
            if variables.estadoClientes == 0:
                self.frClientes = FrameClientes(self.master)
                variables.estadoClientes = 1


    def crearWidgets(self):
        Label(self,
        text="Control de clientes y stock v1.0",
        font=("Consolas",20),
        bg="lightyellow").pack(fill="x",side='top',pady=(0,5))


        #frame de 320x240
        self.frameInterno = Frame(self,bg="gray")
        self.frameInterno.config(bd=5,relief="sunken")
        self.frameInterno.pack(pady=(30,0))

        self.btnVenta = Button(self.frameInterno,text="Venta",font=("Verdana",15),width=12,height=5,bg="yellow")
        self.btnVenta.grid(column=0,row=0,pady=(10,5),padx=(10,5))
        self.btnVenta.config(command=lambda:self.accionMenu("venta"))

        self.btnProductos = Button(self.frameInterno,text="Productos",font=("Verdana",15),width=12,height=5,bg="lightblue")
        self.btnProductos.grid(column=1,row=0,pady=(10,5),padx=(5,10))
        self.btnProductos.config(command=lambda:self.accionMenu("productos"))

        self.btnClientes = Button(self.frameInterno,text="Clientes",font=("Verdana",15),width=12,height=5,bg="lightblue")
        self.btnClientes.grid(column=0,row=1,pady=(5,10),padx=(10,5))
        self.btnClientes.config(command=lambda:self.accionMenu("clientes"))

        self.btnSalir = Button(self.frameInterno,text="Salir",font=("Verdana",15),width=12,height=5,bg="red",fg="white",command=self.master.destroy)
        self.btnSalir.grid(column=1,row=1,pady=(5,10),padx=(5,10))
