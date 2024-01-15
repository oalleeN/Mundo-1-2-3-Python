''' Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.'''
t = int(input('Digite um número para visualizar a sua tabuada: '))

print(f' A tabuada de {t} é: ')

print('\033[0;33m -=- \033[m' * 20)

print(f' {t} x 1 = {t*1} \n {t} x 2 = {t*2} \n {t} x 3 = {t*3}')
print(f' {t} x 4 = {t*4} \n {t} x 5 = {t*5} \n {t} x 6 = {t*6}')
print(f' {t} x 7 = {t*7} \n {t} x 8 = {t*8} \n {t} x 9 = {t*9} \n {t} x 10 = {t*10}')

print(f'\033[0;33m -=- \033[m' * 20)
