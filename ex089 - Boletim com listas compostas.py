'''Cria um programa que leia nome e duas notas de vários alunos e guarda tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as 
notas de cada aluno individualmente.'''

dados = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], média])
    resp = str(input('Deseja continuar? [S/N]: ')).upper()
    if resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).upper()
        if resp in 'N':
            break
    elif resp in 'N':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>12}')
print('-' * 26)
for c, n in enumerate(dados):
    print(f'{c:<4} {n[0]:<10} {n[2]:>8.1f}')
while True:
    print('-' * 30)
    opc = int(input('Mostrar as notas de qual aluno? (999 para interromper...): '))
    if opc == 999:
        print('finalizando...')
        break
    if opc <= len(dados) -1:
        print(f'Notas de {dados[opc][0]} são {dados[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
