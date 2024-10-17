import customtkinter as ctk
from ctypes import windll
from PIL import Image

windll.shcore.SetProcessDpiAwareness(2)

home = ctk.CTk()
ctk.set_appearance_mode('light')

def calendario():
    print('Calendario')

def ajust():
    print('Ajust') 

def lixo():
    print('Lixeira')

def refresh():
    print('refresh')


home_image = ctk.CTkImage(light_image=Image.
                          open('Tkinter/images/proj.png'), 
                          size=(1200, 750))

image_home = ctk.CTkLabel(master=home,text='', 
                          image=home_image)

image_home.place(anchor='center',
                 x=600,y=375)


image_calendario = ctk.CTkImage(light_image= Image.open('Tkinter/images/calendario.png'), size=(30, 25))


button_calendario = ctk.CTkButton(home, bg_color='white',
                                  text='',
                                  fg_color='white',
                                  hover_color='white',
                                  command=calendario,
                                  width=0,
                                  height=0,
                                  image=image_calendario)
button_calendario.place(x=296,y=17)


image_ajust = ctk.CTkImage(light_image= Image.open('Tkinter/images/Ajust.png'), size=(30, 25))

button_ajust =  ctk.CTkButton(home, bg_color='white',
                                  text='',
                                  fg_color='white',
                                  hover_color='white',
                                  command=ajust,
                                  width=0,
                                  height=0,
                                  image=image_ajust)

button_ajust.place(x=328,y=17)


image_lixo = ctk.CTkImage(light_image= Image.open ('Tkinter/images/lixo.png'), size=(30, 25))

button_lixo = ctk.CTkButton(home, bg_color='white',
                                  text='',
                                  fg_color='white',
                                  hover_color='white',
                                  command=lixo,
                                  width=0,
                                  height=0,
                                  image=image_lixo)

button_lixo.place(x=360,y=17)



image_refresh = ctk.CTkImage(light_image= Image.open('Tkinter/images/refresh.png'), size=(30, 25))

button_refresh = ctk.CTkButton(home, bg_color='white',
                                  text='',
                                  fg_color='white',
                                  hover_color='white',
                                  command=refresh,
                                  width=0,
                                  height=0,
                                  image=image_refresh)

button_refresh.place(x=392,y=17)


label_search = ctk.CTkEntry(master=home, placeholder_text='                                                           search',
                            bg_color='white',
                            fg_color='#F5F5F5',
                            border_color='white',
                            corner_radius=9, 
                            width=425, 
                            height=30)
label_search.place(x=503,y=17)




home.geometry('1200x750')
home.resizable(False,False)
home.title('')


home.mainloop()


