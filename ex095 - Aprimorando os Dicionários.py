''' Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''
time = list()
aproveitamento = dict()
qg = list()

while True:
    aproveitamento.clear()
    aproveitamento['nome'] = str(input('Nome do jogador: '))
    part = int(input('Partidas jogadas: '))
    qg.clear()
    for g in range(part):
        gol = int(input(f'Quantos gols na partida {g+1}: '))
        qg.append(gol)
    aproveitamento['gols'] = qg[:]
    aproveitamento['total'] = sum(qg)
    time.append(aproveitamento.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if resp == 'N':
        break
print('-=' *30)
print('cod ', end='')
for i in aproveitamento.keys():
    print(f'{i:<15}', end='')
print()
print('-=' *30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' *30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'EROO! Não existe jogador com código {busca}!')
    else:
        print(f' --- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f' No jogo {i+1} fez {g} gols.')
    print('-' *40)
print('--- VOLTE SEMPRE ---')
