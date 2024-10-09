'''
Exercício - nº 18 - Tkinter - (Mensagem)

pip install messagebox
'''

from tkinter import messagebox
from tkinter import *

window = Tk()
window.title('Teste de Mensagem')
window.geometry('400x200')

def clicked():
    messagebox.showinfo('Sistema XYZ', 'Teste de Mensagem')

btn = Button(window, text='Clique aqui', command=clicked)
btn.pack(expand=True)

window.mainloop()
