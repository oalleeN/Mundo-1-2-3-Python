p1t = int(input('Primeiro termo: '))
razao = int(input('Razão '))
décimo = p1t + (10 - 1) * razao
for c in range(p1t, décimo + razao, razao):
    print(f'{c}', end='-> ')
print('ACABOU!')




