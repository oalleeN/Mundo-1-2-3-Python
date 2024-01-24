def dobro(n = 0):
    return n * 2

def metade(n = 0):
    return n / 2

def aumentar(n = 0, a=0):
    return n + (n * a / 100)

def diminuir(n = 0, a=0):
    return n * a / 100

def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace(".", ",")