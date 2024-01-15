'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''

total = mais_dmil = cheaper = 0
cheaper_name = ''
while True:
    nome = str(input('Nome do produto: '))
    valor = float(input('Valor: R$'))
    cadastro = str(input('Deseja continuar? [S / N]: ')).strip().upper()[0]
    print('===' * 20)
    total += valor
    if cadastro == 'S':
        if valor > 1000:
            mais_dmil += 1
        if cheaper == 0:
            cheaper = valor
            cheaper_name = nome
        elif valor < cheaper:
            cheaper = valor
            cheaper_name = nome
    else:
        if cadastro == 'N':
            print(f'Total da compra: {total:.2f}')
            print(f'Produtos que custam mais de R$1000: {mais_dmil}')
            print(f'Produto mais barato: {cheaper_name}')
            break

# forma que eu encontrei no GitHub

cheaper_name = ""
somador = higher = cheaper = 0

while True:
    name = str(input("Nome do produto: \n"))
    price = float(input("Preço: \n"))
    
    somador += price

    if price > 1000:
        higher += 1
    
    if cheaper == 0:
        cheaper = price
        cheaper_name = name
    elif price < cheaper:
        cheaper = price
        cheaper_name = name

    choice = str(input("Inserir mais produtos? [S / N] \n")).strip().upper()
    
    if choice == "N":
        print(f"Total gasto: R${somador:.2f}")
        print(f"Produtos que custam mais do que R$1.000: {higher}")
        print(f"O produto mais barato é {cheaper_name}, que custa R${cheaper:.2f}")
        break
