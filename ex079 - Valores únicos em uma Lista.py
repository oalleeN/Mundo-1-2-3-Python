'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, 
ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. '''

valores = list()
while True:
    n = int(input('Digite um valor: '))

    if n not in valores:
        valores.append(n)
    else:
        print('Valor duplicado! Não vou adicionar.')

    r = str(input('Deseja continuar? [S/N] '))

    if r in 'Nn':
        break
valores.sort()
print(valores)
