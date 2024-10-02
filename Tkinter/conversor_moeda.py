import tkinter as tk
from PIL import Image, ImageDraw


tela = tk.Tk()
tela.title('SCM')


tela.geometry('1250x700')
tela.resizable(False,False)


msg0 = tk.Label(text='SISTEMA DE COTAÇÃO DE MOEDAS', font=('Ariel', 12, 'normal'), fg='white', bg='#00439A', width=200, height=2)
msg0.pack()






msg2_borda = tk.Frame(tela,background='#032551')
msg2 = tk.Label(msg2_borda,text='Real (BRL)', font=('Ariel', 11),bd=0, width=60, height=2)
msg2.pack(fill='both', expand='True', padx=1.5, pady=1.5)
msg2_borda.place(relx=0.05, rely=0.25, anchor="w")


msg_valor = tk.Label(text='Valor', font=('Ariel', 11), width=10, height=1)
msg_valor.place(relx=0.03, rely=0.2, anchor="w")
#----------------
borda_valor = tk.Frame(tela,background='#A1A8B0')
bordaval = tk.Label(borda_valor,text='0,00', font=('Ariel', 11), fg='#A1A8B0',bd=0, width=10, height=1)
bordaval.pack(fill='both', expand='True', padx=1.5, pady=1.5)
borda_valor.place(relx=0.09, rely=0.2, anchor="w")




msg_Converter = tk.Label(text='Converter de', font=('Ariel', 11), width=10, height=1)
msg_Converter.place(relx=0.41, rely=0.2, anchor="w")




tela.iconbitmap('Tkinter/images/bitcoin.ico')


tela.mainloop()