# Interrompendo loop com break

print('Digite uma mensagem que irei repetir para você!')
print('Para encerrrar escreva "sair".')
while True:
    texto = input('')
    if texto == 'sair':
        break
print('Encerrando o programa...')

# Voltando ao início do loop com continue

while True:
    nome = input('Qual seu nome?')
    if nome != 'Lenhadorzinho':
        continue
    senha = input('Qual sua senha?')
    if senha == 'SeNha':
        break
print('Acesso concedido.')

