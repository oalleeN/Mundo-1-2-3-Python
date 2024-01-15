from datetime import date
nome = str(input('Digite seu nome completo: '))
ano_de_nasci = int(input('Digite sua data de nascimento: '))

print('-=-' * 10)

ano_atual = date.today().year
ano_de_alist = ano_atual - ano_de_nasci

print(f'Você tem {ano_de_alist} anos SOLDADO!')

print('-=-' * 10)

if ano_de_alist < 18:
    tempo_rest = 18 - ano_de_alist
    print(f'VOCÊ AINDA É MUITO JOVEM, SOLDADO! TENTE DAQUI {tempo_rest} ano(s)') 
    ano = ano_atual + tempo_rest
    print(f'Seu alistamento será no ano de {ano}')
elif ano_de_alist == 18:
    print('Está na hora de você se alistar, SOLDADO!')

elif ano_de_alist > 18:
    tempo_passou = ano_de_alist - 18
    print(f'Você passou {tempo_passou} ano(s) da data de alistamento, procure o local mais próximo de você para efetuar o alistamento!')
    ano = ano_atual - tempo_passou
    print(f'Você deveria ter se alistado em {ano}')
print('-=-' * 10)














'''nome = str(input('Digite seu nome: '))
print(f'Seja bem-vindo(a), {nome}!')

data = int(input('Digite sua data de nascimento: '))

a1 = 2005  

if data == a1:
    print('Está na hora de você se alistar!')
elif data <= a1:
    passou = a1 - data
    print(f'Você passou {passou} dias do prazo! VÁ PARA O QUARTEL MAIS PRÓXIMO.')
elif data >= a1:
    print('Você ainda não tem idade o suficiente')
else:
    print('')'''


