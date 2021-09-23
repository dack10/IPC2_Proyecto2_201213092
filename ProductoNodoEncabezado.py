class nodoEncabezado:
    def __init__(self, id,producto):
        self.prod=producto
        self.id = id
        self.siguiente = None
        self.anterior = None
        self.accesoNodo = None