
from Lista_Linea_Produccion import listaEncabezado
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
from tkinter import filedialog
import xml.etree.ElementTree as xml
import re
from Lista_componentes import matriz
from SecuenciaLista import matriz_SecuenciaProducto
mat = matriz()
secuencias = matriz_SecuenciaProducto()
def abrir():
    messagebox.showinfo(title="Mensaje",message="hola")

def reporteColaSecuencia():
    return None
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
mnuArchivo.add_command(label="CARGAR SIMULACION")
mnuArchivo.add_command(label="Guardar")
mnuArchivo.add_command(label="Salir",command=ventana.destroy)
barraMenu.add_cascade(label="ARCHIVO",menu=mnuArchivo)

mnuReportes=Menu(barraMenu,tearoff=0)
mnuReportes.add_command(label="REPORTES",command=abrir)
mnuReportes.add_command(label="REPORTE DE COLA DE SECUENCIA", command=reporteColaSecuencia)
mnuReportes.add_command(label="Guardar")
mnuReportes.add_command(label="Cerrar")
mnuReportes.add_command(label="Salir",command=ventana.destroy)
barraMenu.add_cascade(label="REPORTES",menu=mnuReportes)

mnuAyuda=Menu(barraMenu,tearoff=0)
mnuAyuda.add_command(label="INFORMACION ESTUDIANTE",command=estudiante)
mnuAyuda.add_command(label="INFORMACION APLICACION")
barraMenu.add_cascade(label="AYUDA",menu=mnuAyuda)

ventana.config(menu=barraMenu)

tree = ttk.Treeview(height=10,columns=2)
tree.grid(row=4,column=0,columnspan=2)
tree.heading("#0",text="Name",anchor=CENTER)
tree.heading("#1", text="Price",anchor=CENTER)
tree.pack(side=tkinter.RIGHT)
ventana.mainloop()