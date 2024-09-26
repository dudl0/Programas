codigos = ['BCA001','BSA001','BCA002','BSA002','BCA003','BSA003'] # código de bebidas alcoolicas, 'BCA001' é alcoolico, 'BSA001' não possui alcool
linha = '-------------------------------------------------------------------------------------------------------'


print('\n' + linha)
bebida = input('insira o código da bebida em letra MAISCÙLA: ')


if 'BCA' in bebida:
    print('\n' + linha )
    print('este código está referente a bebida ALCOÒLICA e o código referente é: ', codigos[0])
    print('\n' + linha)
elif 'BSA' in bebida: 
    print('\n' + linha)
    print('este código está referente a bebida SEM ALCOÒL e o código referente é: ', codigos[1])
    print(linha)
else:
    print('\n' + linha )
    print('O código digitado não foi encontrado, digite novamente')
    print('\n')