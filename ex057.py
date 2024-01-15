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


    
