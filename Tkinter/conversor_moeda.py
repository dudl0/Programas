import tkinter as tk


tela = tk.Tk()
tela.title('SCM')


tela.geometry('1250x700')
tela.resizable(False,False)


msg0 = tk.Label( bg='#00439A', width=200, height=2)
msg0.pack()






msg2_borda = tk.Frame(tela,background='#032551')
msg2 = tk.Label(msg2_borda,text='Real (BRL)', font=('Ariel', 11),bd=0, width=60, height=2)
msg2.pack(fill='both', expand='True', padx=1.5, pady=1.5)
msg2_borda.place(relx=0.05, rely=0.25, anchor="w")


msg2_borda = tk.Frame(tela,background='#032551')
msg2 = tk.Label(msg2_borda,text='Dolar (USD)', font=('Ariel', 11),bd=0, width=60, height=2)
msg2.pack(fill='both', expand='True', padx=1.5, pady=1.5)
msg2_borda.place(relx=0.95, rely=0.25, anchor="e")



msg_valor = tk.Label(text='Valor', font=('Ariel', 11), width=10, height=1)
msg_valor.place(relx=0.03, rely=0.2, anchor="w")



valor_borda = tk.Frame(tela,background='#a6a6a6')
bordaval= tk.Entry()
bordaval = tk.Label(valor_borda, font=('Ariel', 11),bd=0, width=15, height=1)
bordaval.pack(fill='both', expand='True', padx=1.3, pady=1.3)

valor_borda.place(relx=0.09, rely=0.2, anchor="w")




msg_Converter = tk.Label(text='Converter de', font=('Ariel', 11), width=10, height=1)
msg_Converter.place(relx=0.41, rely=0.2, anchor="w")

msg_Para = tk.Label(text='Para', font=('Ariel', 11), width=10, height=1)
msg_Para.place(relx=0.493, rely=0.2, anchor="w")

tela.iconbitmap('Tkinter/images/bitcoin.ico')


tela.mainloop()