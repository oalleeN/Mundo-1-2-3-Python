'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.'''
nome = str(input('Digite seu nome: ')).strip()

resposta = 'SILVA' in nome.upper()

print(f'Se seu nome contém "Silva": ')
print(f'OBS: Para verdadeiro "True" e para falso "False"!')
print(resposta)
