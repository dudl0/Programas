nome = input("Digite seu nome: ")
idade = int(input("Digite seua idade: "))
altura = float(input("Digite sua altura: "))
print(f"Nome: {nome}, idade: {idade} e altura: {altura: .2f}")
if idade <= 18:
    print(f"{nome} não possui idade para dirigir")
else:
    print(f"{nome} possui idade para dirigir")