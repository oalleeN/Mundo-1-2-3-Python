nome = str(input('Digite seu nome: '))
if nome == 'Jonas':
    print('Então você é o Jonas...!')
else:
    print('Seu nome é uma merda! Porém...')
print(f'Seja bem-vindo(a), {nome}!')

#-------------------------------------------------
nota1 = float(input('Digite sua nota do 1º bimestre: '))
nota2 = float(input('Digite sua nota do 2º bimestre: '))

resultado = (nota1 + nota2) / 2
print(f'Sua média é {resultado:.1f}')

if resultado >=6:
    print('Parabéns, você passou de ano!')
else:
    print('Ops... Estude mais no ano que vem!')
