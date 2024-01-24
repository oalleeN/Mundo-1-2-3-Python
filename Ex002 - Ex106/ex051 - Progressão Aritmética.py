'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressão.'''

p1t = int(input('Primeiro termo: '))
razao = int(input('Razão '))
décimo = p1t + (10 - 1) * razao
for c in range(p1t, décimo + razao, razao):
    print(f'{c}', end='-> ')
print('ACABOU!')
