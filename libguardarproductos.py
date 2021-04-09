import pickle

class guardar:
    def __init__(self,producto,descripciones):
        self.producto = producto
        self.descripciones = descripciones
        self.filename = "productos"
        self.dicProductos = {}
        self.guardado()

    def guardado (self):
        try:
            self.fichero = open(self.filename,"rb")
            self.fichero.close()
            try:
                self.fichero = open(self.filename,"rb")
                self.dicProductos = pickle.load(self.fichero)
                self.fichero.close()
                self.fichero = open(self.filename,"wb")
                self.dicProductos[self.producto] = self.descripciones
                pickle.dump(self.dicProductos,self.fichero)
                self.fichero.close()
            except:
                pass
        except:
            self.fichero = open(self.filename,"wb")
            self.fichero.close()
            try:
                self.fichero = open(self.filename,"wb")
                self.dicProductos[self.producto] = self.descripciones
                pickle.dump(self.dicProductos,self.fichero)
                self.fichero.close()
            except:
                pass

class leer:
    def __init__(self,producto):
        self.producto = producto
        self.filename = "productos"
        self.descProducto = self.leerProducto()

    def __str__(self):
        return f"{self.descProducto}"

    def leerProducto(self):
        try:
            self.fichero = open(self.filename,"rb")
            self.lectura = pickle.load(self.fichero)
        
            if self.producto in self.lectura:
                return self.lectura[self.producto]
            else:
                return 0

            self.fichero.close()
        except:
            return 0

class borrar:
    def __init__(self,producto):
        self.producto = producto
        self.filename = "productos"

        if self.producto == "todos":
            self.productoBorrado = self.borrarTodosProductos()
        else:
            self.productoBorrado = self.borrarProductos()

    def __str__(self):
        return f"{self.productoBorrado}"

    def borrarProductos(self):
        try:
            self.fichero = open(self.filename,"rb")
            self.lectura = pickle.load(self.fichero)
            self.fichero.close()

            if self.producto in self.lectura:
                del self.lectura[self.producto]
                self.fichero = open(self.filename,"wb")
                pickle.dump(self.lectura,self.fichero)
                self.fichero.close()
                return 1
            else:
                return 0
        except:
            return 0

    def borrarTodosProductos(self):
        self.dicBorrar = {}
        try:
            self.fichero = open(self.filename,"wb")
            pickle.dump(self.dicBorrar,self.fichero)
            self.fichero.close()
            return 1
        except:
            return 0

