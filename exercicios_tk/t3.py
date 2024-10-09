#Aula 18 --> Imput grafico com retorno em string
import tkinter as tk
class app(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()
 
        #cria variavel no app
        self.contents = tk.StringVar ()
        #define valor do campo(texto)
        self.contents.set('Apagar> Digite > ENTER')
        #Captura de texto
        self.entrythingy['textvariable'] = self.contents
 
        #retorna o valor digitado
        self.entrythingy.bind('<Key-Return>',
        self.print_contents)
 
        #imprime o valor atual da variavel
    def print_contents(self, event):
        print('A palavra/frase digitada foi: ',
              self.contents.get())
        
window = tk.Tk()
myapp = app(window)
myapp.mainloop()