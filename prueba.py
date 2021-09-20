import tkinter
from tkinter import font
from tkinter.constants import BOTTOM, RIGHT
from typing import Text 

ventana = tkinter.Tk()
ventana.geometry("600x600")


cajatexto= tkinter.Entry(ventana,font="Helvetica 50")
cajatexto.pack()



def saludo():
    text20=cajatexto.get()
    print(text20)


etiqueta = tkinter.Label(ventana,text="hola mundo",bg="blue")
etiqueta.pack(fill=tkinter.X)

boton1=tkinter.Button(ventana,text="PRESIONA",command=saludo)
boton1.pack()
ventana.mainloop()