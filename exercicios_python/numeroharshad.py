algarismo = int(input('Digite um numero e descubra quais antes dele são números de Harshard: '))
lista_harshad = [] # lista para armazenar números de harshad


# (linha 26) esse laço rodara apartir do 1, até o número armazenado na váriavel algarismo  '(1, int(algarismo))

'''
linha(17)
esse metodo, usa uma variavel (i), para passar pelo número que a variavel (f) está lendo, como a variavel (f) foi direcionada
como uma string 'str(f)', o (i) pode possar por cada caracter da string, ai pode separar a string e cada caracter, no caso o numero

ex:  '11' i= 1,1
como o (i) está sendo lido com int, ele armazena tudo em 'separar algarismos' que é uma array []
'''

for f in range(1, (algarismo)):  
    separar_algarismos= [int(i) for i in str(f)]   
    
    somar_algarismos = sum(separar_algarismos) # soma as variaveis armazenados em 'separar algarismos'
   
    if int(f)%somar_algarismos == 0: # se  f for divisivel por 'somar_algarismos' ele armazenara em lista_harshad
        lista_harshad.append(f) 
    else:
        None 

print(lista_harshad)




