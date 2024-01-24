''' Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda 
vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date
nome = str(input('Digite seu nome completo: '))
ano_de_nasci = int(input('Digite sua data de nascimento: '))

print('-=-' * 10)

ano_atual = date.today().year
ano_de_alist = ano_atual - ano_de_nasci

print(f'Você tem {ano_de_alist} anos SOLDADO!')

print('-=-' * 10)

if ano_de_alist < 18:
    tempo_rest = 18 - ano_de_alist
    print(f'VOCÊ AINDA É MUITO JOVEM, SOLDADO! TENTE DAQUI {tempo_rest} ano(s)') 
    ano = ano_atual + tempo_rest
    print(f'Seu alistamento será no ano de {ano}')
elif ano_de_alist == 18:
    print('Está na hora de você se alistar, SOLDADO!')

elif ano_de_alist > 18:
    tempo_passou = ano_de_alist - 18
    print(f'Você passou {tempo_passou} ano(s) da data de alistamento, procure o local mais próximo de você para efetuar o alistamento!')
    ano = ano_atual - tempo_passou
    print(f'Você deveria ter se alistado em {ano}')
print('-=-' * 10)
