# Exercíco 3.6.1

soma = 0
qtd_numero = 0
x = 0

while True:
    x = int(input('Digite um valor inteiro:'))
    if x <= 0:
        continue
    if not x:
        break
    soma += x
    qtd_numero += 1
media = soma / qtd_numero
print('A média dos valores digitados é: {}' .format(media))