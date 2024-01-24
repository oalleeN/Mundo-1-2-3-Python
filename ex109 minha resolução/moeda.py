# Minha resposta

def dobro(n = 0, ret=False):
    if ret==True:
        return moeda(n * 2)
    else:
        return n * 2

def metade(n = 0, ret=False):
    if ret:
        return moeda(n / 2) 
    else:
        return n / 2

def aumentar(n = 0, a=0, ret=False):
    if ret:
        return moeda(n + (n * a / 100))
    else:
        return n + (n * a / 100)

def diminuir(n = 0, a=0, ret=False):
    if ret:
        return moeda(n * a / 100)
    else:
        return n * a / 100

def moeda(n=0, moeda='R$'):
        return f'{moeda}{n:.2f}'.replace(".", ",")