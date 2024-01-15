''' Faça um programa que leia o comprimento do cateto 
oposto e do cateto adjacente de um triângulo retângulo. 
Calcule e mostre o comprimento da hipotenusa.'''
from math import sqrt 
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

h = (co**2) + (ca**2)

print(f'o valor da hipotenusa é {sqrt(h):.2f}')

#-----------------------------------------------------------

import math

co = float(input('digite o valor do cateto oposto: '))
ca = float(input('digite o valor do cateto adjacente: '))

hi = math.hypot(co, ca)

print(f'o valor da hipotenusa é {hi:.2f}')

#-----------------------------------------------------------

co = float(input('digite o valor do cateto oposto: '))
ca = float(input('digite o valor do cateto adjacente: '))
hi = (co**2 + ca**2) **(1/2)

print(f'o valor da hipotenusa é {hi:.2f}')
