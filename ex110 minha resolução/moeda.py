
def resumo(n=0, a=0, d=0):
    print('~' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('~' * 35)
    print(f'Preço analisado: \tR${n:.2f}'.replace(".", ","))

    dobro = n * 2
    print(f'Dobro do preço: \tR${dobro:.2f}'.replace(".", ","))

    metade = n / 2
    print(f'Metade do preço: \tR${metade:.2f}'.replace(".", ","))

    aumentar = n + (n * a / 100)
    print(f'{a}% de aumento: \tR${aumentar:.2f}'.replace(".", ","))

    diminuir = n * d / 100
    print(f'{d}% de redução: \tR${diminuir:.2f}'.replace(".", ","))
    print('~' * 35)