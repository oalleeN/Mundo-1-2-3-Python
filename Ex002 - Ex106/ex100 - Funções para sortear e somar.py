''' Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda 
função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.'''
from random import randint, random
from time import sleep

def sorteia(lista):
    print(f'Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)      # ESSA PARTE DO CÓDIGO É PARA MOSTRAR A 
        lista.append(n)         # LISTA SEM COLCHETE E VÍRGULA
        print(f'{n}', end=' ')
        sleep(0.3)
    print('Feito!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor # soma = soma + valor
    print(f'Somando os valores de pares de {lista}, temos {soma}')

numeros = list()
sorteia(numeros)
somaPar(numeros)