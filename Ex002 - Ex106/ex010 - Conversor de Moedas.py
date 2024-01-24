''' Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos 
dólares ela pode comprar.'''
d = float(input('Digite quanto de saldo há em sua conta: '))

dc = d/5.22  # dc = dólar(s) comprado(s)

print(f' considerando o valor atual de R${d} que você possui, você poderá comprar apenas US${dc:.2f} ')

# considerei a cotação atual (15/02/2023) do dólar de 5,22 reais!
