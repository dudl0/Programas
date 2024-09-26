pesomin = None
pesomax = None
altmin = None
altmax = None
imc = None
 
def verificacaoidade(idade):
    while idade < 0:
       idade = int(input('idade inválida, tente novamente: '))
 
 
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
 
 
   
sexo = str(input('digite seu sexo (M para masc. ou F para fem.): '))
massa = float(input('digite sua massa em kg: '))
altura = float(input('digite sua altura em metros: '))
 
print(sexo, massa, altura)
 
def calcimc(altura, massa):
    global pesomin, pesomax, altmax, altmin
    if massa >= pesomin and massa <= pesomax and altura >= altmin and altura <= altmax:
        imc = massa/(altura*altura)
        print(imc)
        return imc
   
    else:
        print('dados de massa ou altura, incompátiveis com a idade')
        return
 
 
calcimc(altura, massa)
 
 
def status(sexo):
    imc = massa/(altura*altura)
    if sexo == "M":
        if imc <= 20:
            print('você está abaixo do peso normal')
            return 'você está abaixo do peso normal'
       
        if imc <= 24.9 and imc > 20 and sexo == "M" :
            print('você está abaixo do peso normal')
            return 'você está abaixo do peso normal'
       
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
           
                print('você está abaixo do peso normal')
                return 'você está abaixo do peso normal'
       
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