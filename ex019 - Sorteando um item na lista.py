'''Um professor quer sortear um dos seus quatro 
alunos para apagar o quadro. Faça um programa que ajude ele, 
lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''
import random
a1 = input('Aluno 01: ')
a2 = input('Aluno 02: ')
a3 = input('Aluno 03: ')
a4 = input('Aluno 04: ')

sorteio = random.choice([a1, a2, a3, a4])

print(f'O aluno sorteado foi o(a) {sorteio}!')

#-----------------------------------------------

from random import choice

a1 = input('Aluno 01: ')
a2 = input('Aluno 02: ')
a3 = input('Aluno 03: ')
a4 = input('Aluno 04: ')

escolhido = choice([a1, a2, a3, a4])

print(f'O aluno(a) escolhido(a) foi o(a) {escolhido}')
