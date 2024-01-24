def dobro(n = 0, format=False):
    resp = n * 2
    return resp if format is False else moeda(resp)

def metade(n = 0, format=False):
    resp = n / 2
    return resp if format is False else moeda(resp)

def aumentar(n = 0, a=0, format=False):
    resp = n + (n * a / 100)
    return resp if format is False else moeda(resp)

def diminuir(n = 0, d=0, format=False):
    resp =  n * d / 100
    return resp if format is False else moeda(resp)

def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace(".", ",")

def resumo(n=0, a=0, d=0):
    print('~' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('~' * 35)
    print(f'Preço analisado: \t{moeda(n)}') # \t é chamado de tabulação
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{a}% de aumento: \t{aumentar(n, a, True)}')
    print(f'{d}% de redução: \t{diminuir(n, a, True)}')
    print('~' * 35)