#Resolução professor: 

def dobro(n = 0, format=False):
    resp = n * 2
    return resp if format is False else moeda(resp)

def metade(n = 0, format=False):
    resp = n / 2
    return resp if format is False else moeda(resp)

def aumentar(n = 0, a=0, format=False):
    resp = n + (n * a / 100)
    return resp if format is False else moeda(resp)

def diminuir(n = 0, a=0, format=False):
    resp =  n * a / 100
    return resp if format is False else moeda(resp)

def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace(".", ",")