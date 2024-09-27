import os

preco = 5.25
distancia = 1000
carros = []
consumos = []

os.system('cls')

while True:
    carro = input('Modelo do Carro: ')
    if carro == '':
        break 
    consumo = float(input('Consumo do carro por km²: '))
    if carro in carros:
        index = carros.index(carro)
        consumos[index].append(consumo)
        consumo = None
    else:
        carros.append(carro)
        consumos.append([consumo])
    print()


media_consumos = [sum(consumo)/len(consumo) for consumo in consumos]
melhor_consumo = consumos.index(max(consumos))
menos_economico = consumos.index(min(consumos))

print('\n')
for i in range(len(carros)):
    valor = distancia/media_consumos[i]
    print('O carro', carros[i], 'deverá consumir: ', valor, 'litros de combustiveis', '\n', 'e terá um gasto de: ', 'R$',valor*preco )
    print('\n' + '--------------------------------------------------------------------------------------------------')


print('\n')
print('O carro MENOS economico é o: ', carros[menos_economico])
print('\n' + '--------------------------------------------------------------------------')
print('\n')
print('O carro MAIS economico é o: ', carros[melhor_consumo])
print('\n')
