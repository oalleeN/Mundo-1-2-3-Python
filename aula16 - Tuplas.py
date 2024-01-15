lanches = 'Hambuerguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'

#                                       tuplas são imutáveis!

print(lanches[-3])

#----------------------------------------------------------------------------------

for comida in lanches:
    print(f'Eu vou tomar {comida}' if comida == 'Suco' else f'Eu vou comer {comida}' )
print('comi demais!')

#----------------------------------------------------------------------------------

for cont in range(0, (len(lanches))):
    print(lanches[cont]) # Aqui ele contará em ordem de procedência!

#----------------------------------------------------------------------------------    
for pos, comida in enumerate(lanches):
    print(f'Eu vou comer {comida} na posição {pos}')

#----------------------------------------------------------------------------------    

print(sorted(lanches)) # Para mostrar os lanches ordenado! 

#----------------------------------------------------------------------------------

a = (1 ,5, 7)
b = (6, 7, 8)
c = a + b # Ele não vai somar, apenas acrescentar tudo em sua respectiva ordem!
print(c)

#----------------------------------------------------------------------------------

a = (1 ,5, 7)
b = (6, 7, 8)
c = a + b 
print(c.count(7)) #Irá contar quantas vezes aparece o número "7" ou qualquer outro.

#----------------------------------------------------------------------------------

a = (1, 8, 9)
b = (2, 3, 7)
c = b + a
print(c)
print(c.index(8)) # Isso quer dizer em que posição está o número "8", neste caso, na posição 4

#----------------------------------------------------------------------------------
