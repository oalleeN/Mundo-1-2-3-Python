'''Crie um programa que faça o computador jogar Jokenpô com você.'''

from random import randint
from time import sleep

itens = ['Pedra', 'Papel', 'Tesoura']

computador = randint(0 , 2)

print('''SUA OPÇÕES: 
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

player = int(input('DIGITE AQUI: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(2)
print('-=-' * 11)

print(f'Computador jogou: {itens[computador]}')
print(f'Player jogou: {itens[player]}')

print('-=-' * 11)

if computador == 0: #PEDRA
    if player == 0:
        print('EMPATE!')
    elif player == 1:
        print('PLAYER VENCEU!')
    elif player == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('Jogada inválida!')

if computador == 1: #PAPEL
    if player == 0:
        print('COMPUTADOR VENCEU!')
    elif player == 1:
        print('EMPATE!')
    elif player == 2:
        print('PLAYER VENCEU!')
    else:
        print('Jogada inválida!')

if computador == 2: #TESOURA
    if player == 0:
        print(' PLAYER VENCEU!')
    elif player == 1:
        print('COMPUTADOR VENCEU!!')
    elif player == 2:
        print('EMPATE!')
    else:
        print('Jogada inválida!')
