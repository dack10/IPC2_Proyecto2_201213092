from Nodo_Linea_Produccion import Nodo
from Lista_Linea_Produccion import Linea_Produccion
from Nodo_Componente import Nodo_C

class Lista:
    def __init__(self):
        self.lineas = Linea_Produccion()
    
    def insercion(self,linea,componente):

        nuevo = Nodo_C(linea,componente)

        linea = self.lineas.getLinea(linea)
        if linea == None:
            linea = Nodo(linea)
            linea.abajo=nuevo
            self.linea.setLinea(linea)
        else:
            actual=linea.abajo
            if actual.siguiente==None:
                actual.siguiente =nuevo
                nuevo.anterior=actual

    
    """def insertar(self,componente):
        
        if self.inicio==None:
            nuevo = Nodo_C(componente)
            self.inicio=nuevo
            self.fin=nuevo
        else:
            nuevo = Nodo_C(componente)
            self.fin.siguiente=nuevo
            nuevo.anterior=self.fin
            self.fin=nuevo
    """
    def recorrer(self):
        if self.head!=None:
            aux = self.head
            while aux!=None:
                print(str(aux.lista))
                aux= aux.siguiente
            
    

   
