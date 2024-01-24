''' Faça um programa que leia a largura e a altura de uma parede em metros, calcule a 
sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de 
tinta pinta uma área de 2 metros quadrados.'''
l = float(input('Digite a largura da sua parede: '))
h = float(input('Digite a altura da sua parede: '))

a = l * h # altura e largaura para cálcular a área total em m²

print(f'A área da sua parede é de {a:.0f} m²')

t = float(input('Digte quantos litros de tinta você possui: '))

qn = a/2     # quantindade necessária de tinta.

print(f'A quantidade de tinta necessária para você pintar a parede toda, considerando que cada litro pinta 2m², é de: {qn:.0f} l')