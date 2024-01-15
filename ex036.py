casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o seu salário: R$'))
anos = int(input('Digite em quantos anos você irá quitar sua conta: '))
meses = anos * 12
prestação = casa / meses
minimo = salario * 30 / 100
print(f'{prestação:.2f} - {minimo:.2f}')
if prestação <= minimo:
    print(f'Empréstimo CONCEDIDO! {prestação:.2f}')
else:
    print(f'Empréstimo NEGADO! {prestação:.2f}')
