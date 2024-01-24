'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
 O programa será interrompido quando o número solicitado for negativo. '''

t = 0
while True:
    t = int(input('Digite um número para visualizar a sua tabuada: '))

    if t <= 0 :
        break

    print(f' A tabuada de {t} é: ')

    print(f' {t} x 1 = {t*1} \n {t} x 2 = {t*2} \n {t} x 3 = {t*3}')
    print(f' {t} x 4 = {t*4} \n {t} x 5 = {t*5} \n {t} x 6 = {t*6}')
    print(f' {t} x 7 = {t*7} \n {t} x 8 = {t*8} \n {t} x 9 = {t*9} \n {t} x 10 = {t*10}')

print('ERRO')

# FORMA MAIS SIMPLIFICADA DE FAZER UMA TABUADA EM BAIXO:

t = 0 
c = 0
while True:
    t = int(input('Digite um valor para a tabuada: '))

    if t <= 0:
       break
    print(f'A tabuada de {t} é: ')

    for c in range(1, 11):
        conta = t*c
        print(f'{t} x {c} = {conta}')

print('Programa encerrado!')
