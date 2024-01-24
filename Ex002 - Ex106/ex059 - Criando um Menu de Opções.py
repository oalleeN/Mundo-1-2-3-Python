''' Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))

select = int(input('Digite a opção que você deseja operar: \n [1] Somar \n [2] Multiplicar \n [3] Maior \n [4] Novos números \n [5] Sair do programa \n Digite aqui: '))

while select != 5:
    
    if select == 1:
        soma = valor1 + valor2
        print(f' A soma dos valores é {soma}')
        print('-=-=-' * 10)
        select = int(input('Digite a opção que você deseja operar: \n [1] Somar \n [2] Multiplicar \n [3] Maior \n [4] Novos números \n [5] Sair do programa \n Digite aqui: '))
    
    elif select == 2:
        mult = valor1 * valor2
        print(f' A multiplicação dos valores é de {mult}')
        print('-=-=-' * 10)
        select = int(input('Digite a opção que você deseja operar: \n [1] Somar \n [2] Multiplicar \n [3] Maior \n [4] Novos números \n [5] Sair do programa \n Digite aqui: '))
    
    elif select == 3:
        if valor1 > valor2:
            maior = valor1
            print(f'O maior valor é {maior}')
            print('-=-=-' * 10)
        if valor2 > valor1:
            maior = valor2
            print(f'O maior valor é {maior}')
            print('-=-=-' * 10)
        select = int(input('Digite a opção que você deseja operar: \n [1] Somar \n [2] Multiplicar \n [3] Maior \n [4] Novos números \n [5] Sair do programa \n Digite aqui: '))
    
    elif select == 4:
        valor1 = int(input('Digite um valor: '))
        valor2 = int(input('Digite outro valor: '))
        print('-=-=-' * 10)
        select = int(input('Digite a opção que você deseja operar: \n [1] Somar \n [2] Multiplicar \n [3] Maior \n [4] Novos números \n [5] Sair do programa \n Digite aqui: '))
        
print('Programa encerrado!')