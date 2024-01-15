'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai 
parar quando o usuário digitar o valor 999, que é a condição de parada. No final, 
mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

núm = 0
soma = 0
cont = 0
núm = int(input('Digite um valor [999 para parar]: '))
while núm != 999:
    cont += 1
    soma += núm
    núm = int(input('Digite um valor [999 para parar]: '))
print(f'Você digitou {cont} números e a soma entre eles é de {soma}')

#----------------------------------------------------------------------
#duas formas, porém a mais recomendada é a primeira 

núm = cont = soma = 0
while núm != 999:
    núm = int(input('Digite um valor [999 para parar]: '))
    cont += 1
    soma += núm
print(f'Você digitou {cont - 1} números e a soma entre eles é de {soma - 999}')
