# Truthy e Falsey
# O Python considera o numeral zero, tanto inteiro quanto em ponto flutuante, como um valor
# Falsey e pode ser tratado na linguagem como False. Assim como uma string vazia (quando só
# colocamos aspas simples sem caracteres dentro) também é um dado Falsey. Todos os outros dados
# não listados podem ser tratados como Truthy/True pela linguagem.
#  Nele, inicializamos a variável nome com uma string vazia. Isso
# significa que, se utilizarmos essa variável em um teste lógico com ela estando vazia, seu valor será
# interpretado como False.
# Na linha 2, fazemos um teste lógico no qual estamos negando a variável nome (while not nome).
# Fazer isso é o equivalente a fazer while True, pois a string vazia é False e, ao negá-la, invertemos seu
# valor para True. Assim, fazemos com que o programa caia dentro do laço de repetição e solicite um
# nome.

nome = ''
while not nome:
    nome = input('Digite seu nome:')
valor = int(input('Digite um número qualquer: '))
if valor:
    print('Você digitou um valor diferente de zero.')
else:
    print('Você digitou zero.')

#Após o laço de repetição, temos a leitura de um valor numérico e inteiro qualquer na variável valor. Em seguida, na linha 5, fazemos um teste condicional colocando somente if valor. Quando fazemos isso, o Python irá interpretar o número digitado como um valor lógico. Caso você digite zero, o teste lógico resultará em False, caindo no else. Caso digite qualquer outro número, como 10, o teste lógico será True.
