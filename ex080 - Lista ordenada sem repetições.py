lista = []
for c in range(0, 5): # VAI FAZER COM O QUE O "input" SE REPITA 5 VEZES
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]: #ELE VAI DÁ UM ".append"(ADICIONAR) SE ELE FOR O PRIMEIRO NÚMERO
        lista.append(n)         # OU SE "n" FOR MAIOR QUE O ÚLTIMO NÚMERO TAMBÉM.
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=-' * 30)
print(f'Os valores digitados em ordem foram {lista}')
