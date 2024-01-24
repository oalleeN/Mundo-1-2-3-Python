'''Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o 
comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. 
Importante: use cores.'''

from termcolor import colored

def sistema(msg):
    print(colored('~' * len(msg), 'white', 'on_green'))
    print(colored(f'{msg}', 'white', 'on_green'))
    print(colored('~' * len(msg), 'white', 'on_green'))

def acesso(txt):
    print(colored(f'~' * len(txt), 'white', 'on_blue'))
    print(colored(f'{txt}', 'white', 'on_blue'))
    print(colored(f'~' * len(txt), 'white', 'on_blue'))

def thefinal(msg):
    print(colored('~' * len(msg), 'white', 'on_yellow'))
    print(colored(f'{msg}', 'white', 'on_yellow'))
    print(colored('~' * len(msg), 'white', 'on_yellow'))

def socorro(a):
    acesso(f'  acessando o manual do comando \'{ajuda}\'  ')
    print('\033[7;30m', end='')
    help(a)
    print('\033[m', end='')
    
while True:
    sistema('  SISTEMA DE AJUDA PyHELP  ')
    ajuda = str(input('Função ou biblioteca: ')).lower()
    if ajuda == 'fim':
        thefinal(' PROGRAMA FINALIZADO ')
        break
    socorro(ajuda)
