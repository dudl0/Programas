# Projeto 1º - Calculadora com Python e Tkinter com layout inspirado no estilo "PyPhone"
# Esta aplicação cria uma calculadora simples usando o módulo Tkinter.
# Ela permite ao usuário realizar operações básicas como adição, subtração, multiplicação e divisão.

# Importando o módulo Tkinter para criar a interface gráfica (GUI)
import tkinter as tk
import time
# Função que será chamada quando o usuário clicar em um botão da calculadora
def click(event):
    # Captura o texto do botão que foi clicado
    text = event.widget.cget("text")

    # Verifica se o botão clicado foi "=" (para calcular o resultado)
    if text == "=":
        try:
            # Avalia a expressão contida na tela (usando eval)
            result = eval(screen.get())
            screen.set(result)  # Exibe o resultado na tela
        except Exception as e:
            # Caso haja erro na expressão (ex.: divisão por zero), exibe "Erro" na tela
            screen.set("Erro")

    # Se o botão clicado foi "C", limpa a tela da calculadora
    elif text == "C":
        screen.set("")

    # Caso contrário (para qualquer outro botão), adiciona o texto do botão à expressão na tela
    else:
        screen.set(screen.get() + text)

# Configuração da janela principal da calculadora
root = tk.Tk()  # Cria uma nova janela
root.title("Calculadora - PyPhone")  # Define o título da janela
root.geometry("350x500")  # Define o tamanho da janela (largura x altura)
root.config(bg="#F0F0F0")  # Configura a cor de fundo da janela (cinza claro, estilo Windows)

# Variável para armazenar o texto que será exibido na tela da calculadora
screen = tk.StringVar()

# Caixa de entrada onde as expressões e resultados serão exibidos
entry = tk.Entry(root, textvar=screen, font="Arial 24", bd=10, insertwidth=2, width=14, justify='right')
# Configura a aparência da caixa de entrada (fonte, borda, alinhamento à direita)
entry.pack(fill="both", ipadx=8, padx=10, pady=20)  # Posiciona a caixa na interface

# Lista de botões da calculadora, organizados por linha
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

# Função para criar os botões com o estilo específico
def create_button(frame, text, color="#FFFFFF", bg="#C0C0C0"):
    # Cria um botão com o texto, cor de fundo, e estilo desejado
    button = tk.Button(frame, text=text, font="Arial 20", padx=20, pady=20, bg=bg, fg=color, borderwidth=0)
    # Posiciona o botão no frame (linha) e ajusta o tamanho para preencher o espaço disponível
    button.pack(side="left", expand=True, fill="both", padx=5, pady=5)
    # Adiciona a função click ao evento de clique do botão
    button.bind("<Button-1>", click)
    return button

# Laço para criar e organizar os botões na interface
for line in buttons:
    # Cria um frame (linha) para organizar os botões da calculadora
    frame = tk.Frame(root, bg="#F0F0F0")  # Cor de fundo similar à calculadora do Windows
    frame.pack(expand=True, fill="both")  # Ajusta o frame para preencher o espaço disponível
    for button_text in line:
        # Para cada botão na linha, cria o botão com o texto e estilo apropriados
        create_button(frame, button_text)
        
# Inicia o loop principal da aplicação (para exibir a janela)
root.mainloop()
