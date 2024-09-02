import os
import datetime
from tkinter import messagebox
import math


def abrirCalculadora():
    os.system("calc")

def horaActual():
    tiempo = datetime.datetime.now()

    messagebox.showinfo(message=tiempo.strftime("%Y-%m-%d \n \n %H:%M:%S"), title="Tiempo Actual")
    

    