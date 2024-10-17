import customtkinter as ctk
from ctypes import windll
from PIL import Image

windll.shcore.SetProcessDpiAwareness(2)

home = ctk.CTk()
ctk.set_appearance_mode('light')


home_image = ctk.CTkImage(light_image=Image.open('C:/Programas/Tkinter/images/fundohome.png'), size=(1200, 750))
home_label = ctk.CTkLabel(master=home, image=home_image,text=None)
home_label.pack(anchor='center')


home.geometry('1200x750')
home.resizable(False,False)
home.title('')

#--------------------- Funcionário ---------------------

def Abrir_tela_funcionario():
        interior_func = ctk.CTkFrame(master=home,bg_color='#DEDEDE',fg_color='#DEDEDE',width=840,height=636)
        interior_func.place(x=298,y=64)

        barra_pesquisa = ctk.CTkEntry(
                                      master=interior_func,
                                      placeholder_text='Pesquisar',
                                      border_color='white',
                                      font=('Istok Web', 14),
                                      bg_color='#DEDEDE',
                                      fg_color='white',
                                      corner_radius=5,
                                      width=345,
                                      height=28)
        barra_pesquisa.place(x=25,y=0)
        lupa_image = ctk.CTkImage(light_image=Image.open('C:/Programas/Tkinter/images/ttt.png'), size=(28,28))
        lupa_label = ctk.CTkLabel(master=interior_func,text=None,height=28,image=lupa_image)
        lupa_label.place(x=0,y=0)
        
        filtro = ctk.CTkEntry(
                              master=interior_func,
                              placeholder_text='Filtro',
                              justify='center',                              
                              border_color='white',
                              font=('Istok Web', 14),
                              bg_color='#DEDEDE',
                              fg_color='white',
                              corner_radius=5,
                              width=120,
                              height=28)
        filtro.place(x=420,y=0)
        filtro_image = ctk.CTkImage(light_image=Image.open('C:/Programas/Tkinter/images/Filter.png'), size=(20,20))
        filtro_label = ctk.CTkLabel(master=interior_func, 
                                    image=filtro_image,
                                    text=None,
                                    bg_color='white',
                                    fg_color='white',
                                    width=0,
                                    height=0)
        filtro_label.place(x=425,y=4)
        
        adicionar_image = ctk.CTkImage(light_image=Image.open('C:/Programas/Tkinter/images/adicionar.png'), size=(110,28))
        adicionar_label = ctk.CTkButton(master=interior_func, 
                                        image=adicionar_image,
                                        text=None,
                                        bg_color='#DEDEDE',
                                        fg_color='#DEDEDE',
                                        hover=None,
                                        width=0,
                                        height=0,
                                        border_spacing=0)
        adicionar_label.place(x=580,y=-3.5)

        delete_image = ctk.CTkImage(light_image=Image.open('C:/Programas/Tkinter/images/delete.png'), size=(110,28))
        delete_label = ctk.CTkButton(master=interior_func, 
                                     image=delete_image,
                                     text=None,
                                     bg_color='#DEDEDE',
                                     fg_color='#DEDEDE',
                                     hover=None,
                                     width=0,
                                     height=0,
                                     border_spacing=0)
        delete_label.place(x=727,y=-3.5)


#------------  LATERAL -----------------



logo_image = ctk.CTkImage(light_image=Image.open('C:/Programas/Tkinter/images/vslogo.png'), size=(40,40))
logo_label = ctk.CTkLabel(master=home, image=logo_image,text=None,bg_color='white',fg_color='white',width=0,height=0)
logo_label.place(x=27,y=20)


foto_user_image = ctk.CTkImage(light_image=Image.open('C:/Programas/Tkinter/images/foto.png'), size=(40,40))
logo_label = ctk.CTkLabel(master=home, 
                          image=foto_user_image,
                          text=None,
                          bg_color='white',
                          fg_color='white',
                          width=0,
                          height=0)
logo_label.place(x=23,y=110)
logo_text_label = ctk.CTkLabel(master=home,
                               text='Eduardo Costa Lobo',
                               text_color='#787878',
                               font=('Istok Web', 14),
                               bg_color='white',
                               width=0,
                               height=0)
logo_text_label.place(x=73,y=120)



funcionario_image = ctk.CTkImage(light_image=Image.open('C:/Programas/Tkinter/images/func.png'), size=(237,50))
funcionario_button = ctk.CTkButton(master=home,
                                   text=None,
                                   image=funcionario_image,
                                   bg_color='#E9E5E5',
                                   fg_color='white',
                                   hover_color='#E9E5E5',
                                   border_color='#E9E5E5',
                                   width=0,
                                   height=0,
                                   command=Abrir_tela_funcionario
                                   )
funcionario_button.place(x=-8,y=200)


cadastro_image = ctk.CTkImage(light_image=Image.open('C:/Programas/Tkinter/images/cadastro.png'), size=(237,50))
cadastro_button = ctk.CTkButton(master=home,
                                   text=None,
                                   image=cadastro_image,
                                   bg_color='#E9E5E5',
                                   fg_color='white',
                                   hover_color='#E9E5E5',
                                   border_color='#E9E5E5',
                                   width=0,
                                   height=0,
                                   )
cadastro_button.place(x=-8,y=255)


meusdados_image = ctk.CTkImage(light_image=Image.open('C:/Programas/Tkinter/images/meusdados.png'), size=(237,50))
meusdados_button = ctk.CTkButton(master=home,
                                   text=None,
                                   image=meusdados_image,
                                   bg_color='#E9E5E5',
                                   fg_color='white',
                                   hover_color='#E9E5E5',
                                   border_color='#E9E5E5',
                                   width=0,
                                   height=0,
                                   )
meusdados_button.place(x=-8,y=320)







home.mainloop()

