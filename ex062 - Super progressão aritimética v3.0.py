'''Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão da PA: '))
termo = primeiro 
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Digite quantos termos a mais você quer mostrar: '))
print('FIM')
