from Nodo_C import *
class Linea_Produccion:
    def __init__(self):
        self.inicio=None
        self.fin = None
    

    def insertar_componente(self,componente):
        if self.inicio==None:
            nuevo = Nodo_C(componente)
            self.inicio=nuevo
            self.fin=nuevo
        else:
            nuevo = Nodo_C(componente)
            self.fin.siguiente=nuevo
            nuevo.anterior=self.fin
            self.fin=nuevo
            
    
