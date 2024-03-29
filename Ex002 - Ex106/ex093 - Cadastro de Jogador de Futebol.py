''' Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols 
feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

aproveitamento = dict()
aproveitamento['nome'] = str(input('Nome do jogador: '))
part = int(input('Partidas jogadas: '))
qg = list()
for g in range(part):
    gol = int(input(f'Quantos gols na partida {g+1}: '))
    qg.append(gol)

aproveitamento['gols'] = qg

soma = sum(qg)
aproveitamento['total'] = soma

print('-=' *30)
print(aproveitamento)

print('-=' *30)
for key, val in aproveitamento.items():
    print(f'O campo {key} tem o valor {val}')

print('-=' *30)
print(f'O jogador {aproveitamento["nome"]} jogou {part} partidas')
for key, val in enumerate(qg):
    print(f' ==>  Na partida {key+1}, fez {val} gols.')
print(f'Foi um total de {aproveitamento["total"]} gols.')
