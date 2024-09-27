import os

os.system('cls')

produtos = []


# função para adicionar produto
def adicionar_produto(nome, preco, quantidade):
    produto = (nome, preco, quantidade) # a variavel produto recebe 3 parametros
    produtos.append(produto) # guarda na lista os produtos registrados

#funcao para exibir os produtos para o cliente
def exibir_produtos():  
    for produto in produtos: # a variavel produtos vai rodar na lista produtos procurando os seus parametros
        nome, preco, quantidade = produto # indica que o produto q rodara na lista, vai buscar 3 elementos, que ja vao estar em ordem na lista, e retornar os mesmo
        print(f"Produto: {nome} /  Preço: R$ {preco:.2f} /  Quantidade: {quantidade}" + '\n') # organiza as informações



adicionar_produto('Cadeira', 120.00, 50)
adicionar_produto('Mesa', 300.00, 20)
exibir_produtos()