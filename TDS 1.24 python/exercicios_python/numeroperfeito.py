'''
Número perfeito

Em matemática, um número perfeito é um número natural para o qual a soma de todos os seus divisores naturais próprios (excluindo ele mesmo) é igual ao próprio número.
Por exemplo, o número 28 é, pois: 
28 = 1+2+4+7+14
    <divisores>

'''





class Perfeito(): # criando uma class para executar o método ( possivel fazer de forma estrutural)
    divisores = [] # criando array para armazenar divisores
    numero = int(input('Digite um número e verifique se ele é perfeito: '))
    

    # Perfeito.numero = chamando a variavel (numero) para dentro das def, resumindo é a variavel (numero)

    def calculo(self):
        for i in range(1,Perfeito.numero): # fazendo um laço, em que o i começa a rodar apartir de 1, até o valor da variavel (numero)
            
            r = Perfeito.numero%i          # dividi o numero pelo i, o i no caso consta do 1 até o numero digitado| caso (numero) = 10   i= [1,2,3,4,5,6,7,8,9,1]
            
            if r == 0:                     # se o resto da divisao for zero, significa que é divisor 
                Perfeito.divisores.append(i) # armazena os (i), que são divisores, na lista [divisores]
        
        
        
        soma = sum(Perfeito.divisores) # soma os numeros da variavel
        
        if Perfeito.numero == soma:    # se o numero digitado for igual a soma dos divisores, ele é um número perfeito
            print(f'{Perfeito.numero} é um número perfeito')
        else:
            print(f'{Perfeito.numero} não é um número perfeito')


c1 = Perfeito()
print(c1.calculo())


