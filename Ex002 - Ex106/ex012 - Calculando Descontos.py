''' Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''
p = float(input('Digite o valor do produto: '))

d = p * 5 / 100 # produto com 5% de desconto // exemplo proposto!

print(f'O valor do produto já com os 5% de desconto é de: R${d:.2f}')
