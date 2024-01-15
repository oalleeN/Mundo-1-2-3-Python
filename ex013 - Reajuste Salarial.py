''': Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.'''
s = float(input('Para a compra no crédito, digite o valor do produto: '))

a = s + (s * 5 / 100)
b = s - (s * 20 / 100)


print(f'O valor do produto parcelo em 8x terá um aumento no preço original de 5% e ficará: R${a:.2f}')
print(f'O produto pago à vista terá um desconto de 20% e ficará: R${b:.2f}')
