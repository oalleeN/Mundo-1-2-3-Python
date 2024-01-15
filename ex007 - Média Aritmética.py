''' Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.'''
nome = input('Digite seu nome: ')
print(f'Bem-vindo(a), {nome}')

nota1 = float(input('Digite a sua nota 1º bimestre: '))
nota2 = float(input('Digite a sua nota 2º bimestre, por favor:'))

s = nota1 + nota2
mf = (nota1 + nota2) / 2

print(f' Sua nota total ficou a seguinte: {s} \n Sua média final ficou a seguinte: {mf:.1f}')

