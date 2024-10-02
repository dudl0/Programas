import customtkinter 
from ctypes import windll
from PIL import Image



tela = customtkinter.CTk()

windll.shcore.SetProcessDpiAwareness(2)

tela.geometry('500x400')
tela.resizable(False,False)
tela.title('')

customtkinter.set_appearance_mode('light')


label_image = customtkinter.CTkImage(light_image=Image.open('Tkinter/images/fundo.png'), size=(500, 402))
image_label = customtkinter.CTkLabel(master=tela,text='', image=label_image)
image_label.place(anchor='center',x=250,y=200)


login_text = customtkinter.CTkLabel(tela,text='Fazer Login',font=('Tahoma',18, 'bold'),fg_color='white',text_color='#006ff9')
login_text.place(anchor='center',x=296,y=60)

email_text = customtkinter.CTkEntry(tela,placeholder_text='Seu email', border_width=1.4, border_color='#4a4a4a', fg_color='white',corner_radius=5, width=195, height=34)
email_text.place(anchor='center',x=340,y=100)

senha_text = customtkinter.CTkEntry(tela,placeholder_text='Seu senha', border_width=1.4, border_color='#4a4a4a', fg_color='white', corner_radius=5, width=195,height=34, show='*')
senha_text.place(anchor='center',x=340,y=145)

checkbox_remember = customtkinter.CTkCheckBox(tela,text='Lembrar Login',text_color='#4a4a4a',fg_color='#006ff9',checkbox_height=18,checkbox_width=18,border_width=1.48, corner_radius=36)
checkbox_remember.place(anchor='center',x=300,y=185)


def funclick():
    print('login')

btn_login = customtkinter.CTkButton(master=tela,text='Login',font=('Tahoma', 13,'bold'), command=funclick)
btn_login.place(anchor='center',x=360,y=255)


senha_text = customtkinter.CTkLabel(tela,text='Problemas com Login?',font=('Ariel', 12,'underline'),text_color='#4a4a4a', fg_color='white')
senha_text.place(anchor='center',x=360,y=310)









tela.mainloop()