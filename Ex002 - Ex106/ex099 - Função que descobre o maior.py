''' Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com 
valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior'''

def maior(* núm): # "*" = desempacotar/vai usar vários valores que ainda não sabemos
    contador = maior = 0
    print('-=' * 20)
    print('Analisando os valores descritos...')
    for valor in núm:
        print(f'{valor}', end=' ')
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1
    print(f'Foram informados {contador} valores ao todo.')
    print(f'O maior valor informado é {maior}')

maior(2, 9, 4 ,5 ,1)
maior(7, 8, 3, 0)
maior(1, 10)
maior(6)
maior()
