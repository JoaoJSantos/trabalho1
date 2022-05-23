print('Seja bem vindo ao restaurante do João Vitor dos Santos')
#tabela do cardapio
print('***************Cardápio***************')
print('|  Código |       Descrição        | Valor |')
print('|   100   |     Cachorro Quente    |  9,00 |')
print('|   101   |  Cachorro Quente Duplo | 11,00 |')
print('|   102   |         X-EGG          | 12,00 |')
print('|   103   |         X-SALADA       | 13,00 |')
print('|   104   |         X-BACON        | 14,00 |')
print('|   105   |         X-TUDO         | 17,00 |')
print('|   200   |    Refrigerante Lata   |  5,00 |')
print('|   201   |       Chá Gelado       |  4,00 |')
#variavel do total da conta
total_da_conta = 0

#while de repetção do pedido
while True:

    pedido = int(input('qual o codigo do produto desejao?'))
    if pedido == 100:
        total_da_conta = total_da_conta + 9.00
    elif pedido == 101:
        total_da_conta = total_da_conta + 11.00
    elif pedido == 102:
        total_da_conta = total_da_conta + 12.00
    elif pedido == 103:
        total_da_conta = total_da_conta + 13.00
    elif pedido == 104:
        total_da_conta = total_da_conta + 14.00
    elif pedido == 105:
        total_da_conta = total_da_conta + 17.00
    elif pedido == 200:
        total_da_conta = total_da_conta + 5.00
    elif pedido == 201:
        total_da_conta = total_da_conta + 4.00
    else:
        print('\ncodigo do produto não encontrado\n')
        continue

    print('deseja mais alguma coisa?')
    print('1 - Sim')
    print('0 - Não')
    condicao = input()
    if condicao == '0':
        break
print('O total a ser pago é:{}'.format(total_da_conta))






