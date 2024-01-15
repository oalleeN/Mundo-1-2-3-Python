# A MINHA RESOLUÇÃO:

linha1 = [[],[],[]]
linha2 = [[],[],[]]
linha3 = [[],[],[]]
for a in range(0,3):
    linha012 = int(input(f'Digite um valor para {[0, a]}: '))
    linha1[0].append(linha012)
    linha1[1].append(linha012)
    linha1[2].append(linha012)
for b in range(0, 3):
    linha102 = int(input(f'Digite um valor para {[1, b]}: '))
    linha2[0].append(linha102)
    linha2[1].append(linha102)
    linha2[2].append(linha102)
for c in range(0, 3):
    linha210 = int(input(f'Digite um valor para {[2, c]}: '))
    linha3[0].append(linha210)
    linha3[1].append(linha210)
    linha3[2].append(linha210)

print(f'[ {linha1[0][0]} ]' ,end=' ')
print(f'[ {linha1[1][1]} ]' ,end=' ')
print(f'[ {linha1[2][2]} ]')
print(f'[ {linha2[0][0]} ]' ,end=' ')
print(f'[ {linha2[1][1]} ]' ,end=' ')
print(f'[ {linha2[2][2]} ]')
print(f'[ {linha3[0][0]} ]' ,end=' ')
print(f'[ {linha3[1][1]} ]' ,end=' ')
print(f'[ {linha3[2][2]} ]')

# RESOLUÇÃO FEITA PELO PROFESSOR:

matriz = [[0, 0, 0] , [0, 0, 0] , [0, 0, 0]]                                                          # essas listas aqui!
for l in range(0, 3): # FOR para as "Linhas" (l)      OBS: Estes 2 "for's" são para adicionar os valores através da input nas lacunas da lista!
    for c in range(0, 3): #FOR para as "Colunas" (c)
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: ')) # Para cada linha haverá 3 colunas, então logo assim suprindo cada indice das "listas" acima! 
print('-=' * 20)
for l in range(0, 3):  # Estes 2 "for's" servem para mostrar na tela  resultado da matriz por completo e de forma mais organizada.
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]' , end=' ')
    print() # Serve para quebrar as colunas, ou seja, toda vez que ele preencher cada linha e coluna por vez, ele irá quebrar a linha.