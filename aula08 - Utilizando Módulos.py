import math
numero = int(input('Digite um número: '))

raiz = math.sqrt(numero)

print(f'A raiz quadrada de {numero} é igual a {raiz:.3f} ')
print(f'A raiz já arredondada é igual a {math.ceil(raiz)}')
