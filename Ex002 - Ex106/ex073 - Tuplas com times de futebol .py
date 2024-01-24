'''CRIE UMA TUPLA PREENCHIDA COM OS 20  PRIMEIROS COLOCADOS DA TABELA DO CAMPEONATO BRASILEIRO DE FUTEBOL
NA ORDEM DE COLOCAÇÃO. DEPOIS MOSTRE: 
a) Os 5 primeiros
b) Os últimos 4 colocados
c) Times em ordem alfabética
d) Em que posição está o Vasco'''

times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Atlético-MG', 'São Paulo',
'Fluminense', 'Grêmio', 'Fortaleza', 'Athletico-PR', 'Cruzeiro','' 'Inter',
'Red Bull Bragantino', 'Santos', 'Bahia', 'Corinthians', 'Cuiabá', 'Goiás',
'América-MG', 'Vasco', 'Coritiba')

print(f'Os 5 primeiros colocados {times[:5]}')
print(f'Os últimos 4 colocados são: {times[-4:]}')
print(f'Os times em ordem alfabética {sorted(times)}')
print(f'O Vasco está {times.index("Vasco") +1 }ª posição')
