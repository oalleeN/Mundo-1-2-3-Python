'''Faça um programa que leia nome e média de um aluno, guardando também a 
situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''

dados = dict()

dados['nome'] = str(input('Nome: '))
dados['média'] = float(input(f'Média de {dados["nome"]}: '))
print(f'Nome é igual a {dados["nome"]}')
print(f'Média é igual a {dados["média"]}')
if dados["média"] <= 6.9:
    print('Situação é igual a REPROVADO(A)')
else:
    print('Situação é igual a APROVADO(A)')