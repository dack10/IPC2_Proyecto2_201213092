from simulacionNodo import *

class listaSimulacion:
    def __init__(self):
        self.inicio = None
        self.fin = None
    
    def insertar(self, id,producto,nombreSimulacion):
        if self.inicio == None:
            self.inicio = NodoSimulacion(id,producto,nombreSimulacion)
            self.fin = self.inicio
        else:
            nuevo = NodoSimulacion(id,producto,nombreSimulacion)
            self.fin.siguiente = nuevo
            self.fin = nuevo
    
    def recorrer(self):
        if self.inicio != None:
            aux = self.inicio
            while aux!= None:
                print(str(aux.id), aux.producto,aux.nombreSimulacion)
                aux = aux.siguiente

    def cantidadElementos(self):
        contador=0
        if self.inicio!=None:
            aux=self.inicio
            while aux!=None:
                contador=contador+1
                aux=aux.siguiente
            print("cantidad de elementos   "+str(contador))
            return contador

    def verificar(self,id):
        if self.inicio!=None:
            aux =self.inicio
            while aux!=None:
                if aux.id==id:
                    return aux.producto
                aux = aux.siguiente

    def modificar(self,id,producto):
        if self.inicio != None:
            aux = self.inicio
            while aux!= None:
                if aux.id==id:
                    aux.producto = producto
                    break
                aux = aux.siguiente
    def eliminar(self,id):
        if self.inicio != None:
            if self.inicio.id==id and self.inicio.siguiente==None:
                self.inicio = None
                self.fin=None
            elif self.inicio.id==id:
                self.inicio = self.inicio.siguiente
            else:
                aux= self.inicio.siguiente
                aux2=self.inicio
                while aux !=None:
                    if aux.id==id and aux != self.fin:
                        aux2.siguiente= aux.siguiente
                        break
                    elif aux.id == id:
                        aux2.siguiente = None
                        self.fin = aux2
                        break
                    aux2 = aux
                    aux = aux.siguiente
                        