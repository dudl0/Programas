import random
 
def monty_hall(escolha_usuario):
    # Lista das portas
    portas = ['A', 'B', 'C']
   
    # Escolha aleatória de qual porta tem o carro
    carro_porta = random.choice(portas)
   
 
   
    # Monty escolhe uma porta que não tem o carro nem é a escolha do usuário
    portas_restantes = [porta for porta in portas if porta != carro_porta and porta != escolha_usuario]
    porta_aberta = random.choice(portas_restantes)
   
    # Mostrar qual porta Monty abriu
    print("Monty abre a porta", porta_aberta)
   
    # O usuário decide se quer trocar de porta ou não
    trocar = input("Você quer trocar de porta? (sim/não): ").lower().strip() == 'sim'
   
    if trocar:
        # Se o usuário decidir trocar, a nova escolha será a porta que não foi escolhida anteriormente e que não foi aberta por Monty
        nova_escolha = [porta for porta in portas if porta != escolha_usuario and porta != porta_aberta][0]
        escolha_usuario = nova_escolha
   
    # Mostrar o resultado final
    if escolha_usuario == carro_porta:
        print("Parabéns! Você ganhou o carro!")
    else:
        print("Que pena! O carro estava atrás da porta", carro_porta)
 
# Permitir que o usuário escolha uma porta
escolha_usuario = input("Escolha uma porta (A, B ou C): ").upper().strip()
while escolha_usuario not in ['A', 'B', 'C']:
    print("Escolha inválida. Por favor, escolha uma porta válida (A, B ou C).")
    escolha_usuario = input("Escolha uma porta (A, B ou C): ").upper().strip()
 
# Executar o jogo
monty_hall(escolha_usuario)