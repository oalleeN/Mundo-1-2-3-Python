''' Crie um programa que leia um número inteiro e mostre 
na tela se ele é PAR ou ÍMPAR.'''
from termcolor import colored
numero = int(input('Digite um número inteiro: '))

result = numero % 2

print(colored('-===-' * 10, 'red')) #style

if result == 0:
    print('O valor é par!')
else:
    print('O valor é ímpar!')

print(colored('-===-' * 10, 'red')) #style