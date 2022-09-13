print('PAGAMENTO: ')
print('1 - à vista')
print('2 - parcelamento em 3x')
print('3 - parcelamento em 5x')
print('4 - parcelamento em 10x')
print('Pressione outra tecla para sair')
op = int(input('Qual forma de parcelamento deseja fazer?'))
valor = float(input('Qual o preço do produto?'))

if op == 1:  # à vista, desconto de 5%
      valor_final = valor * 0.95
      print('Produto comprado à vista. Total a pagar: {}' .format(valor_final))

elif op == 2:  # em 3x sem alterações
      valor_final = valor
      parcela = valor_final / 3
      print('Produto parcelado em 3x. Total a pagar: {}. Valor da parcela:{}' .format(valor_final, parcela))
elif op == 3:  # em 5x com acréscimo de 2%
      valor_final = valor * 1.02
      parcela = valor_final / 5
      print('Produto parcelado em 5x. Total a pagar: {}. Valor da parcela: {}' .format(valor_final, parcela))
elif op == 4:  # em 10x com acréscimo de 8%
      valor_final = valor * 1.08
      parcela = valor_final / 10
      print('Produto parcelado em 10x. Total a pagar: {}. Valor da parcela: {}' .format(valor_final, parcela))
else:
     print('Operação inválida!')







