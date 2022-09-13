# Operadores especiais de atribuição

x = 1
while x <= 5:
    print(x)
    x += 1  # Equivalente: x = x + 1

soma = 0
cont = 1
while cont <= 5:
    x = int(input('Digite o {}° número:' .format(cont)))
    soma += x  # Equivalente: soma = soma + x
    cont += 1  # Equivalente: cont = cont + 1
print('Somatório: {}' .format(soma))

# Validar o dado de entrada com um loop

x = int(input('Digite um valor maior do que zero: '))
while x <= 0:
    x = int(input('Digite um valor maior do que zero: '))
print('Você digitou {}. Encerrando o programa...' . format(x))

# Saindo quando quiser

print('Digite uma mensagem que irei repetir para você!')
print('Para encerrar digite "sair".')
texto = input('')
while texto != 'sair':
    print(texto)
    texto = input('')
print('Encerrando programa...')

