''' Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer'''

from termcolor import colored
from random import randint
print(colored('-=-' * 20, 'black'))
print(colored('SÉRA QUE TU CONSEGUES ME GANHAR!?', 'green'))
print(colored('Digite um número entre 0 e 5', 'yellow'))
print(colored('-=-' * 20, 'black'))

pc = randint(0, 10)
player = int(input('Digite um número e tente me vencer! Tente... '))
soma = 1

while player != pc:
    print('Tente novamente.')
    player = int(input('Digite um número e tente me vencer! Tente... '))
    pc = randint(0, 10)
    soma += 1 
    
print(f'Parabéns, você venceu! Você usou {soma} tentivas!')

#---------------------------------------------------------

#mais simples e prático!
from random import randint
pc = randint(0, 10)
print('pensei em um número, tente acerta-lo')
tentativas = 0
acertou = False

while not acertou:
    player = int(input('Digite um valor entre 0 e 10: '))
    tentativas += 1
    if player == pc:
        acertou = True
    else: 
        print('Tente novamente!')
print(f'Parabéns, você me venceu! Você usou {tentativas} tentativas para me vencer.')
