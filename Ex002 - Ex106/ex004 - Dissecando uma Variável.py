''' Faça um programa que leia algo pelo teclado e mostre na tela o seu 
tipo primitivo e todas as informações possíveis sobre ele.'''
a = input('digite algo:')
print(f'é do tipo primitivo: {type(a)}')
print(f'só tem letras maiúsculas? {a.isupper()}')
print(f'só tem letras minúsculas? {a.islower()}')
print(f'é numérico? {a.isnumeric()}')
print(f'é alfabético? {a.isalpha()}')
print(f'ela está capitalizada? {a.istitle()}')
print(f'ele é alfanumérico? {a.isalnum()}')
print(f'tem somente espaços? {a.isspace()}')
