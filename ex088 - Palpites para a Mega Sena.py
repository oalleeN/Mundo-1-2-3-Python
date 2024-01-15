''' Faça um programa que ajuda um jogador da MEGA SENA a criar palpites. 
O programa vai parguntar quantos jogos serão gerados e vai sortear 6 números 
entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta. '''

from random import randint
from time import sleep

lista = list() # primeira lista
copy = list() # lista que irá receber todas as outras listas através da cópia

print('-' * 50)
print('          SORTEIO ALEATÓRIO DA MEGA SENA     ')
print('-' * 50)
sorteio = int(input('Quantos jogos você quer sortear? '))
total = 1

while total <= sorteio: #enquanto o total for menor-igual ao sorteio ele continuará rodando o programa.
    
    cont = 0 # para poder os números na lista serem contados normalmente de 1 até 6 (que foi o solicitado no ex)
    while True: # "While" para decidir os 6 valores da lista 

        num = randint(1, 60)
        if num not in lista:
            lista.append(num)   
            cont += 1  # para cada vez que o número for acrescentado na lista, o contador soma mais 1 até chegar em 6
        if cont >= 6: 
            break

    lista.sort()
    copy.append(lista[:])
    lista.clear()
    total += 1

print('-=' * 3, f'SORTEANDO {sorteio} JOGOS' ,'-=' * 3)

for i, j in enumerate(copy): # o "i" enumera e faz com que fique um embaixo do outro em ordem 
    sleep(1)                 
    print(f'JOGO {i+1}: {j} ') # e o "j" toma poder das listas


# RESOLUÇÃO DE ALUNOS NOS COMENTÁRIOS DO VIDEO

'''import random
for x in range(int(input('Number of games: '))):
    print(f'Game {x+1}: {random.sample(range(1, 61), 6)}') '''