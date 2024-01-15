maior = 0
menor = 0
for c in range(1 , 5+1):
    peso = float(input(f'Qual o peso da {c} pessoa em KG: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
        
print(f'O maior peso é {maior} e o menor peso é {menor}')