def verificar_estoque(itens):
    #lista de itens com quantidade menor ou igual a 5
    reposicao = [item for item, quantidade in itens if quantidade <= 5]
    return reposicao


linha = '-------------------------------------------------------------------------'



estoque = [('Caneta',10), ('Lapis', 8), ('Caneta',4), ('Borracha', 2)]
print('\n' + '-----------------------------------------------------------')
print('Os itens que estão em falta no estoque de papelaria são: ', verificar_estoque(estoque))
print('---------------------------------------------------------------' + '\n')
 