'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.'''
nome = str(input("Digite seu nome completo: ")).split()


primeiro = nome[0]
ultimo = nome[-1]

print(f'Nome completo: {nome}')
print(f'Primeiro nome: {primeiro}')
print(f'Último nome: {ultimo}')
