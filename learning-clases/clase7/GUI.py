"""grafic user interface - GUI"""

from tkinter import *
from tkinter import messagebox
from controladoresgui import *

ventana = Tk()

ventana.title("Ventana1")#Titulo de la ventana
ventana.geometry("520x480")#tamaño de la ventana
ventana.iconbitmap("C:/Users/SNPP/Desktop/python_Jorge/clase7/a.ico")
boton = Button(text="Abrir Calculadora", command=abrirCalculadora)
boton.place(x= 50, y= 50)
boton_hora = Button(text="Tiempo Actual", command=horaActual)
boton_hora.place(x=160, y=50)

ventana.mainloop()


