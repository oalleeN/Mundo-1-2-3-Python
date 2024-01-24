'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador
e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha 
sido informado corretamente.'''

# Minha resolução não 100% completa:
def ficha(nome="<desconhecido>", gols=0):
    if nome == '':
        nome = "<desconhecido>"
        if gols == '': 
            gols = 0
            print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
        else:
            print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
    elif gols == '': 
        gols = 0
        print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
    else:
        print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

jogador = str(input('Nome do Jogador: '))
gols = str(input('Número de gols: '))

print(ficha(jogador, gols))

# Resolução do professor:
def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

jogador = str(input('Nome do jogador: '))
gol = str(input('Número de gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if jogador.strip() == '':
    ficha(gols=gol)
else:
    ficha(jogador, gol)
