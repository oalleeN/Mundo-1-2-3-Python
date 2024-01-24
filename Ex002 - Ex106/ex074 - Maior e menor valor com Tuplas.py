'''CRIE UM PROGRAMA QUE VAI GERAR 5 NÚMEROS ALEATÓRIOS E COLOCAR EM UMA TUPLA
DEPOIS DISSO, MOSTRE A LISTAGEM DE NÚMEROS GERADOS E TAMBÉM INDIQUE O MENOR E 
O MAIOR VALOR QUE ESTÃO NA TUPLA.'''

from random import sample
list_num = tuple(sorted(sample(range(0, 11),4))) #USEI O MÉTODO "SORTED" (ORDERNAR) PARA QUE NÃO 
print(list_num)                                   #REPETISSEM OS NÚMEROS SORTEADOS PELO "SAMPLE"
print(f'o maior número é {max(list_num)} e o menor é {min(list_num)}')
