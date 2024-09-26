#Exemplo 1
 
lista_comp1 = ['PC', 'Notebook', 'HD', 'RAM', 'GPU']
print(lista_comp1[4])
print('\n' + '-------------------------------------------------------------------')
#Exemplo 2
 
lista_comp2 = ['PC', 'Notebook', 'HD', 'RAM', 'GPU']
print(lista_comp2[0:4])
print('\n' + '-------------------------------------------------------------------')
#Exemplo 3
 
msg1 = 'O indice do produto é:'
msg2 = 'O item da lista é:'
msg3 = 'A quantidade do produto é:'
 
produtos = ['Celular', 'Computador', 'Monitor', 'Placa de video', 'Processador']
estoque = [100, 200, 300, 400, 500]
 
i = produtos.index('Processador')
 
print('\n' + msg1, i, msg2, produtos[i], msg3, estoque[i])
print('\n' + '-------------------------------------------------------------------')
#Exemplo 4
 
prod = input('\n' + 'Insira o nome de um equipamento eletronico: ')
prods = ['Celular', 'Computador', 'Monitor', 'Placa de video', 'CPU']
estoque = [100,     200,        300,        400,        500]
 
if prod in prods:
    i = prods.index(prod)
    qtd_estoque = estoque[i]
    print('\n' + 'A quantidade do produto: {} em estoque é de: {} unidades.'.format(prod, qtd_estoque))
print('\n' + '-------------------------------------------------------------------')
