letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

#o [-1] puxa o final da lista, e o [-10] o começo, só que utilizando negativo
print(letras[-1])
print(letras[-10])
print('\n' + '----------------------------------------------------')




#---------------------------------------------------------------------
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


print('Indices Positivos')
for i in range(len(letras)):
    print(f'indice {i}: {letras[i]}')


print('Indices Negativos')
for i in range(-1,-len(letras)-1, -1):
    print(f'indice {i}: {letras[i]}')