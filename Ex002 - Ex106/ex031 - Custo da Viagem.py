''' Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''
from termcolor import colored
pergunta =float(input('Digite a distância da sua viagem: '))

print(colored(f'Você está prestes a fazer uma viagem de {pergunta}km', 'grey'))

print(colored('-=-' * 20, 'red')) #style

if pergunta <=200:
    preço = pergunta * 0.50 # valor da tarifa por cada km
    print(colored(f'O valor a pagar pela passagem é o seguinte: {preço:.2f}', 'blue'))
else:
    preço = pergunta * 0.45 # valor da tarifa após passar os 200km de viagem 
    print(colored(f'O valor a pagar pela passagem é o seguinte: {preço:.2f}', 'blue'))

print(colored('-=-' * 20, 'red'))  #style
 