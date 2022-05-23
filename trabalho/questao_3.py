def dimensoesObejto():
    dimensao = 100000
    comprimento = 0
    altura = 0
    largura = 0
    while dimensao >= 100000:
        repetir_comprimento = True
        while repetir_comprimento:
            try:
                comprimento = float(input('digite o comprimento do obejto (em cm):'))
                repetir_comprimento = False
            except:
                print('digite valores numericos')


        repetir_altura = True
        while repetir_altura:
            try:
                altura = float(input('digite a altura do obejto (em cm) :'))
                repetir_altura = False
            except:
                print('digite valores numericos')

        repetir_largura = True
        while repetir_largura:
            try:
                largura = float(input('digite a largura do objeto (em cm) :'))
                repetir_largura = False
            except:
                print('digite valores numericos')

        dimensao = largura * altura * comprimento
        print('dimensao (em cm) :', dimensao)
        if dimensao >= 100000:
            print('não aceitamos objetos com valores tão grandes')

    return dimensao

def pesoObjeto():
    peso = 0
    repetir_peso = True
    while repetir_peso:
        try:
           peso = float(input('digite o peso do objeto (em Kg) :'))
           if peso >= 30:
               print('não aceitamos objetos tão pesados')
               print('entre com o peso desejado novamente')
           else:
               repetir_peso = False
        except:
            print('digite valores numericos')
            print('entre com o peso desejado novamente')

    return peso

rota = ''
def rotaObjeto():
    repetir_rota = True
    while repetir_rota:
        print('BR - De Brasilia para Rio de Janeiro')
        print('BS - De Brasilia para São paulo')
        print('RB - De Rio de janeiro para Brasilia')
        print('RS - De Rio de Janeiro para São paulo')
        print('SR - De São Paulo para Rio de Janeiro')
        print('SB - De São paulo para Brasilia')
        rota = input('selecione a rota :')
        siglas = ['BR','BS','RB','RS','SR','SB']
        if not rota in siglas:
            print('voce digitou uma rosa que não existe')
            print('por favor digite uma rota existente')

        else:
            repetir_rota = False

    return rota

dimensao = dimensoesObejto()
peso = pesoObjeto()
rota = rotaObjeto()

valor_dimensao = 0

if dimensao < 1000:
    valor_dimensao = 10
elif dimensao >= 1000 and dimensao < 10000:
    valor_dimensao = 20
elif dimensao >= 10000 and dimensao < 30000:
    valor_dimensao = 30
elif valor_dimensao >= 30000 and dimensao < 100000:
    valor_dimensao = 50
else:
    print('não é aceito')

peso_mutiplicador = 0

if peso <= 0.1:
    peso_mutiplicador = 1
elif peso >= 0.1 and peso < 1:
    peso_mutiplicador = 1.5
elif peso >= 1 and peso < 10:
    peso_mutiplicador = 2
elif peso >= 10 and peso < 30:
    peso_mutiplicador = 3
else:
    print('não é aceito')

rota_mutiplicador = 0

if rota == 'RS':
    rota_mutiplicador = 1
elif rota == 'SR':
    rota_mutiplicador = 1
elif rota == 'BS':
    rota_mutiplicador = 1.2
elif rota == 'SB':
    rota_mutiplicador = 1.2
elif rota == 'BR':
    rota_mutiplicador = 1.5
elif rota =='RB':
    rota_mutiplicador = 1.5

total = valor_dimensao * peso_mutiplicador * rota_mutiplicador
print(f'total a pagar (R$) {total} (dimensao: {dimensao} * peso: {peso} * rota: {rota}')









g














































