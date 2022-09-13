x = int(input('Digite um valor inteiro: '))

if x%2==0:
#podemos obter o resto de uma divisão diretamente utilizando o símbolo de percentual. obtemos o resto da divisão por 2 e, em seguida, pela comparação lógica de igualdade verificamos se é igual a zero. ademais, a ordem de precedência dos operadores também deve ser respeitada aqui. primeiro, o cálculo aritmético é realizado, e por último, o teste lógico.


    print('O número é par!')

else:

    print('O número é ímpar!')

if x%7==0:
    print('Múltiplo de 7!')

else:
    print('Não é múltiplo de 7!')
