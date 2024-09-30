from tkinter import *


def centralizar_janela(janela):
    janela.update_idletasks()
    largura = janela.winfo_width()
    altura = janela.winfo_height()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f'{largura}x{altura}+{x}+{y}')

menu = Tk()

menu.title('Calculadora Valorant')

menu.geometry('330x500')

menu['bg'] = '#322D2D'


menu.iconbitmap('Tkinter/images/valorant.ico')

menu.resizable(False,False)

def msg_btn(mensagem):
    print(mensagem)

btn = Button(menu, text = 'Executar', command=lambda: msg_btn('TOMA SAFADA') )
btn.pack()
menu.mainloop()
