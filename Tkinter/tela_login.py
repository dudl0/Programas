import customtkinter as ctk
from tkinter import ttk
from ctypes import windll
from PIL import Image
import csv
import os


windll.shcore.SetProcessDpiAwareness(2)

home = ctk.CTk()
ctk.set_appearance_mode('light')


home_image = ctk.CTkImage(light_image=Image.open('D:/Programas/Tkinter/images/fundohome.png'), size=(1200, 750))
home_label = ctk.CTkLabel(master=home, image=home_image,text=None)
home_label.pack(anchor='center')


home.geometry('1200x750')
home.resizable(False,False)
home.title('')








#-------------------------------------------------------
#--------------------- Def Hover -----------------------

def fc_enter(event):
    funcionario_button.configure(image=funcionario_hover_image)
 
def fc_leave(event):
    funcionario_button.configure(image=funcionario_image)

def md_enter(event):
        meusdados_button.configure(image=md_hover)

def md_leave(event):
        meusdados_button.configure(image=meusdados_image)

def cd_enter(event):
        cadastro_button.configure(image=cadastro_hover)

def cd_leave(event):
        cadastro_button.configure(image=cadastro_image)
#-------------------------------------------------------
#--------------------- Funcionário ---------------------

def Abrir_tela_funcionario():

        def carregar_dados():
                arquivo_csv = 'D:/Programas/clientes.csv'
                
                # Verificar se o arquivo existe
                if not os.path.isfile(arquivo_csv):
                        print(f"O arquivo {arquivo_csv} não foi encontrado.")
                        return []

                # Inicializar a lista de dados
                dados = []
                
                # Abrir o arquivo e ler os dados
                with open(arquivo_csv, mode="r", newline="", encoding="utf-8") as file:
                        leitor_csv = csv.reader(file)
                        next(leitor_csv)  # Pular o cabeçalho, caso necessário
                        for linha in leitor_csv:
                                dados.append((linha[0],linha[5],linha[4],linha[3],linha[2],linha[1]))  # Converter cada linha em uma tupla e adicionar à lista

                        return dados


        def buscar_dados(event=None):
                search_query = barra_pesquisa.get().lower()  # Obtém o texto do campo de pesquisa e transforma em minúsculas

                # Limpa a tabela antes de adicionar os resultados filtrados
                for row in table.get_children():
                        table.delete(row)

                # Insere apenas as linhas que correspondem à pesquisa
                for item in dados:
                        if search_query in item[0].lower():  # Filtra pelo nome (índice 1), mas pode ajustar para outras colunas
                                table.insert("", "end", values=item)


        def deletar_linha():
                arquivo_csv = 'D:/Programas/clientes.csv'
                selecionado = table.selection()
               
                # Obtém os dados da linha selecionada para remoção do CSV
                linhas_para_manter = []
                for item in table.get_children():
                        if item not in selecionado:
                                linhas_para_manter.append(('Nome /,Email /,Cpf /,Salário /,Setor /,Senha /,Cargo /'))
                                linhas_para_manter.append(table.item(item)['values'])

                # Atualiza o treeview e o CSV
                table.delete(*selecionado)

                # Escreve as linhas restantes de volta no CSV
                with open(arquivo_csv, mode='w', newline='', encoding='utf-8') as csvfile:
                        escritor = csv.writer(csvfile)
                        escritor.writerows(linhas_para_manter)

        meusdados_button = ctk.CTkButton(
                                 master=home,
                                 text=None,
                                 image=meusdados_image,
                                 bg_color='#E9E5E5',
                                 fg_color='white',
                                 hover_color='#E9E5E5',
                                 border_color='#E9E5E5',
                                 width=0,
                                 height=0,
                                 command=Abrir_tela_md
                                                      )
        meusdados_button.place(x=-8,y=320)
        
        cadastro_button = ctk.CTkButton(
                                master=home,
                                text=None,
                                image=cadastro_image,
                                bg_color='#E9E5E5',
                                fg_color='white',
                                hover_color='#E9E5E5',
                                border_color='#E9E5E5',
                                width=0,
                                height=0,
                                command=Abrir_tela_cadastro
                                                           )
        cadastro_button.place(x=-8,y=255)
        
        
        funcionario_button.place_forget()
        func_hover = ctk.CTkButton(
                                   master=home,
                                   text=None,
                                   image=funcionario_hover_image,
                                   bg_color='#E9E5E5',
                                   fg_color='#E9E5E5',
                                   hover_color='#E9E5E5',
                                   border_color='#E9E5E5',
                                   width=0,
                                   height=0,
                                            )
        func_hover.place(x=-9,y=190)    

        interior_func = ctk.CTkFrame(master=home,bg_color='#DEDEDE',fg_color='#DEDEDE',width=840,height=636)
        interior_func.place(x=298,y=62)


        


        barra_pesquisa = ctk.CTkEntry(
                                      master=interior_func,
                                      placeholder_text='Pesquisar',
                                      border_color='white',
                                      font=('Istok Web', 14),
                                      bg_color='#DEDEDE',
                                      fg_color='white',
                                      corner_radius=5,
                                      width=345,
                                      height=28
                                                           )
        barra_pesquisa.place(x=25,y=0)
        barra_pesquisa.bind("<KeyRelease>", buscar_dados)
        lupa_image = ctk.CTkImage(light_image=Image.open('D:/Programas/Tkinter/images/ttt.png'), size=(28,28))
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
        filtro_image = ctk.CTkImage(light_image=Image.open('D:/Programas/Tkinter/images/Filter.png'), size=(20,20))
        filtro_label = ctk.CTkLabel(master=interior_func, 
                                    image=filtro_image,
                                    text=None,
                                    bg_color='white',
                                    fg_color='white',
                                    width=0,
                                    height=0)
        filtro_label.place(x=425,y=4)
        
        adicionar_image = ctk.CTkImage(light_image=Image.open('D:/Programas/Tkinter/images/adicionar.png'), size=(110,28))
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




        delete_image = ctk.CTkImage(light_image=Image.open('D:/Programas/Tkinter/images/delete.png'), size=(110,28))
        delete_label = ctk.CTkButton(master=interior_func, 
                                     image=delete_image,
                                     text=None,
                                     bg_color='#DEDEDE',
                                     fg_color='#DEDEDE',
                                     hover=None,
                                     width=0,
                                     height=0,
                                     border_spacing=0,
                                     command=deletar_linha
                                                           )
        delete_label.place(x=727,y=-3.5)

        style = ttk.Style()
        style.theme_use('clam')  # Use um tema que permita personalização
        style.configure("Custom.Treeview",
        bordercolor="white",
        borderwidth=0,
        height=10,
                )         
        style.configure(
                        "Custom.Treeview", 
                        font=('Istok Web', 10),
                        rowheight=28
                                ) 
        style.configure("Custom.Treeview.Heading",
                background="white",  # Cor de fundo dos cabeçalhos
                foreground="#000000", # Cor do texto dos cabeçalhos
                borderwidth=0,
                font=('Istok Web', 11, 'bold')) 

        style.map("Custom.Treeview.Heading",
          background=[('active', 'white'), ('pressed', 'white'), ('!active', 'white')],
          foreground=[('active', '#000000'), ('pressed', '#000000'), ('!active', '#000000')]) 
        
  
        
        table = ttk.Treeview(interior_func, columns = ('nome', 'cargo', 'setor','salario','cpf','email'), show='headings', style="Custom.Treeview")
        
   
        table.heading('nome', text='Nome',anchor='w')
        table.heading('cargo', text='Cargo',anchor='w')
        table.heading('setor', text='Setor',anchor='w')
        table.heading('salario', text='Salario',anchor='w')
        table.heading('cpf', text='Cpf',anchor='w')
        table.heading('email', text='Email',anchor='w')


        table.column('nome', width=110)
        table.column('cargo', width=60)
        table.column('setor', width=60)
        table.column('salario', width=60)
        table.column('cpf', width=80)
        table.column('email', width=130)
        

        dados = carregar_dados()
        
        for item in dados:
                table.insert("", "end", values=item)


  
        table.place(x=0, y=36, width=840, height=600)

        
        def md_enter(event):
                meusdados_button.configure(image=md_hover)

        def md_leave(event):
                meusdados_button.configure(image=meusdados_image)

        def cd_enter(event):
                cadastro_button.configure(image=cadastro_hover)

        def cd_leave(event):
                cadastro_button.configure(image=cadastro_image)


        cadastro_button.bind("<Enter>", cd_enter)
        cadastro_button.bind("<Leave>", cd_leave)

        meusdados_button.bind("<Enter>", md_enter)
        meusdados_button.bind("<Leave>", md_leave)

#-----------------------------------------
#------------ Cadastro ------------------

def Abrir_tela_cadastro():
    



        meusdados_button = ctk.CTkButton(
                                master=home,
                                text=None,
                                image=meusdados_image,
                                bg_color='#E9E5E5',
                                fg_color='white',
                                hover_color='#E9E5E5',
                                border_color='#E9E5E5',
                                width=0,
                                height=0,
                                command=Abrir_tela_md
                                                )
        meusdados_button.place(x=-8,y=320)

        funcionario_button = ctk.CTkButton(
                                   master=home,
                                   text=None,
                                   image=funcionario_image,
                                   bg_color='#E9E5E5',
                                   fg_color='white',
                                   hover_color='#E9E5E5',
                                   border_color='#E9E5E5',
                                   width=0,
                                   height=0,
                                   command=Abrir_tela_funcionario,
                                                                 )
        funcionario_button.place(x=-8,y=190)
        
        
        cadastro_button.place_forget()

        cd_hover = ctk.CTkButton(
                                master=home,
                                text=None,
                                image=cadastro_hover,
                                bg_color='#E9E5E5',
                                fg_color='#E9E5E5',
                                hover_color='#E9E5E5',
                                border_color='#E9E5E5',
                                width=0,
                                height=0,
                                         )
        cd_hover.place(x=-8,y=255)
        
        
        interior_cadastro = ctk.CTkFrame(master=home,bg_color='#DEDEDE',fg_color='white',width=840,height=636)
        interior_cadastro.place(x=298,y=62)


        def reset():
                nome_entry.delete(0, ctk.END)
                email_entry.delete(0, ctk.END)
                cpf_entry.delete(0, ctk.END)
                salario_entry.delete(0, ctk.END)
                setor_entry.delete(0, ctk.END)
                senha_entry.delete(0, ctk.END)
                cargo_entry.delete(0, ctk.END)


        def salvar_dados():  
                nome = nome_entry.get()
                email = email_entry.get()
                cpf = cpf_entry.get()
                salario = salario_entry.get()
                setor = setor_entry.get()
                senha = senha_entry.get()
                cargo = cargo_entry.get()

                arquivo_csv = 'clientes.csv'
                file_exists = os.path.isfile(arquivo_csv)

                with open(arquivo_csv, mode="a", newline="", encoding="utf-8") as file:
                        escritor_csv = csv.writer(file)
                        if not file_exists:
                                escritor_csv.writerow(['Nome /', 'Email /', 'Cpf /', 'Salário /', 'Setor /', 'Senha /', 'Cargo /'])
                        escritor_csv.writerow([nome, email, cpf, salario, setor, senha, cargo])
                
                nome_entry.delete(0, ctk.END)
                email_entry.delete(0, ctk.END)
                cpf_entry.delete(0, ctk.END)
                salario_entry.delete(0, ctk.END)
                setor_entry.delete(0, ctk.END)
                senha_entry.delete(0, ctk.END)
                cargo_entry.delete(0, ctk.END)

        text_preencher = ctk.CTkLabel( 
                                interior_cadastro,
                                text='Preencher',
                                text_color='#EF5151',
                                font=('Istok Web', 32, 'bold'),
                                fg_color='white',
                                bg_color='white',
                                width=155,
                                height=46
                                          )
        text_preencher.place(x=35,y=35)


        nome_text = ctk.CTkLabel(
                                interior_cadastro,
                                text='Nome',
                                text_color='#787878',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=37,
                                height=20
                                          )
        nome_text.place(x=35,y=121)                               
        

        email_text = ctk.CTkLabel(
                                interior_cadastro,
                                text='Email',
                                text_color='#787878',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=34,
                                height=20
                                          )
        email_text.place(x=429,y=121)


        cpf_text = ctk.CTkLabel(
                                interior_cadastro,
                                text='Cpf',
                                text_color='#787878',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=22,
                                height=20
                                          )
        cpf_text.place(x=35,y=219)


        salario_text = ctk.CTkLabel(
                                interior_cadastro,
                                text='Salario',
                                text_color='#787878',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=43,
                                height=20
                                          )
        salario_text.place(x=429,y=219)


        setor_text = ctk.CTkLabel(
                                interior_cadastro,
                                text='Setor',
                                text_color='#787878',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=34,
                                height=20
                                          )
        setor_text.place(x=35,y=317)


        senha_text = ctk.CTkLabel(
                                interior_cadastro,
                                text='Senha',
                                text_color='#787878',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=39,
                                height=20
                                          )
        senha_text.place(x=429,y=317)



        cargo_text = ctk.CTkLabel(
                                interior_cadastro,
                                text='Cargo',
                                text_color='#787878',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=38,
                                height=20
                                          )
        cargo_text.place(x=35,y=415)


        resetar_text = ctk.CTkButton(
                                interior_cadastro,
                                text='Resetar',
                                text_color='#787878',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                border_width=None,
                                hover=None,
                                width=38,
                                height=20,
                                command=reset
                                          )
        resetar_text.place(x=35,y=545)


        cadastrar_button = ctk.CTkButton(
                                interior_cadastro,
                                text='Cadastrar',
                                text_color='white',
                                font=('Istok Web', 15, 'bold'),
                                fg_color='#EF5151',
                                bg_color='white',
                                border_width=None,
                                hover=None,
                                corner_radius=5,
                                width=100,
                                height=26,
                                command= salvar_dados
                                                     )
        cadastrar_button.place(x=705,y=545)
        

        
        
        nome_entry = ctk.CTkEntry(
                                interior_cadastro,
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                border_width=0,
                                width=376,
                                height=3
                                          )
        nome_entry.place(x=35,y=146)                               
        

        email_entry = ctk.CTkEntry(
                                interior_cadastro,
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                border_width=0,
                                width=376,
                                height=3
                                          )
        email_entry.place(x=429,y=146)


        cpf_entry = ctk.CTkEntry(
                                interior_cadastro,
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                border_width=0,
                                width=376,
                                height=3
                                          )
        cpf_entry.place(x=35,y=244)


        salario_entry = ctk.CTkEntry(
                                interior_cadastro,
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                border_width=0,
                                width=376,
                                height=3
                                          )
        salario_entry.place(x=429,y=244)


        setor_entry = ctk.CTkEntry(
                                interior_cadastro,
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                border_width=0,
                                width=376,
                                height=3
                                          )
        setor_entry.place(x=35,y=342)


        senha_entry = ctk.CTkEntry(
                                interior_cadastro,
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                border_width=0,
                                width=376,
                                height=3
                                          )
        senha_entry.place(x=429,y=342)



        cargo_entry = ctk.CTkEntry(
                                interior_cadastro,
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                border_width=0,
                                width=376,
                                height=3
                                          )
        cargo_entry.place(x=35,y=440)

        linha_image = ctk.CTkImage(light_image=Image.open('D:/Programas/Tkinter/images/linha.png'), size=(376,3))
        
        linha = ctk.CTkLabel(
                             interior_cadastro,
                             text=None,
                             fg_color='#D9D9D9',
                             bg_color='white',
                             width=0,
                             height=0,
                             image=linha_image
                                     )
        linha.place(x=35,y=166)

        linha = ctk.CTkLabel(
                             interior_cadastro,
                             text=None,
                             fg_color='#D9D9D9',
                             bg_color='white',
                             width=0,
                             height=0,
                             image=linha_image
                                     )
        linha.place(x=429,y=166)

        linha = ctk.CTkLabel(
                             interior_cadastro,
                             text=None,
                             fg_color='#D9D9D9',
                             bg_color='white',
                             width=0,
                             height=0,
                             image=linha_image
                                     )
        linha.place(x=35,y=264)

        linha = ctk.CTkLabel(
                             interior_cadastro,
                             text=None,
                             fg_color='#D9D9D9',
                             bg_color='white',
                             width=0,
                             height=0,
                             image=linha_image
                                     )
        linha.place(x=429,y=264)

        linha = ctk.CTkLabel(
                             interior_cadastro,
                             text=None,
                             fg_color='#D9D9D9',
                             bg_color='white',
                             width=0,
                             height=0,
                             image=linha_image
                                     )
        linha.place(x=35,y=362)

        linha = ctk.CTkLabel(
                             interior_cadastro,
                             text=None,
                             fg_color='#D9D9D9',
                             bg_color='white',
                             width=0,
                             height=0,
                             image=linha_image
                                     )
        linha.place(x=429,y=362)

        linha = ctk.CTkLabel(
                             interior_cadastro,
                             text=None,
                             fg_color='#D9D9D9',
                             bg_color='white',
                             width=0,
                             height=0,
                             image=linha_image
                                     )
        linha.place(x=35,y=460)




        
        def md_enter(event):
                meusdados_button.configure(image=md_hover)

        def md_leave(event):
                meusdados_button.configure(image=meusdados_image)


        def fc_enter(event):
                funcionario_button.configure(image=funcionario_hover_image)
        
        def fc_leave(event):
                funcionario_button.configure(image=funcionario_image)
        
        funcionario_button.bind("<Enter>", fc_enter)
        funcionario_button.bind("<Leave>", fc_leave)

        meusdados_button.bind("<Enter>", md_enter)
        meusdados_button.bind("<Leave>", md_leave)

#----------------------------------------
#------------- Meus Dados ----------------

def Abrir_tela_md():
        
        def carregar_dados(n):
                arquivo_csv = 'D:/Programas/clientes.csv'
                
                # Verificar se o arquivo existe
                if not os.path.isfile(arquivo_csv):
                        print(f"O arquivo {arquivo_csv} não foi encontrado.")
                        return []

                # Inicializar a lista de dados
                dados = []
                
                # Abrir o arquivo e ler os dados
                with open(arquivo_csv, mode="r", newline="", encoding="utf-8") as file:
                        leitor_csv = csv.reader(file)
                        next(leitor_csv)  # Pular o cabeçalho, caso necessário
                        for linha in leitor_csv:
                                dados.append((linha[n]))

        funcionario_button = ctk.CTkButton(
                                   master=home,
                                   text=None,
                                   image=funcionario_image,
                                   bg_color='#E9E5E5',
                                   fg_color='white',
                                   hover_color='#E9E5E5',
                                   border_color='#E9E5E5',
                                   width=0,
                                   height=0,
                                   command=Abrir_tela_funcionario,
                                                                 )
        funcionario_button.place(x=-8,y=190)
        
        
        cadastro_button = ctk.CTkButton(
                                master=home,
                                text=None,
                                image=cadastro_image,
                                bg_color='#E9E5E5',
                                fg_color='white',
                                hover_color='#E9E5E5',
                                border_color='#E9E5E5',
                                width=0,
                                height=0,
                                command=Abrir_tela_cadastro
                                                           )
        cadastro_button.place(x=-8,y=255)
        
        

        meusdados_button.place_forget()

        md_hovb = ctk.CTkButton(
                                 master=home,
                                 text=None,
                                 image=md_hover,
                                 bg_color='#E9E5E5',
                                 fg_color='#E9E5E5',
                                 hover_color='#E9E5E5',
                                 border_color='#E9E5E5',
                                 width=0,
                                 height=0,
                                         )
        md_hovb.place(x=-8,y=320)
        
        
        interior_md = ctk.CTkFrame(master=home,bg_color='#DEDEDE',fg_color='white',width=840,height=636)
        interior_md.place(x=298,y=62)

        text_dados = ctk.CTkLabel( 
                                interior_md,
                                text='Seus Dados',
                                text_color='#EF5151',
                                font=('Istok Web', 32, 'bold'),
                                fg_color='white',
                                bg_color='white',
                                width=155,
                                height=46
                                          )
        text_dados.place(x=35,y=35)


        nome_text = ctk.CTkLabel(
                                interior_md,
                                text='Nome',
                                text_color='#787878',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=37,
                                height=20
                                          )
        nome_text.place(x=35,y=121)                               
        

        email_text = ctk.CTkLabel(
                                interior_md,
                                text='Email',
                                text_color='#787878',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=34,
                                height=20
                                          )
        email_text.place(x=429,y=121)


        cpf_text = ctk.CTkLabel(
                                interior_md,
                                text='Cpf',
                                text_color='#787878',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=22,
                                height=20
                                          )
        cpf_text.place(x=35,y=219)


        salario_text = ctk.CTkLabel(
                                interior_md,
                                text='Salario',
                                text_color='#787878',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=43,
                                height=20
                                          )
        salario_text.place(x=429,y=219)


        setor_text = ctk.CTkLabel(
                                interior_md,
                                text='Setor',
                                text_color='#787878',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=34,
                                height=20
                                          )
        setor_text.place(x=35,y=317)


        senha_text = ctk.CTkLabel(
                                interior_md,
                                text='Senha',
                                text_color='#787878',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=39,
                                height=20
                                          )
        senha_text.place(x=429,y=317)



        cargo_text = ctk.CTkLabel(
                                interior_md,
                                text='Cargo',
                                text_color='#787878',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=38,
                                height=20
                                          )
        cargo_text.place(x=35,y=415)


        aumento_button = ctk.CTkButton(
                                interior_md,
                                text='Pedir Aumento',
                                text_color='white',
                                font=('Istok Web', 15, 'bold'),
                                fg_color='#EF5151',
                                bg_color='white',
                                border_width=None,
                                hover=None,
                                corner_radius=5,
                                width=376,
                                height=26
                                          )
        aumento_button.place(x=429,y=437)
        

        
        
        nome_entry = ctk.CTkEntry(
                                interior_md,
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                border_width=0,
                                width=376,
                                height=3
                                          )
        nome_entry.place(x=35,y=146)                               
        

        email_entry = ctk.CTkEntry(
                                interior_md,
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                border_width=0,
                                width=376,
                                height=3
                                          )
        email_entry.place(x=429,y=146)


        cpf_entry = ctk.CTkEntry(
                                interior_md,
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                border_width=0,
                                width=376,
                                height=3
                                          )
        cpf_entry.place(x=35,y=244)


        salario_entry = ctk.CTkEntry(
                                interior_md,
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                border_width=0,
                                width=376,
                                height=3
                                          )
        salario_entry.place(x=429,y=244)


        setor_entry = ctk.CTkEntry(
                                interior_md,
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                border_width=0,
                                width=376,
                                height=3
                                          )
        setor_entry.place(x=35,y=342)


        senha_entry = ctk.CTkEntry(
                                interior_md,
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                border_width=0,
                                width=376,
                                height=3
                                          )
        senha_entry.place(x=429,y=342)



        cargo_entry = ctk.CTkEntry(
                                interior_md,
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                border_width=0,
                                width=376,
                                height=3
                                          )
        cargo_entry.place(x=35,y=440)

        linha_image = ctk.CTkImage(light_image=Image.open('D:/Programas/Tkinter/images/linha.png'), size=(376,3))
        
        linha = ctk.CTkLabel(
                             interior_md,
                             text=None,
                             fg_color='#D9D9D9',
                             bg_color='white',
                             width=0,
                             height=0,
                             image=linha_image
                                     )
        linha.place(x=35,y=166)

        linha = ctk.CTkLabel(
                             interior_md,
                             text=None,
                             fg_color='#D9D9D9',
                             bg_color='white',
                             width=0,
                             height=0,
                             image=linha_image
                                     )
        linha.place(x=429,y=166)

        linha = ctk.CTkLabel(
                             interior_md,
                             text=None,
                             fg_color='#D9D9D9',
                             bg_color='white',
                             width=0,
                             height=0,
                             image=linha_image
                                     )
        linha.place(x=35,y=264)

        linha = ctk.CTkLabel(
                             interior_md,
                             text=None,
                             fg_color='#D9D9D9',
                             bg_color='white',
                             width=0,
                             height=0,
                             image=linha_image
                                     )
        linha.place(x=429,y=264)

        linha = ctk.CTkLabel(
                             interior_md,
                             text=None,
                             fg_color='#D9D9D9',
                             bg_color='white',
                             width=0,
                             height=0,
                             image=linha_image
                                     )
        linha.place(x=35,y=362)

        linha = ctk.CTkLabel(
                             interior_md,
                             text=None,
                             fg_color='#D9D9D9',
                             bg_color='white',
                             width=0,
                             height=0,
                             image=linha_image
                                     )
        linha.place(x=429,y=362)

        linha = ctk.CTkLabel(
                             interior_md,
                             text=None,
                             fg_color='#D9D9D9',
                             bg_color='white',
                             width=0,
                             height=0,
                             image=linha_image
                                     )
        linha.place(x=35,y=460)

                 


        def fc_enter(event):
                funcionario_button.configure(image=funcionario_hover_image)
 
        def fc_leave(event):
                funcionario_button.configure(image=funcionario_image)

        def cd_enter(event):
                cadastro_button.configure(image=cadastro_hover)

        def cd_leave(event):
                cadastro_button.configure(image=cadastro_image)

        
        funcionario_button.bind("<Enter>", fc_enter)
        funcionario_button.bind("<Leave>", fc_leave)

        cadastro_button.bind("<Enter>", cd_enter)
        cadastro_button.bind("<Leave>", cd_leave)

#--------------------------------------
#------------  LATERAL -----------------



logo_image = ctk.CTkImage(light_image=Image.open('D:/Programas/Tkinter/images/vslogo.png'), size=(40,40))
logo_label = ctk.CTkLabel(
                          master=home, 
                          image=logo_image,
                          text=None,bg_color='white',
                          fg_color='white',
                          width=0,
                          height=0
                                  )
logo_label.place(x=27,y=20)


foto_user_image = ctk.CTkImage(light_image=Image.open('D:/Programas/Tkinter/images/foto.png'), size=(40,40))
logo_label = ctk.CTkLabel(
                          master=home, 
                          image=foto_user_image,
                          text=None,
                          bg_color='white',
                          fg_color='white',
                          width=0,
                          height=0
                                  )
logo_label.place(x=23,y=110)
logo_text_label = ctk.CTkLabel(
                               master=home,
                               text='Eduardo Costa Lobo',
                               text_color='#787878',
                               font=('Istok Web', 14),
                               bg_color='white',
                               width=0,
                               height=0)
logo_text_label.place(x=73,y=120)



funcionario_image = ctk.CTkImage(light_image=Image.open('D:/Programas/Tkinter/images/func.png'), size=(237,50))
funcionario_hover_image = ctk.CTkImage(light_image=Image.open('D:/Programas/Tkinter/images/func_hover.png'), size=(237,50))
funcionario_button = ctk.CTkButton(
                                   master=home,
                                   text=None,
                                   image=funcionario_image,
                                   bg_color='#E9E5E5',
                                   fg_color='white',
                                   hover_color='#E9E5E5',
                                   border_color='#E9E5E5',
                                   width=0,
                                   height=0,
                                   command=Abrir_tela_funcionario,
                                                                 )
funcionario_button.place(x=-8,y=190)


cadastro_image = ctk.CTkImage(light_image=Image.open('D:/Programas/Tkinter/images/cadastro.png'), size=(237,50))
cadastro_hover = ctk.CTkImage(light_image=Image.open('D:/Programas/Tkinter/images/cad_hover.png'), size=(237,50))
cadastro_button = ctk.CTkButton(
                                master=home,
                                text=None,
                                image=cadastro_image,
                                bg_color='#E9E5E5',
                                fg_color='white',
                                hover_color='#E9E5E5',
                                border_color='#E9E5E5',
                                width=0,
                                height=0,
                                command=Abrir_tela_cadastro
                                                           )
cadastro_button.place(x=-8,y=255)


meusdados_image = ctk.CTkImage(light_image=Image.open('D:/Programas/Tkinter/images/meusdados.png'), size=(237,50))
md_hover = ctk.CTkImage(light_image=Image.open('D:/Programas/Tkinter/images/md_hover.png'), size=(237,50))
meusdados_button = ctk.CTkButton(
                                 master=home,
                                 text=None,
                                 image=meusdados_image,
                                 bg_color='#E9E5E5',
                                 fg_color='white',
                                 hover_color='#E9E5E5',
                                 border_color='#E9E5E5',
                                 width=0,
                                 height=0,
                                 command=Abrir_tela_md
                                                      )
meusdados_button.place(x=-8,y=320)





funcionario_button.bind("<Enter>", fc_enter)
funcionario_button.bind("<Leave>", fc_leave)

cadastro_button.bind("<Enter>", cd_enter)
cadastro_button.bind("<Leave>", cd_leave)

meusdados_button.bind("<Enter>", md_enter)
meusdados_button.bind("<Leave>", md_leave)


home.iconbitmap('D:/Programas/Tkinter/images/vslogo.png')

home.mainloop()

