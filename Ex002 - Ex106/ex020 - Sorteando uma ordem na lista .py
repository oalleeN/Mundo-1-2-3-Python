'''O mesmo professor do desafio 019 quer sortear a ordem de 
apresentação de trabalhos dos alunos. Faça um programa que 
leia o nome dos quatro alunos e mostre a ordem sorteada.'''
import random
a1 = str(input('Aluno 01: '))
a2 = str(input('Aluno 02: '))
a3 = str(input('Aluno 03: '))
a4 = str(input('Aluno 04: '))

lista = [a1, a2, a3, a4]
random.shuffle(lista)

print(f'Ordem de apresentação: ')

print(lista)
