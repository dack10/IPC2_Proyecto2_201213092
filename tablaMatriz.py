from tkinter.constants import NONE
from tablaEncabezado import tablaEncabezado
from tablaNodoEncabezado import tablaNodoEncabezado
from tablaNodoMatriz import tablaNodoMatriz

class Tablamatriz:
    
    def __init__(self):
        self.eFilas = tablaEncabezado()  
        self.eColumnas = tablaEncabezado() 
    
    def insertar(self, fila, columna, valor,estado):
        nuevo = tablaNodoMatriz(fila, columna, valor,estado)
    
        eFila = self.eFilas.getEncabezado(fila)
        if eFila == None:                          
            eFila = tablaNodoEncabezado(fila)            
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
            eColumna = tablaNodoEncabezado(columna)           
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
            print("\nColumna "+str(actual.columna))
            print("Fila   Estado        Valor")
            while actual != None:
                print(str(actual.fila)+"      "+actual.estado + "      "+str(actual.valor))
                actual = actual.abajo
            
            eColumna = eColumna.siguiente            
        print("****************** Fin recorrido por columnas ******************\n")

    def cantidadLineas(self):
        columna=self.eColumnas.primero
        contador=0
        while columna!=None:
            contador=contador+1
            columna=columna.siguiente
        return contador
    
    def igualMayorMenor(self,linea,componente):
        if self.eColumnas.primero!=None:
            aux = self.eColumnas.primero
            while aux!=None:
                if aux.id==linea:
                    aux2=aux.accesoNodo
                    while aux2!=None:
                        if aux2.valor==componente:
                            return int(2)
                        elif aux2.valor<componente:
                            return int(1)
                        elif aux2.valor>componente:
                            return int(0)
                else:
                    aux=aux.siguiente
    
    def obtenerUltimoValor(self,linea):
        if self.eColumnas.primero!=None:
            aux=self.eColumnas.primero
            while aux!=None:
                if aux.id==linea:
                    aux2=aux.accesoNodo
                    while aux2!=None:
                        if aux2.abajo==None:
                            return int(aux2.valor)
                        else:
                            aux2=aux2.abajo
                else:
                    aux=aux.siguiente

    def obtenerFilaUltimoValor(self,columna):
        if self.eColumnas.primero!=None:
            aux=self.eColumnas.primero
            while aux!=None:
                if aux.id==columna:
                    aux2=aux.accesoNodo
                    while aux2!=None:
                        if aux2.abajo==None:
                            return aux2.fila
                        aux2=aux2.abajo

    
    def obtenerEstado(self,linea):
        if self.eColumnas.primero!=None:
            aux=self.eColumnas.primero
            while aux!=None:
                if aux.id==linea:
                    aux2=aux.accesoNodo
                    while aux2!=None:
                        if aux2.siguiente==None:
                            return 0
    
    def existeFilaSiguiente(self,fila):
        if self.eFilas.primero!=None:
            aux=self.eFilas.primero
            while aux!=None:
                if aux.id == fila:
                    return True
                aux=aux.siguiente
            return False
                
    def traerEstadoValor(self,fila,columna):
        if self.eColumnas.primero!=None:
            aux=self.eColumnas.primero
            while aux!=None:
                if aux.id==columna:
                    aux2=aux.acceosoNodo
                    while aux2!=None:
                        if aux2.fila==fila:
                            fil=aux2.valor
                            estado=aux2.estado
                            resultado=str(estado+" "+fil)
                            return resultado
    
    def valorColumna(self):
        if self.eColumnas.primero!=None:
            aux=self.eColumnas.primero
            while aux!=None:
                if aux.siguiente==None:
                    return aux.id
                aux=aux.siguiente
    def valorFila(self):
        if self.eFilas.primero!=None:
            aux=self.eFilas.primero
            while aux!=None:
                if aux.siguiente==None:
                    return aux.id
                aux=aux.siguiente
                            




     

