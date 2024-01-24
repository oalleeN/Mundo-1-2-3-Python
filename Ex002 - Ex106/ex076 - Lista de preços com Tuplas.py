''' Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

listagem = ('Carregador', 150.00,
            'Fone de Ouvido', 50.00,
            'Cabo para carregador', 53.30,
            'Cabo USB', 24.50,
            'Caderno Digital', 15.20,
            'Microfone', 67.45,)
print('-' * 40)
print(f'{"Listagem de Preços" :^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end=' ')
    else:
        print(f'R${listagem[pos]:>6.2f}') # ".2f" quer dizer que é duas casas decimais no máximo após a vírgula 
