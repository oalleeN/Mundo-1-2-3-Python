'''Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''

num = int(input('Escolha um número para receber a tabuada: '))
print('-=-' * 10)
for c in range(1, 10):
    print(f' {num} x {c} = {num*c}')
print('-=-' * 10)
print('FIM')
