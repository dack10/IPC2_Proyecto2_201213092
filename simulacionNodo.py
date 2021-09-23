class NodoSimulacion:
    def __init__(self,id,producto,nombreSimulacion):
        self.nombreSimulacion=nombreSimulacion
        self.id =id
        self.producto = producto
        self.siguiente = None