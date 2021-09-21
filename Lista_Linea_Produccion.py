from Nodo_Linea_Produccion import Nodo
from Nodo_Componente import Nodo_C

class Linea_Produccion:
    def __init__(self,inicio=None):
        self.inicio=inicio
       
    def setLinea(self,linea):
        if self.inicio ==None:
            self.inicio=linea
        elif linea.linea < self.inicio.linea:
            linea.siguiente = self.inicio
            self.inicio=linea
        else:
            actual = self.inicio
            while actual.siguiente!=None:
                if linea.linea<actual.siguiente.linea:
                    linea.siguiente =actual.siguiente
                    actual.siguiente=linea
                    break
                actual=actual.siguiente
            if actual.siguiente==None:
                actual.siguiente=linea
            

            
    def getLinea(self,linea):
        actual=self.inicio
        while actual!=None:
            if actual.linea==linea:
                return actual
            actual=actual.siguiente
        return None

