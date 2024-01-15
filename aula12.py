nome = str(input('Digite seu nome: '))

if nome in 'Tobias':
    print(f'Seu nome é muito bonito, {nome}!')
elif nome in 'Marta' or nome == 'Tulio':
    print(f'Seu nome é diferente.')
elif nome in 'Lucas':
    print(f'Parabéns, é seu aniversário hoje!')
else:
    print('Que droga, seu nome é muito feio!')
print(f'Seja bem-vindo(a), {nome}!')
