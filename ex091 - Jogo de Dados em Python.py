'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. 
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'jogador 1': randint(1,6),
             'jogador 2': randint(1,6),
             'jogador 3': randint(1,6),
             'jogador 4': randint(1,6)}
print('Valores sorteados:')
ranking = list()
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True) #técnica para pegar qual o maior valor do "randint"
print(f'{"-=" * 5}{"Ranking do Jogadores":^5}{"-=" * 5}')  
for k, i in enumerate(ranking):
    print(f'{k+1}º Lugar: {i[0]} com {i[1]} pontos no dado.')
    sleep(1)
 