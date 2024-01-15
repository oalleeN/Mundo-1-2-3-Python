# RESOLUÇÃO FEITA POR MIM:

import datetime
from datetime import date # classe date
current_date = date.today()
dados = {
    'nome': str(input('Nome: ')),
    'idade': int(input('Ano de nascimento: ')),
    'ctps': int(input('Carteira de trabalho (0 não tem): ')),
    'contratação': int(input('Ano de contratação: ')),
    'salário': float(input('Salário: R$'))
}
print('===' * 20)
data_actual = current_date.year
dados['idade'] = data_actual - dados['idade']

print(dados)
if dados['ctps'] <= 0:
    print(f'nome tem o valor {dados["nome"]}')
    print(f'idade tem o valor {dados["idade"]}' )
    print(f'ctps tem o valor {dados["ctps"]}')
else:
    for k, i in dados.items():
        print(f'{k} tem o valor {i}')

dados['contratação'] = data_actual - dados['contratação']
dados['contratação'] = (35 - dados['contratação']) + dados['idade']
print(f'aposentadoria tem o valor {dados["contratação"]}')

# AGORA IREI MOSTRAR A RESOLUÇÃO DO PROFESSOR:

from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')
