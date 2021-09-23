class Nodo:
    def __init__(self, fila, columna, valor,producto):
        self.producto=producto
        self.fila = fila
        self.columna = columna
        self.valor = valor
        self.derecha = None
        self.izquierda = None
        self.arriba = None 
        self.abajo = None