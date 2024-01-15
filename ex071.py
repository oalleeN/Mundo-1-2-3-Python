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
