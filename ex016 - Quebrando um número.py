''' Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a 
sua porção Inteira.'''
import math
numero = float(input(' Digite um número real qualquer: '))

print(f' O número {numero} tem a parte inteira {math.trunc(numero)}')

#------------------------

from math import trunc
a = float(input('digite um número real: '))
print(f' o valor inteiro de {a} é igual à {trunc(a)}')

#------------------------

numero = float(input('digite um número real: '))
print(f'O valor inteiro de {numero} é igual a {int(numero)}')
