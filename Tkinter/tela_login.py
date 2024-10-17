import customtkinter
from ctypes import windll
from PIL import Image
 
 
 
tela = customtkinter.CTk()
 
windll.shcore.SetProcessDpiAwareness(2)
 
def centralizar_janela(janela):
    janela.update_idletasks()
    largura = janela.winfo_width()
    altura = janela.winfo_height()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2) - (50)
    janela.geometry(f'{largura}x{altura}+{x}+{y}')
 
 
 
 
tela.geometry('1200x750')
tela.resizable(False,False)
tela.title('')
 
customtkinter.set_appearance_mode('light')
 
 
label_image = customtkinter.CTkImage(light_image=Image.open('Tkinter/images/login.png'), size=(1200, 750))
image_label = customtkinter.CTkLabel(master=tela,text='', image=label_image)
image_label.place(anchor='center',x=600,y=375)
 
 
login_text = customtkinter.CTkLabel(tela,text='Fazer Login',font=('Tahoma',32, 'bold'),fg_color='white',text_color='#62859B')
login_text.place(x=708,y=55)
 
email_bordetext = customtkinter.CTkLabel(tela,text='Email', font=('Ariel', 15), bg_color='white')
email_bordetext.place(x=709,y=228)
 
email_text = customtkinter.CTkEntry(tela,placeholder_text='Seu email', border_width=1.4, border_color='#4a4a4a', fg_color='white',corner_radius=5, width=437, height=44)
email_text.place(x=708,y=250)
 
senha_bordetext = customtkinter.CTkLabel(tela,text='Senha', font=('Ariel', 15), bg_color='white')
senha_bordetext.place(x=709,y=351)
 
senha_text = customtkinter.CTkEntry(tela,placeholder_text='Sua senha', border_width=1.4, border_color='#4a4a4a', fg_color='white', corner_radius=5, width=437,height=44, show='*')
senha_text.place(x=708,y=373)
 
checkbox_remember = customtkinter.CTkCheckBox(tela,text='Lembrar Login',font=('Ariel', 14),text_color='#4a4a4a',bg_color='white',fg_color='#006ff9',checkbox_height=28,checkbox_width=28,border_width=1.5, corner_radius=9)
checkbox_remember.place(x=710,y=438)
 
 
def funclick():
    print('login')
 
btn_login = customtkinter.CTkButton(master=tela,text='Login',bg_color='white',fg_color='#62859B',font=('Tahoma', 18,'bold'),text_color='white', command=funclick, width=179, height=44)
btn_login.place(x=837,y=563)
 
 
senha_text = customtkinter.CTkLabel(tela,bg_color='white',text='Problemas com Login?',font=('Ariel', 14,'underline'),text_color='#4a4a4a', fg_color='white', width=179, height=44 )
senha_text.place(x=837,y=610)
 
 
 
 
centralizar_janela(tela)
 
 
 
 
tela.mainloop()
 