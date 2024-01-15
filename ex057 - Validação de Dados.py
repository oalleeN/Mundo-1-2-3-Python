'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

M = 'M'
F = 'F'
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo: Masc [M] / Femi [F] \nDigite aqui: ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Inválido! Digite novamente!')
if sexo == "M":
    print('Obrigado!')
else:
    print('Obrigado!')  
