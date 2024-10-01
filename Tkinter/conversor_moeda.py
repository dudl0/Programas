import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfile

tela = tk.Tk()
tela.title('SCM')


tela.geometry('500x500')
tela.resizable(False,False)

msg0 = tk.Label(text='SISTEMA DE COTAÇÃO DE MOEDAS', font=('Ariel', 12, 'normal'), fg='white', bg='#ffc101', width=110, height=2)
msg0.pack()

msg1 = tk.Label(text='Selecione o Tipo de Moeda', font=('Ariel', 10))
msg1.pack()
msg1.place(relx=0.5, rely=0.2, anchor="center")
tela.iconbitmap('Tkinter/images/bitcoin.ico')
tela.mainloop()