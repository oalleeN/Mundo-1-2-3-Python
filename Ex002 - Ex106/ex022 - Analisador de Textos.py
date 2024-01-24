'''Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.'''
nome = input('Digite seu nome completo: ')
nome1 = nome.upper()
nome2 = nome.lower()
nomed = len(nome.replace(" ", ""))
nome3 = nome.split()
nome4 = len(nome3[0])

print(f'Seu nome completo: {nome} \nSeu nome completo maiúsculo: {nome1} \nSeu nome completo minúsculo: {nome2}')
print(f'Quantas letras tem seu nome sem considerar os espaços: {nomed} \nQuantas letras tem o primeiro nome: {nome4}')
