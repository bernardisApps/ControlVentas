from tkinter import Frame,Label,Button,Entry,Toplevel,Listbox,PhotoImage
from libVariables import variables
from ventanas import Ventana


class FrameProductos (Ventana):
    def __init__(self,master):
        super().__init__(master,"productos")

    def crearWidgets(self):

        self.mainFrame = Frame(self,bg="lightgrey")
        self.mainFrame.pack(expand=True,fill="both",pady=5,padx=5)

        self.img_buscar = PhotoImage(file="search-line.png")

        Label(self.mainFrame,
        text="Control de clientes y stock v1.0\nProductos",
        font=("Consolas",20),
        bg="lightyellow").pack(fill="x")

        self.searchFrame = Frame(self.mainFrame,bg="lightgrey",bd=2,relief="groove")
        self.searchFrame.pack(expand=True,fill="both")

        self.lbl_buscar = Label(self.searchFrame,bg="lightgrey",text="Buscar: ",font=("Consolas",15))
        self.lbl_buscar.place(x=10,y=10)

        self.txt_buscar = Entry(self.searchFrame,width=50)
        self.txt_buscar.place(x=90,y=15)

        self.btn_buscar = Button(self.searchFrame,text="Buscar",borderwidth=0,image=self.img_buscar,bg="lightgrey")
        self.btn_buscar.place(x=400,y=10)

        self.lista = Listbox(self.searchFrame,width=68,height=21)
        self.lista.place(x=10,y=50)

        self.optionFrame = Frame(self.searchFrame,bd=2,relief="groove",bg="lightgrey",width=190,height=341)
        self.optionFrame.place(x=430,y=50)

        self.btn_nuevo = Button(self.optionFrame,text="Nuevo",width=20)
        self.btn_nuevo.place(x=20,y=30)

        self.btn_editar = Button(self.optionFrame,text="Editar",width=20)
        self.btn_editar.place(x=20,y=60)

        self.btn_eliminar = Button(self.optionFrame,text="Eliminar",width=20)
        self.btn_eliminar.place(x=20,y=90)


