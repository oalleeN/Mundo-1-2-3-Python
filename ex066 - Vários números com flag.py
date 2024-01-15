'''Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, 
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''

num = soma = quant = 0
while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    soma += num
    quant += 1
print(f' A soma dos números é de {soma} e a quantidade é de {quant}')
