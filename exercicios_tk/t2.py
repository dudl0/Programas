'''
Exercício - nº 20 - Tkinter - (Barra de Progresso)

pip install progressbar
pip install time
'''

from tkinter import *
from tkinter.ttk import *
root = Tk()
root.geometry('400x200')
progress = Progressbar(root, orient=HORIZONTAL,
                      length=100, mode='determinate')
root.title('--Instalação do Software XYZ--')

def bar():
    import time
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 40
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 50
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 60
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 80
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 100
    root.update_idletasks()
    time.sleep(1)

progress.pack(pady=50)
Button(root, text=  '--instalar--', command=bar).pack(pady=10)
mainloop()
