from tkinter import *
from tkinter import ttk



def rCuadratica (a, b, c):
     a = input("Numero de la a")
     b = input("Ingresa el numero de la b: ")
     c = input("Ingresa el numero de c")

ventana = Tk()

ventana.geometry("500x500")
ventana.title("Calcular Ecuacion Cuadratica")
dividendo = Label(text="Ecuacion Cuadratica \n\n\n -B (+/-) √ B^2 - 4xAxC")
dividendo.pack(pady=5)
dividendo.configure(font=('calibri 24 italic underline'))
divisor = Label(text="2A")
divisor.pack(pady=0)
divisor.configure(font='calibri 24 italic')
mainloop()