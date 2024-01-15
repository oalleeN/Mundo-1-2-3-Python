''' Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com 
valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior'''

from random import choice, randint, random
from subprocess import check_output

def maior():
    print('-=' * 20)
    print('Analisando os valores passados...')
    numeros = []
    
    for c in range(0, 5):
        numeros.append(randint(0, 10))
        print(f'{numeros[c]}', end=' ')
    print(f'Foram informados {len(numeros)} valores ao todo.')
    print(F'O maior valor informado foi {max(numeros)}')
        
maior()
maior()
maior()
maior()
maior()
