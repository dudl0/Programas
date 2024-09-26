import random
 
nipes = ["♦","♠","♥", "♣"]
cartas = ["A", "2", "3","4", "5", "6", "7", "Q", "J", "K"]
 
baralho = []
 
for naipe in nipes:
    for carta in cartas:
            baralho.append(naipe+carta)
 
print(baralho)
 
 
 
 
jogador1 = []
 
jogador2 = []
 
for i in range(3):
    p = random.choice(baralho)
    jogador1.append(p)
 
for i in range(3):
    p = random.choice(baralho)
    jogador2.append(p)
  
 
 
 
vira = random.choice(baralho)
 
 
 
index = baralho.index(vira)
print('------')
print(f'O vira é: {vira}')
print('------')
 
 
manilha = index
 
manilhaA = [0,10,20,30]
manilha2 = [1,11,21,31]
manilha3 = [2,12,22,32]
manilha4 = [3,13,23,33]
manilha5 = [4,14,24,34]
manilha6 = [5,15,25,35]
manilha7 = [6,16,26,36]
manilha8 = [7,17,27,37]
manilha9 = [8,18,28,38]
manilha10 = [9,19,29,39]
 
print('             ')
manilha_valor = ("♦" == 0, "♠" == 0, "♥" == 0, "♣" == 0)
if manilha in manilhaA:
    print('As manilhas do jogo são:')
    for i in manilha2:
        print(baralho[i])
    manilha2 = ('♦2' == 11, '♠2' == 12, '♥2' == 13, '♣2' == 14)
elif manilha in manilha2:
    print('As manilhas do jogo são:')
    for i in manilha3:
          print(baralho[i])
    manilha3 = ('♦3' == 11, '♠3' == 12, '♥3' == 13, '♣3' == 14)
elif manilha in manilha3:
    print('As manilhas do jogo são:')
    for i in manilha4:
          print(baralho[i])
    manilha4 = ('♦4' == 11, '♠4' == 12, '♥4' == 13, '♣4' == 14)
elif manilha in manilha4:
    print('As manilhas do jogo são:')
    for i in manilha5:
          print(baralho[i])
    manilha5 = ('♦5' == 11, '♠5' == 12, '♥5' == 13, '♣5' == 14)
elif manilha in manilha5:
    print('As manilhas do jogo são:')
    for i in manilha6:
          print(baralho[i])
    manilha6 = ('♦6' == 11, '♠6' == 12, '♥6' == 13, '♣6' == 14)
elif manilha in manilha6:
    print('As manilhas do jogo são:')
    for i in manilha7:
          print(baralho[i])
    manilha7 = ('♦7' == 11, '♠7' == 12, '♥7' == 13, '♣7' == 14)
elif manilha in manilha7:
    print('As manilhas do jogo são:')
    for i in manilha8:
          print(baralho[i])
    manilha8 = ('♦Q' == 11, '♠Q' == 12, '♥Q' == 13, '♣Q' == 14)
elif manilha in manilha8:
    print('As manilhas do jogo são:')
    for i in manilha9:
          print(baralho[i])
    manilha9 = ('♦J' == 11, '♠J' == 12, '♥J' == 13, '♣J' == 14)
elif manilha in manilha9:
    print('As manilhas do jogo são:')
    for i in manilha10:
          print(baralho[i])
    manilha10 = ('♦K' == 11, '♠K' == 12, '♥K' == 13, '♣K' == 14)
elif manilha in manilha10:
    print('As manilhas do jogo são:')
    for i in manilhaA:
          print(baralho[i])
    manilhaA = ('♦A' == 11, '♠A' == 12, '♥A' == 13, '♣A' == 14)
 
 
 
print('           ')
 
print(f'Jogador1:  {jogador1}')
print('           ')
print(f'Jogador2:  {jogador2}')
 
 
print('       ')
print('       ')
print('|Jogador1 selecione e jogue uma carta|')
print('|carta0|  |carta1|  |carta2|')
 
round1 = int(input())
carta_jogador1_round1 = (jogador1[round1])
print(carta_jogador1_round1)
 
 
 
 
 
print('       ')    
print('       ')    
print('       ')
print('       ')
print('|Jogador2 selecione e jogue uma carta|')
print('|carta0|  |carta1|  |carta2|')
 
round1 = int(input())
carta_jogador2_round1 = (jogador2[round1])
print(carta_jogador2_round1)
 
 
d1 = carta_jogador2_round1
d2 = carta_jogador1_round1
 
if carta_jogador2_round1 > carta_jogador1_round1:
     print('gg j1')
else:
     print('gg j2')
 
 