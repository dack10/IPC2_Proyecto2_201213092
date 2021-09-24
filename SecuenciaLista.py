from SecuenciaNodo import Nodo
from ProductoEncabezado import listaEncabezado
from ProductoNodoEncabezado import nodoEncabezado

class matriz_SecuenciaProducto:
    
    def __init__(self):
        self.eFilas = listaEncabezado()
        self.eColumnas = listaEncabezado() 
    
    def insertar(self, fila, columna, valor,producto):
        nuevo = Nodo(fila, columna, valor,producto)

        
        eFila = self.eFilas.getEncabezado(fila)
        if eFila == None:                         
            eFila = nodoEncabezado(fila,producto)            
            eFila.accesoNodo = nuevo
            self.eFilas.setEncabezado(eFila)        
        else:                                       
            if nuevo.columna < eFila.accesoNodo.columna: 
                nuevo.derecha = eFila.accesoNodo     
                eFila.accesoNodo.izquierda = nuevo
                eFila.accesoNodo = nuevo
            else:
                actual = eFila.accesoNodo
                while actual.derecha != None:
                    if nuevo.columna < actual.derecha.columna:
                        nuevo.derecha = actual.derecha 
                        actual.derecha.izquierda = nuevo
                        nuevo.izquierda = actual
                        actual.derecha = nuevo
                        break
                    actual = actual.derecha
                
                if actual.derecha == None:
                    actual.derecha = nuevo          
                    nuevo.izquierda = actual
        

        
        eColumna = self.eColumnas.getEncabezado(columna)
        if eColumna == None:                          
            eColumna = nodoEncabezado(columna,producto)            
            eColumna.accesoNodo = nuevo
            self.eColumnas.setEncabezado(eColumna)        
        else:                                      
            if nuevo.fila < eColumna.accesoNodo.fila: 
                nuevo.abajo = eColumna.accesoNodo      
                eColumna.accesoNodo.arriba = nuevo
                eColumna.accesoNodo = nuevo
            else:
                actual = eColumna.accesoNodo
                while actual.abajo != None:
                    if nuevo.fila < actual.abajo.fila:
                        nuevo.abajo = actual.abajo  
                        actual.abajo.arriba = nuevo
                        nuevo.arriba = actual
                        actual.abajo = nuevo
                        break
                    actual = actual.abajo
                
                if actual.abajo == None:
                    actual.abajo = nuevo        
                    nuevo.arriba = actual
                       

    def recorrerFilas(self):
        eFila = self.eFilas.primero
        print("\n****************** Recorrido por filas ******************")

        while eFila != None:

            actual = eFila.accesoNodo
            print("\nFila "+str(actual.fila))
            print("Columna   Valor")
            while actual != None:
                print(str(actual.columna)+"         "+actual.valor)
                actual = actual.derecha
            
            eFila = eFila.siguiente        
        print("****************** Fin recorrido por filas ******************\n")


    def recorrerColumnas(self):
        eColumna = self.eColumnas.primero
        print("\n****************** Recorrido por columnas ******************")

        while eColumna != None:
            
            actual = eColumna.accesoNodo
            print("\nColumna "+str(actual.columna)+"PRODUCTO "+str(actual.producto))
            print("Fila   Valor")
            while actual != None:
                print(str(actual.fila)+"      "+actual.valor)
                actual = actual.abajo
            
            eColumna = eColumna.siguiente            
        print("****************** Fin recorrido por columnas ******************\n")
    
    def obtenerSecuencia(self,fila,producto): #obtiene el valor de secuencia segun fila y segun el producto
        prod = self.eColumnas.primero
        while prod!=None:
                actual = prod.accesoNodo
                while actual!=None:
                    if actual.producto==producto and actual.fila==fila:
                        return actual.valor
                    else:
                        actual=actual.abajo
                prod=prod.siguiente

    def cantidadElementos(self,producto): # cantidad de la secuencia del producto
        contador=0
        prodd = self.eColumnas.primero
        while prodd!=None:
            actual=prodd.accesoNodo
            while actual!=None:
                if actual.producto==producto:
                    contador=contador+1
                actual=actual.abajo
            prodd=prodd.siguiente
            print("cantidad de elementos: "+str(contador))
        return contador          
            