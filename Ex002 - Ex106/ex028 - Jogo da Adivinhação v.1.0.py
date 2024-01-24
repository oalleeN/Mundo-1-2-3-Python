''' Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e 
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa 
deverá escrever na tela se o usuário venceu ou perdeu.'''
from termcolor import colored
from random import randint
pc = randint(0, 10)
player = ''
soma = 1
print(colored('-=-' * 20, 'black'))
print(colored('SÉRA QUE TU CONSEGUES ME GANHAR!?', 'green'))
print(colored('Digite um número entre 0 e 5', 'yellow'))
print(colored('-=-' * 20, 'black'))
while player != pc:
    player = int(input('Digite um número e tente me vencer! Tente... '))
    if pc != player:
        print('Tente novamente.')
if player == pc:
    print(colored(f'FINALMENTE ganhou algo na vida.', 'red'))
soma = pc + soma
print(f'Você usou {soma}')
