from lista import Lista
from Linea_Produccion import Linea_Produccion
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
from tkinter import filedialog
import xml.etree.ElementTree as xml

lista_lineas= Lista()
def abrir():
    messagebox.showinfo(title="eehhh",message="hola")

def cargarMaquina():
    archivo = filedialog.askopenfilename(title="abrir",filetypes=(("Archivos xml","*.xml"),("Archivo Python","*.py")))
    
    objetoTree = xml.parse(archivo)
    root = objetoTree.getroot()
    
    CantidadLineas = root.findtext("CantidadLineasPrgasdgasdgasfasgdasduccion")

    messagebox.showinfo(title="cantidad",message="cantidad es: "+CantidadLineas)
    c=int(CantidadLineas)
    
    
    for cantidad in range(1,c+1):
        lista_lineas.insertar(cantidad)
    lista_lineas.recorrer()
    
    for cantidad in range(1,c+1):
        Linea_Produccion()
    

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
mnuArchivo.add_command(label="Cerrar")
mnuArchivo.add_command(label="Salir",command=ventana.destroy)
barraMenu.add_cascade(label="ARCHIVO",menu=mnuArchivo)

mnuReportes=Menu(barraMenu,tearoff=0)
mnuReportes.add_command(label="REPORTES",command=abrir)
mnuReportes.add_command(label="Nuevo")
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