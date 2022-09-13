ano_nasc = int(input('Digite seu ano de nascimento:'))
ano_atual = int(input('Em que ano estamos: '))
idade = ano_atual-ano_nasc
print('Você tem {} anos de idade.' .format(idade))
if idade>=18:
    print('Você é maior de idade. Já pode tirar a carteira de motorista!')
