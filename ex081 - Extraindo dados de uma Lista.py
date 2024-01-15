''' Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

valores = []
while True:
    valores.append(int(input('Digite um número: ')))
    p = str(input('Deseja continuar [S/N]: '))
    if p in 'Nn':
        break
print('-=' * 30)
print(f'{len(valores)} números foram digitados!')
valores.sort(reverse=True)
print(f'Os números ordenados em forma decrescente são: {valores}')
if 5 not in valores:
    print('O valor 5 não foi digitado e não se encontra na lista!')
else:
    print(f'O valor 5 foi digitado e se encontra na lista!')
