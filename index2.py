from os import name, system,startfile
import os
from sys import winver
from tablaNodoMatriz import tablaNodoMatriz
from Lista_Linea_Produccion import listaEncabezado
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
from tkinter import filedialog
import xml.etree.ElementTree as xml
import re
from simulacionLista import listaSimulacion
from Lista_componentes import matriz
from SecuenciaLista import matriz_SecuenciaProducto
from tablaMatriz import Tablamatriz

mat = matriz()
secuencias = matriz_SecuenciaProducto()
productos=listaSimulacion()
tabla = Tablamatriz()


def abrir():
    messagebox.showinfo(title="Mensaje",message="hola")

def generarSalidaXML():
    for item in listaProductos.curselection():
        nombreP=str(listaProductos.get(item))
        messagebox.showinfo(title="verificar",message=nombreP)
        
    root = xml.Element("SalidaSimulacion")
    salto=xml.SubElement(root,"\n")
    doc = xml.SubElement(root,"Nombre")
    productos.recorrer()
    nombreSIMULACION=productos.obtenerNombreSimulacion("SmartWatch")
    doc.text=nombreSIMULACION
    print(nombreSIMULACION)
    nodo1=xml.SubElement(root,"ListadoProductos")
    nodo1.text="texto de nodo 1"
    xml.SubElement(root,"nodo2",atributo="algo").text="texto2"
    arbol=xml.ElementTree(root)
    arbol.write("prueba.xml")

def obtenerTiempo():
    #Llenar todas las filas con el componente 1
    lineass=int(mat.cantidadLineas())
    for num in range(0,lineass+1):
        if num==0:
            tabla.insertar(1,num,1,"TIEMPO")
        elif num>0:    
            tabla.insertar(1,num,1,"MOVER A: ")
    tabla.recorrerColumnas()
    #fin de llenar 

    for item in listaProductos.curselection():
        productoSeleccionado=listaProductos.get(item) #producto seleccionado para generar el tiempo

    print(secuencias.obtenerSecuencia(1,productoSeleccionado))
    cantidadElementosSecuencia=int(secuencias.cantidadElementos(productoSeleccionado))
    contador = 2
    for n in range(1,cantidadElementosSecuencia+1):
        sec= secuencias.obtenerSecuencia(n,productoSeleccionado)
        print(str(sec))
        lin = re.search(r"\bL\d+",str(sec))
        lin2=lin.group() #Linea de la secuencia
        print("Linea numero: "+str(lin2))
        linNum = re.sub(r"\bL","",str(lin2))
        linNumm=int(linNum)#Numero de la linea
        con=re.search(r"\wC\d+",str(sec))
        con2=con.group()
        con3=re.sub(r"\bp","",str(con2))        
        con4=str(con3) #componente de secuencia
        con5=re.sub(r"\bC","",str(con4))
        con6=int(con5) #numero de componente de la secuencia
        print("Numero de componente"+str(con6))
        
        #N= tabla.igualMayorMenor(linNumm,con6)
        M=tabla.obtenerUltimoValor(linNumm)
        print(M)
        b=True
        
        while b!=False:
            print("si entro")
            M=tabla.obtenerUltimoValor(linNumm)
            if M==con6:
                print("entro en igual")
                bo=tabla.existeFilaSiguiente(contador)
                print(bo)
                if bo ==True:
                    contador=contador+1
                elif bo==False:
                    tabla.insertar(contador,linNumm,tabla.obtenerUltimoValor(linNumm),"ENSAMBLAR C")
                        #tabla.insertar(4,linNumm+1,0,"NO") 
                    b=False   
                    contador = 2
                    tabla.recorrerColumnas()
            else:
                if M<con6:
                    tabla.insertar(contador,linNumm,tabla.obtenerUltimoValor(linNumm)+int(1),"MOVER A: ")
                    contador=contador+1
                    b=True
                    print("aqui entro en componente es mayor a ultimo elemento")
                    tabla.recorrerColumnas()
                elif M>con6:
                    tabla.insertar(contador,linNumm,tabla.obtenerUltimoValor(linNumm)-int(1),"MOVER A: ")
                    print("aqui entro en componente es menor que ultimo elemento")
                    contador = contador +1
                    tabla.recorrerColumnas()
    tabla.recorrerColumnas()
    #print("EL VLAOR ES:"+str(N))
    colum=tabla.valorColumna()
    fil=tabla.valorFila()
    

   
def reporteColaSecuencia():
    for item in listaProductos.curselection():
        sii=listaProductos.get(item)
        messagebox.showinfo(title="verificar",message=sii)
    
    cantEle = secuencias.cantidadElementos(sii)
    for elem in range(1,cantEle+1):
        lb = tkinter.Label(ventana,text=str(secuencias.obtenerSecuencia(elem,sii))).place(x=275,y=elem*25)

def graficarSecuencia():

    for item in listaProductos.curselection():
        s=listaProductos.get(item)
        messagebox.showinfo(title="verificar",message=s)
    nombre=str(s)
    
   
    graphviz='''
        digraph L{
        node[shape=component fillcolor="white" style =filled]
    
        subgraph cluster_p{
        label= "SECUENCIA DE '''+nombre+''' " '''

    graphviz=graphviz+'''
        bgcolor = "blue"
        raiz[label ='''+nombre+''']
        edge[dir = "forward"]
        /*Aqui creamos las cabeceras
        de las filas*/'''
        
    cant=secuencias.cantidadElementos(nombre)
    for secuencia in range(1,cant+1):
        graphviz=graphviz+'''
        Fila'''+str(secuencia)+'''[label=" ''' +str(secuencias.obtenerSecuencia(secuencia,nombre))+'''",group='''+str(1)+'''];'''


    for filaaa in range(1,cant):
        graphviz=graphviz+'''
        Fila'''+str(filaaa)+'''->Fila'''+str(filaaa+1)+'''
            '''    
    graphviz=graphviz+'''
        raiz->Fila1;
        }
        }
        '''
    miArchivo=open('graphviz.dot','w')
    miArchivo.write(graphviz)
    miArchivo.close()
    
    system('dot -Tpng graphviz.dot -o graphviz.png')
    system('cd ./graphviz.png')
    startfile('graphviz.png')

def cargaSimulacion():
    try:
        for it in range(1,10):
            listaProductos.delete(it)
    except:
        print("no se pudo")

    archivo = filedialog.askopenfilename(title="abrir",filetypes=(("Archivos xml","*.xml"),("Archivo Python","*.py")))
    objetoTree = xml.parse(archivo)
    root = objetoTree.getroot()
    for nombre in root.findall("Nombre"):
        name=nombre.text
    
    for listado in root.findall("ListadoProductos"):
        contador=1
        for producto in listado.findall("Producto"):

            productos.insertar(contador,str(producto.text),str(name))
            contador=contador+1
    productos.recorrer()   

    messagebox.showinfo(title="AVISO",message="SIMULACION CARGADA")    

    cantidadP=int(productos.cantidadElementos())
    contador=1
    for cant in range(1,cantidadP+1):
        listaProductos.insert(contador,str(productos.verificar(contador)))
        contador=contador+1
    
def cargarMaquina():
    archivo = filedialog.askopenfilename(title="abrir",filetypes=(("Archivos xml","*.xml"),("Archivo Python","*.py")))
    objetoTree = xml.parse(archivo)
    root = objetoTree.getroot()

    for listado in root.findall("ListadoLineasProduccion"):
        for lista in listado.findall("LineaProduccion"):
            for numero in lista.findall("Numero"):
                num = numero.text
                for componente in lista.findall("CantidadComponentes"):
                   canComp = int(componente.text)
                   print(componente.text)
                   for c in range(1,canComp+1):
                       ca=str(c)
                       mat.insertar(ca,"L"+num,"C"+ca)
    CantidadLineas = root.findtext("CantidadLineasProduccion")
    c=CantidadLineas
    messagebox.showinfo(title="cantidad",message="cantidad es: "+c)
    print(c)
    mat.recorrerColumnas()
    mat.recorrerFilas()
    producto=1
    #carga de la secuencia de cada producto
    for listado in root.findall("ListadoProductos"):
        for lista in listado.findall("Producto"):
            
            for numero in lista.findall("nombre"):
                num = numero.text
                for componente in lista.findall("elaboracion"):
                   secuencia = componente.text
                   print(componente.text)
                   booleano=False
                   cadena=secuencia  
                   cadenaCorta=re.sub(r"\s+","",cadena)
                   contador=1
                   while booleano==False:
                        if not cadenaCorta:
                          booleano=True
                        else:
                            res = re.search(r"(\w{6})",cadenaCorta)
                            res2=res.group(1)
                            print(res2)
                            secuencias.insertar(contador,producto,res2,num)
                            contador=contador+1
                            if not res2:
                                booleano=True
                            else:
                                st3= re.sub(res2,"",cadenaCorta)
                                #print(st3)
                                cadenaCorta=st3
                                booleano=False
                producto=producto+1
    secuencias.recorrerColumnas()
    messagebox.showinfo(title="AVISO",message="MAQUINA CARGADA")

def estudiante():
    estud=Tk()
    estud.title("ESTUDIANTE    dgasdgsagsagasdgasgasg")
    L=LabelFrame(estud,text="INFORMACION")

    L.grid(row=0,column=0,columnspan=3,pady=20)
    et=Label(L,text="DIEGO ALEJANDRO CULAJAY GUINAC").grid(row=1,column=0)

    et2=Label(L,text="201213092").grid(row=2,column=0)
    
    Label(L,text="INTRODUCCION A LA PROGRAMACION Y COMPUTACION 2").grid(row=3,column=0)
    Label(L,text="4to SEMETRE").grid(row=4,column=0)
    estud.geometry("330x200")
    estud.resizable(0,0)
    estud.mainloop()
    
ventana= Tk()

x_ventana = ventana.winfo_screenwidth() // 2 - 700 // 2
y_ventana = ventana.winfo_screenheight() // 2 - 700 // 2
posicion = str(700) + "x" + str(700) + "+" + str(x_ventana) + "+" + str(y_ventana)

ventana.geometry(posicion)
#ventana.resizable(0,0)

ventana.title("LINEA DE ENSAMBLAJE")


barraMenu= Menu(ventana)

mnuArchivo=Menu(barraMenu,tearoff=0)
mnuArchivo.add_command(label="CARGAR MAQUINA",command=cargarMaquina)
mnuArchivo.add_command(label="CARGAR SIMULACION",command=cargaSimulacion)
mnuArchivo.add_command(label="Guardar")
mnuArchivo.add_command(label="Salir",command=ventana.destroy)
barraMenu.add_cascade(label="ARCHIVO",menu=mnuArchivo)

mnuReportes=Menu(barraMenu,tearoff=0)
mnuReportes.add_command(label="REPORTES",command=obtenerTiempo)
mnuReportes.add_command(label="REPORTE DE COLA DE SECUENCIA", command=reporteColaSecuencia)
mnuReportes.add_command(label="SALIDA XML",command=generarSalidaXML)
mnuReportes.add_command(label="Cerrar")
mnuReportes.add_command(label="Salir",command=ventana.destroy)
barraMenu.add_cascade(label="REPORTES",menu=mnuReportes)

mnuAyuda=Menu(barraMenu,tearoff=0)
mnuAyuda.add_command(label="INFORMACION ESTUDIANTE",command=estudiante)
mnuAyuda.add_command(label="INFORMACION APLICACION")
barraMenu.add_cascade(label="AYUDA",menu=mnuAyuda)



ventana.config(menu=barraMenu)

tree = ttk.Treeview(ventana,height=25,columns=("LINEA 1","LINEA 2","Linea 3","Linea 4"))
tree.grid(row=3,column=0,columnspan=2)
for n in range(0,5):
    tree.heading("#"+str(n),text="Linea "+str(n+1),anchor=CENTER)

tree.pack(side=tkinter.RIGHT)
tree.place(x=260,y=5)

lblProductos = Label(ventana,text="PRODUCTOS: ").place(x=10,y=10)

listaProductos = Listbox(ventana,width=40)
listaProductos.place(x=10,y=38)

lblComponentes=Label(ventana,text="COMPONENTES: ").place(x=10,y=215)
listaComponentes = Listbox(ventana,width=40)
listaComponentes.place(x=10,y=250)

botonComponentes = Button(ventana,text="MOSTRAR COMPONENTES")
botonComponentes.place(x=105,y=215)

botonGraficarSecuencia=Button(ventana,text="GRAFICA SECUENCIA",command=graficarSecuencia)
botonGraficarSecuencia.place(x=105,y=10)

botonTiempo = Button(ventana,text="TIEMPO DE ENSAMBLE",command=obtenerTiempo)
botonTiempo.place(x=10,y=400)

ventana["bg"]="#fb0"
ventana.mainloop()