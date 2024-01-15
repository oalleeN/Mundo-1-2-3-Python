'''from datetime import date
nome = str(input('Digite seu nome, por favor!: '))
print(f'Seja bem-vindo(a), {nome}!')

data_nasci = int(input('Digite sua data de nascimento: '))

ano_atual = date.today().year
idade = ano_atual - data_nasci

if idade <= 9:
    print(f'A sua categoria é MIRIM!')

elif idade >= 9 and idade <= 14:
    print(f'A sua categoria é INFANTIL!')

elif idade >= 14 and idade <= 19:
    print(f'A sua categoria é JUNIOR!')

elif idade >= 19 and idade <= 20:
    print(f'A sua categoria é SÊNIOR!')

elif idade >= 20:
    print(f'A sua categoria é MASTER!')
'''

#ou 

from datetime import date
atual = date.today().year
nasci = int(input('Digite sua data de nascimento: '))
idade = atual - nasci

if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JUNIOR')
elif idade <= 25:
    print('Categoria: SÊNIOR')
elif idade >= 25:             #ou    else:
    print('Categoria: MASTER')

    




