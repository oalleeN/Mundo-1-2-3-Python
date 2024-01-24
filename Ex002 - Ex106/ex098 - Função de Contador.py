'''Faça um programa que tenha uma função chamada contador(), que receba 
três parãmetros: início, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada'''

from time import sleep
def contador(inicio, fim, passo):
    if passo < 0: 
        passo *= -1 # serve para tirar o sinal de negatio do número
    if passo == 0:
        passo = 1
    print('-=' * 20)
    print(f'A contagem de {inicio} até {fim} de {passo} em {passo}.')
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            sleep(0.3)
            print(cont, end=' ')
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            sleep(0.3)
            print(cont, end=' ')
            cont -= passo # para a quantidade de passos subitrair a quantidade de inicial
        print('FIM!')
        
#Programa principal
contador(1, 10, 1)
contador(10, 0, 2)

print('-=' * 15)
print('Agora é sua vez de personalizar a contagem')
i = int(input('INICIO: '))
f = int(input('FIM:    '))
p = int(input('PASSO:  '))
contador(i, f, p)

'''OBS: Para quem quiser transformar negativos em positivos também dá pra fazer com a função "abs":
passo = abs(passo) 
Também dá pra declarar: "i = inicio" fora do if/else, economiza uma linha'''