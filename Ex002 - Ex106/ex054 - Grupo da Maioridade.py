'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas 
pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

from datetime import date
ano = date.today().year
for i in range(1, 7 + 1):
    nasci = int(input('Digite seu ano de nascimento: '))
    idade = ano - nasci

    if idade >= 21:
        print('Você atingiu a maioridade.')
    else:
        print('Você ainda não atingiu a maioridade')

print('FIM.')