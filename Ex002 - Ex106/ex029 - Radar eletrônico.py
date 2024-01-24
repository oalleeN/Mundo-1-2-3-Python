''' Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma 
mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''
from termcolor import colored
from random import choice
#v = choice(range(1, 300))
v = float(input('Digite a sua velocidade: '))


if v >=80:
    print('-=-' * 30)
    print(colored(f'Você foi mutado por excesso de velocidade. Você ultrapassou a marca dos 80km/h e atingiu {v}km/h', 'red'))
    multa = (v - 80) * 7
    print(colored( f'E a sua multa custará o valor de R${multa:.2f}', 'red'))
    print('-=-' * 30)
else:
    print('-=-' * 30)
    print(colored('Você não foi mutado!', 'green'))
    print('-=-' * 30)
