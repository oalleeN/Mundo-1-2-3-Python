'''Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.'''
g = float(input('Informe a temperatura em ºC:'))

c = ((9 * g) / 5) + 32

print(f' A temperatura em ºC é {g:.1f}ºC e a temperatura convertida em ºF é {c:.1f}')
