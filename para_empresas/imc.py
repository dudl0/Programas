import os

# essas variveis terao valores diferentes mais a frente, então estão definidas como nulas no momento
pesomin = None
pesomax = None
altmin = None
altmax = None
imc = None
 
def verificacaoidade(idade): # funcao para caso alguem coloque idade negativa
    while idade < 0:
       idade = int(input('idade inválida, tente novamente: '))
 
 
 # essa funcao delimita para ninguem colocar uma informação fora do comum para a idade, ex: 'Tenho 5 anos e 2 metros de altura' -> a funcao n permite q isso aconteça
def parametriza(idade): 
    global pesomin, pesomax, altmin, altmax
    if idade >= 0 and idade <=8:
        pesomin = 2.5
        pesomax = 40
        altmin = 0.4
        altmax = 1.5
    elif idade >= 0 and idade <= 18:
        pesomin = 30
        pesomax = 250
        altmin = 1.3
        altmax = 2.2
    else:
        pesomin = 35
        pesomax = 500
        altmin = 1.35
        altmax = 2.5
 
 
idade = int(input('digite a idade: '))
verificacaoidade(idade)
parametriza(idade)
 
os.system('cls')
   
sexo = str(input('digite seu sexo (M para masculino. ou F para fem.): '))
massa = float(input('digite sua massa em kg: '))
altura = float(input('digite sua altura em metros: '))
 

os.system('cls')


print(f'Seu sexo é: {sexo}  /  Seu peso é: {massa}  /  Sua altura é: {altura}' + '\n')
print('-----------------------------------------------------------------------------') 
 
def calcimc(altura, massa): # utiliza os dados da funcao parametriza para retornar se esta coerente, se estiver ok, retorna o calculo do imc
    global pesomin, pesomax, altmax, altmin
    if massa >= pesomin and massa <= pesomax and altura >= altmin and altura <= altmax:
        imc = massa/(altura*altura)
        print(f'Seu imc é: {imc}' + '\n')
        print('-----------------------------------------------------------------------------')
        return imc
   
    else:
        print('dados de massa ou altura, incompátiveis com a idade')
        return
 
 
calcimc(altura, massa) # executa a funcao
 


# essa funcao diz se vc esta magro demais ou gordo demais, e é diferente de homem para mulher 
def status(sexo):
    imc = massa/(altura*altura)
    if sexo == "M": # utiliza da String que foi usada para definir o sexo para diferenciar o imc da mulher para o do homem
        if imc <= 20:
            print('você está abaixo do peso normal')
            return 'você está abaixo do peso normal'
       
        if imc <= 24.9 and imc > 20 and sexo == "M" :
            print('você está no peso ideal')
            return 'você está no peso ideal'
       
        if imc <= 29.9 and imc > 20 and sexo == "M":
            print('você está em obesidade leve')
            return 'você está em obesidade leve'
       
        if imc <= 39.9 and imc >= 30 and sexo == "M":
            print('você está em obesidade moderada')
            return 'você está em obesidade moderada'
       
        if imc >= 43 and sexo == "M":
            print('você está em obesidade moderada')
            return 'você está em obesidade moderada'
    else:
        if sexo == "F":
           
            if imc <= 19:
           
                print('você está no peso ideal')
                return 'você está no peso ideal'
       
            if imc <= 23.9 and imc > 20 and sexo == "F" :
                print('você está abaixo do peso normal')
                return 'você está abaixo do peso normal'
       
            if imc <= 28.9 and imc > 20 and sexo == "F":
                print('você está em obesidade leve')
                return 'você está em obesidade leve'
       
            if imc <= 38.9 and imc >= 30 and sexo == "F":
                print('você está em obesidade moderada')
                return 'você está em obesidade moderada'
       
            if imc >= 39 and sexo == "F":
                print('você está em obesidade moderada')
                return 'você está em obesidade moderada'
           
       
 
   
status(sexo)