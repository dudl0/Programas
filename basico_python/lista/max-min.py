#o método max e min, puxam o valor maximo e minimo de uma lista

valores = [100, 200, 300]


valor_max = max(valores)
valor_min = min(valores)

print('\n')
print('O valor maximo é: {} E o valor minimo é: {}'.format(valor_max,valor_min))
print('\n' + '----------------------------------------------------')
#-----------------------------------------------------------------------------------

valores = [100, 200, 300]


vendas_max = max(valores)
vendas_min = min(valores)
index_max = valores.index(vendas_max)
index_min = valores.index(vendas_min)


print('\n')
print('O modelo mais vendido: {} Valor das vendas: {}'.format(index_max,valor_max))
print('O modelo menos vendido: {} Valor das vendas: {}'.format(index_min,valor_min))