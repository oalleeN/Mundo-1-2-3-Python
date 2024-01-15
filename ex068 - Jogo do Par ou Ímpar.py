''' Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
v = 0

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0,10)
    tipo = ' '
    total = jogador + computador

    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]: ')).upper().strip()[0]

    print(f'Você jogou {jogador} e o computador {computador}. O total foi de {total}', end=' ')
    print(f'e deu Par' if total % 2 == 0 else 'e deu Ímpar')

    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            ('Você perdeu!')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break

    print('Jogue novamente!')   
print(f'GAMER OVER!!! Você venceu {v} vezes' if v > 1 else 'GAMER OVER!!! Você não venceu nenhuma vez' )