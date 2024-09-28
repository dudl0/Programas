def BubbleSort(lista):
    tamanho = len(lista)
    print(tamanho)
    for i in range(tamanho):
        for j in range(0, tamanho -1):
            if lista[j]>lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista
lista = [2,12,3,0,8,90,69,102]
lista_ordenada = BubbleSort(lista)

print('Lista Ordenada:', lista_ordenada)