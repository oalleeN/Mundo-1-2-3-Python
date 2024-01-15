'''Faça um programa que tenha uma função chamada contador(), que receba 
três parãmetros: início, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada'''

from time import sleep
def texto(txt):
    print('-=' * 15)
    print(txt)

texto('Contagem de 1 até 10 de 1 em 1')    
for s in range(1, 10+1, 1):
    sleep(0.3)
    print(s, end = ' ')
    if s == 10:
        sleep(0.3)
        print('FIM')
        break

texto('Contagem de 10 até 0 de 2 em 2')
for s in range(10, -1, -2):
    sleep(0.3)
    print(s, end = ' ')
    if s <= 0:
        sleep(0.3)
        print('FIM')
        break
print()
texto('Contagem personalizada')
inicio = int(input('INÍCIO: '))
fim = int(input('FIM: '))
passos = int(input('PASSOS: '))
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -passos
        if inicio < fim:
            for c in range(inicio, fim + 1, passo):
                print(c, end=' ')
                if c == fim:
                    print('FIM')
                    break
        else:
            for c in range(inicio, fim - 1, passo):
                print(c, end=' ')
                if c == fim:
                    print('FIM')
                    break
    else:
        if inicio < fim:
            for c in range(inicio, fim + 1, passo):
                print(c, end=' ')
                if c == fim:
                    print('FIM')
                    break
        else:
            for c in range(inicio, fim - 1, passo):
                print(c, end=' ')
                if c == fim:
                    print('FIM')
                    break

contador(inicio, fim, passos)
