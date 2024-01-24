'''Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.'''
nome = input('digite seu nome:')
print('É um prazer te conhecer, {}!' .format(nome))

# formato novo!

nome = input('digite seu nome:')
print('É um prazer te conhecer,', nome+'!')

# formato antigo!

nome = input('digite seu nome:')
print(f'É um prazer te conhecer, {nome}!')

# Mais atual!
