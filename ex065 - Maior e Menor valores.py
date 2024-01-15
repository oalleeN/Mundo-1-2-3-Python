resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
         maior = menor = núm
    else:
        if núm > maior:
             maior = núm
        if núm < menor:
             menor = núm
    resp = str(input('Você quer continuar? [S/N]: ')).upper().strip()[0]
média = soma / quant
print(f'A soma dos números foi de {soma}, a quantidade de números é {quant} e a média é de {média:2f}')
print(f'O maior número é {maior} e o menor número é {menor}')