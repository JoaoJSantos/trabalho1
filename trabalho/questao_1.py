print('Seja bem vindo ao atacadão do João Vitor dos Santos')

quantidade = input('Entre com o valor da quantidade ')
quantidade = int(quantidade)

valor_produto = input('Entre com o valor do produto ')
valor_produto = float(valor_produto)

if quantidade <= 9:
    texto_desconto = '0% de desconto'
    porcentagem_desconto = 1

elif quantidade > 9 and quantidade < 100:
    texto_desconto = '5% de desconto'
    porcentagem_desconto = 0.05

elif quantidade >= 100 and quantidade < 1000:
    texto_desconto = '10% de desconto'
    porcentagem_desconto = 0.10
else:
    texto_desconto = '15% de desconto'
    porcentagem_desconto = 0.15

valor_total = quantidade * valor_produto

desconto = valor_total - (valor_total * porcentagem_desconto)
print('valor sem desconto foi R$ {:.2f}' .format(valor_total))
print('valor com desconto foi R$ {:.2f} ({})' .format(desconto, texto_desconto))
