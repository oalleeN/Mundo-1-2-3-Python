'''Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''

matriz = [[0, 0, 0] , [0, 0, 0] , [0, 0, 0]]                    # essas listas aqui!      
spar = mai = scol = 0  
                                    
for l in range(0, 3): # FOR para as "Linhas" (l)      OBS: Estes 2 "for's" são para adicionar os valores através da input nas lacunas da lista!
    for c in range(0, 3): #FOR para as "Colunas" (c)
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: ')) # Para cada linha haverá 3 colunas, então logo assim suprindo cada indice das "listas" acima! 

print('-=' * 20)

for l in range(0, 3):  # Estes 2 "for's" servem para mostrar na tela  resultado da matriz por completo e de forma mais organizada.
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]' , end=' ')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c] #vai fazer com o que ele some "spar" + "matriz[l][c]""
    
    print() # Serve para quebrar as colunas, ou seja, toda vez que ele preencher cada linha e coluna por vez, ele irá quebrar a linha.

print('-=' * 30)

print(f'A soma dos números pares da matriz é {spar}')

for l in range(0, 3): # como ele já tem os valores fixos da coluna (que é [2]) ele apenas vai fazer com que 
    scol += matriz[l][2] # passe todos os valores da linha 0, 1 e 2 e assim vai ver quais números fazem parte
print(f'A soma dos valores da coluna 3 é de {scol}')

print(f'O maior valor da 2ª linha é {max(matriz[1])}') 