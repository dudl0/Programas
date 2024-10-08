#Opções seleção
import tkinter as tk
from tkinter import *
 
window = Tk()
var1 = IntVar()
Checkbutton(window, text='Masculino', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(window, text='Feminino', variable=var2).grid(row=1, sticky=W)
var3 = IntVar()
Checkbutton(window, text='Menine', variable=var3).grid(row=2, sticky=W)
var4 = IntVar()
Checkbutton(window, text='Foda-se, Robô intergalatico', variable=var4).grid(row=3, sticky=W)
mainloop()