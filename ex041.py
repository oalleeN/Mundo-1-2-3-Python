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
