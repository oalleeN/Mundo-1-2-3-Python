''' Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''
ano = int(input('Que ano quer analisar? '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} bissexto!')
else: 
    print(f'O ano de {ano} não é bissexto! ')

    