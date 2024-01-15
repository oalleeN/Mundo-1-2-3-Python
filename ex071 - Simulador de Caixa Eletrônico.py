'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('--' * 15,'CAIXA ELETRÔNICO','--' * 15)   
finalizar = ''
saque = int(input('Qual valor você deseja sacar?: R$'))
total = saque
soma50 = 50 
totalsoma = 0
while True:
    if total >= soma50:
        total -= soma50
        totalsoma += 1
    else:
        if totalsoma > 0:
            print(f'Você recebeu {totalsoma} cédulas de {soma50}')
        if soma50 == 50:
            soma50 = 20
        elif soma50 == 20:
            soma50 = 10
        elif soma50 == 10:
            soma50 = 1
        totalsoma = 0
        if total == 0:
            break
