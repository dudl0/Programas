def classificar_alunos(alunos):
    #classifica cada aluno conforme a nota
    classificacao = [(aluno, 'Aprovado' if nota >= 7  else 'Recuperação' if nota >= 5  else 'Reprovado') for aluno, nota in alunos]
    return classificacao

resultado = 'A lista de resultado dos alunos APROVADOS e REPROVADOS é: '
linha = '------------------------------------------------------------------'
print('\n' + linha + '\n' + resultado + '\n') # organização
alunos_notas = [('Ana', 8), ('Biel', 5), ('Joao', 3), ('Du', 10)] # armazenando nota dos alunos
print(classificar_alunos(alunos_notas)) # chamando a função para rodar em [alunos_notas]  e fazer a verificação das aprovações
print(linha +'\n')