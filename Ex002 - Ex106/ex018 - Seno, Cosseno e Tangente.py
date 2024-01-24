'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''
import math
a = float(input('digite um valor: '))

seno = math.sin (math.radians(a))
coss = math.cos (math.radians(a))
tang = math.tan (math.radians(a))

print(f' O valor em seno é {seno:.2f} \n O valor em cosseno é {coss:.2f} \n O valor da tangente é {tang:.2f}')

#-------------------------------------------------------------------------------------------------------------

from math import sin, cos, tan, radians
ângulo = float(input('digite o ângulo: '))

seno = sin (radians(ângulo))
coss = cos (radians(ângulo))
tang = tan (radians(ângulo))

print(f'O seno é {seno:.2f} \nO cosseno é {coss:.2f} \nA tangente é {tang:.2f}')
