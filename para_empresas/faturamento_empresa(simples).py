qtd_c = 1000 #qntd de cocas
qtd_p = 500 #qntd de pepis
vco = 4.50 #valor coca
vps = 3.90 #valor pepis

investimento = 6000
linha = '--------------------------------------------------------------------------'

print('\n' + linha)
print(f'O total de vendas de latas de Coca-Cola foi de: R${qtd_c * vco:,.2f}') # imprimi o valor total das vendas de Coca
print(f'O total de vendas de latas Pepis foi de: R${qtd_p * vps:,.2f} ')  # imprimi o valor total das vendas de Pepis


faturamento = (qtd_p * vps) + (qtd_c * vco) # faturamento da empresa é todo dinheiro obtido com vendas 

print(linha + '\n')

print(f'O faturamento das vendas de latas de refrigerantes foi de: R$ {faturamento:,.2f}' + '\n')

if investimento > faturamento: # se o a empresa ter prejuizo, no caso o faturamento for menor q o investimento, printara o prejuizo
    print(linha + '\n')
    print(f'      A empresa levou PREJUIZO  nas  vendas de refrigerantes : R${faturamento - investimento:,.2f} ')
    print('\n' + linha)
else: # se o a empresa ter lucro, no caso o faturamento for maior q o investimento, printara o lucro
    print(linha + '\n')
    print(f'      A empresa levou LUCRO nas vendas de refrigerante: R${faturamento - investimento:,.2f}  ')
    print('\n' + linha)