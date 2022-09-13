print('Bem-vindo à loja da Stéffani Araújo de Amorim')  # RU: 4002091
valor_produto = float(input('Entre com o valor do produto: '))
quant_produto = int(input('Entre com a quantidade do produto: '))
subtotal = valor_produto * quant_produto

if quant_produto <= 4:
    valor_final = subtotal
elif 5 <= quant_produto <= 19:  # subtotal >= 5 and subtotal <=400
    valor_final = subtotal - subtotal * 0.03  # desconto de 3%
elif 20 <= quant_produto <= 99:
    valor_final = subtotal - subtotal * 0.06  # desconto de 6%
else:  # para qualquer outro valor igual ou acima de 100
    valor_final = subtotal - subtotal * 0.10  # desconto de 10%

print('O valor sem desconto: {}' .format(subtotal))
print('O valor com desconto: {}' .format(valor_final))
