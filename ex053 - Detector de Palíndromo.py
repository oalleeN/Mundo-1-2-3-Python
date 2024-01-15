'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.'''

frase = str(input('Digite sua frase e veja se ela é um palíndromo: ')).strip().upper()
palavras = frase.split()
junto = '' .join(palavras)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print(f'Temos um palíndromo.')
else:
    print(f'Não é um palíndromo')
    