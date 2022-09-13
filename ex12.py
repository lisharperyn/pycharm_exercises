salario = float(input('Qual é o seu salário?'))
ano_admissao = int(input('Em que ano foi contratado?'))
ano_atual = int(input('Em que ano estamos?'))
tempo = ano_atual-ano_admissao
if tempo>=5:
    bonus = salario*0.2
else:
    bonus = salario*0.1

print('Você tem {} anos dentro desta empresa.' .format(tempo))
print('Seu salário é de {}.' .format(salario))
print('Sua bonificação é de {}.' .format(bonus))
print('Portanto, seu salário final é de {}.' .format(bonus + salario))
