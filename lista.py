from Nodo import Nodo
from Linea_Produccion import Linea_Produccion

class Lista:
    def __init__(self):
        self.head = None
        self.fin=None
    
    def insertar(self,dato):
        if self.head==None:
            self.head=Nodo(dato)
            self.fin=self.head
        else:
            nuevo=Nodo(dato)
            self.fin.siguiente=nuevo
            self.fin=nuevo
    
    def recorrer(self):
        if self.head!=None:
            aux = self.head
            while aux!=None:
                print(str(aux.lista))
                aux= aux.siguiente
    

    def crearListaProduccion(self):
        lista=Linea_Produccion()
