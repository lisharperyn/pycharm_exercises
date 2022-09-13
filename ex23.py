# Exercíco 2.3.2

inicio = int(input('Digite um valor inicial: '))
fim = int(input('Digite um valor final: '))
qtd_postivo = 0
qtd_par = 0
qtd_impar = 0
soma_positivo = 0
soma_par = 0
soma_impar = 0
cont = inicio

if inicio < fim:
    while cont <= fim:
        if cont > 0:
            qtd_postivo = qtd_postivo + 1
            soma_positivo = soma_positivo + cont
        if cont % 2 == 0:
            qtd_par = qtd_par + 1
            soma_par = soma_par + cont
        else:
            qtd_impar = qtd_impar + 1
            soma_impar = soma_impar + cont
        cont = cont + 1
    media_positivo = soma_positivo / qtd_postivo
    media_par = soma_par / qtd_par
    media_impar = soma_impar / qtd_impar
    print('Quantidade de valores positivos: {}' .format(qtd_postivo))
    print('Média de valores postivos: {}' .format(media_positivo))
    print('Quantidade de valores pares: {}' .format(qtd_par))
    print('Média de valores pares: {}' .format(media_par))
    print('Quantidade de valores ímpares: {}' .format(qtd_impar))
    print('Média de valores ímpares: {}' .format(media_impar))
else:
    print('Você digitou jum valor maior ou igual ao final. Encerrando o programa...')

