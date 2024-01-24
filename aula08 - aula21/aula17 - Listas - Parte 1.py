lista = ['casa', 'carro', 'montanha', 'xadrez']
lista.append('pão') # para adicionar um objeto ao fim da lista
lista.insert(1, 'moto') # para adicionar um objeto na lista sem que remova outro
lista.pop(2) # para deletar um objeto na lista
lista.remove('casa') # para remover um obejto utilizando seu "nome"
lista.sort(reverse=True) # ordenar obejtos na ordem reversa (4,3,2,1)
lista.sort() # ordenar objetos (1,2,3,4)
print(f' Quantos objetos restaram a lista: {len(lista)}')
print(lista)
#--------------------------------------------------------
valores = []
valores.append(9)
valores.append(6)
valores.append(3)

for c, v in enumerate(valores):
    print(f'na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista!')
#--------------------------------------------------------
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista!')