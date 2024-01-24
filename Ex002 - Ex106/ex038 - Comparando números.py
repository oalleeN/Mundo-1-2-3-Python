''' Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro: '))

if num1 > num2 or num2 > num1:
    if num1 >= num2:
        print(f'O maior número é o {num1}' )
    elif num2 >= num1:
        print(f'O maior número é o {num2}')

if num1 < num2 or num2 < num1:
    if num1 <= num2:
        print(f'O menor número é o {num1}')
    elif num2 <= num1:
        print(f'O menor número é o {num2}')

if num1 == num2 or num2 == num1:
    if num1 == num2:
        print('Os números são iguais!')
    elif num2 == num1:
        print('Os números são iguais!')