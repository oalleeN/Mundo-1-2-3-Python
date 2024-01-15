#PARA DECLARAR UMA VARIÁVEL EM DICIONÁRIOS PODEMOS UTILIZAR DESSES MODOS:
dados = dict()
# OU
dados = {'nome':'Alan', 'idade':'19'}
print(dados['nome'])
print(dados['idade'])

#NESTA SEGUNDA FORMA GERALMENTE É USADA QUANDO VOCê JÁ TEM OS VALORES QUE VOCÊ PRECISA

#-------------------------------------------------------------------------------------

#PARA ADICIONAR UM ELEMENTO:

dados['sexo'] = 'm'

#PARA REMOVER UM ELEMENTO:

del dados['idade']

#PARA DECLARAR UMA VARIÁVEL SEPERANDO "CHAVES" POR LINHA:

filme = {'titulo':'Star Wars',
         'ano':1977,
         'diretor':'George Lucas'
        }

#DESTRINCHANDO OS ELEMENTOS DA VARIÁVEL "Filme":

# 1 - OS VALORES SÃO: 'Star Wars', 1977, 'George Lucas'
#PARA OBERSERVAR ESSES VALORES VOCÊ DEVE DIGITAR DA SEGUINTE FORMA:

print(filme.values())

# 2 - AS CHAVES SÃO: 'titulo', 'ano', 'diretor'
#PARA OBSERVAR AS CHAVES VOCÊ DEVE DIGITAR DA SEGUINTE FORMA::

print(filme.keys())

# 3 - OS ITENS SERIAM TODOS OS VALORES E CHAVES CONTIDAS EM TAL VARIÁVEL, COMO NESSE CASO A VARIÁVEL "Filme"
#PARA OBSERVAR OS ITENS VOCÊ DEVE DIGITAR DA SEGUINTE FORMA:

print(filme.items())

#----------------------------------------------------------------------------------------------------------

#PARA UTILIZAR OS .values, .keys ou .items EM LAÇOS DE REPETIÇÕES, POR EXEMPLO EM "for":

for k, v in filme.items():
    print(f'O {k} é {v}')

#COMO O "".items" TEM TODOS O ELEMENTOS CONTIDOS NA VARIÁVEL, ELE PASSA O LAÇO POR CHAVES (k) E VALORES (v)

#----------------------------------------------------------------------------------------------------------

pessoas = {'nome': 'Gustavo', 
           'sexo': 'Masculino', 
           'idade': 19
           }

#CASO EU QUEIRA MUDAR O "nome", PODEMOS FAZER DE TAL FORMA:
pessoas['nome'] = 'Alan'

print(f'O {pessoas["nome"]} é do sexo {pessoas["sexo"]} e tem {pessoas["idade"]} anos de idade.')
#TIVE QUE USAR ASPAS DUPLAS NA HORA DE "referênciar" PORQUE EU JÁ ESTAVA USANDO ASPAS SIMPLES


for k in pessoas.keys(): # PARA CADA "CHAVE", ELE VAI DAR UM "print" ATÉ CHEGAR AO FIM DO LAÇO
    print(k)

for v in pessoas.values(): # PARA CADA "VALOR", ELE VAI DAR UM "print" ATÉ CHEGAR AO FIM DO LAÇO
    print(v)

for k, v in pessoas.items(): # COMO O ".items" TEM TODOS O ELEMENTOS CONTIDOS NA VARIÁVEL, ELE PASSA O LAÇO POR CHAVES (k) E VALORES (v) ATÉ CHEGAR AO FIM DO LAÇO
    print(f'{k} = {v}')

#------------------------------------------------------------------------------------------------------
#PODEMOS UTILIZAR TUPLAS, LISTAS E DICIONÁRIOS NO MESMO PROGRAMA!

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil) 
print(brasil[0]['uf'])
print(brasil[1]['sigla']) 

#-----------------------------------------------------
# AQUI NESTA PARTE VAI SER MOSTRADO COMO ADICIONA UM "Dicionário" À UMA "Lista" ATRÁVES DO "input"

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
# PARA MOSTRAR DE FORMA ORDENADA
for e in brasil: # PARA CADA ESTADO (e) em BRASIL
    for v in e.values():
        print(v, end=' ')
    print()