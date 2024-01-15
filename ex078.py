valores = list()
for v in range(0, 5):
    valores.append(int(input('Digite um número: ')))
print(valores)
print(f'O maior número digitado foi {max(valores)} e o menor valor digitado foi {min(valores)}')
for a, c in enumerate(valores):
    print(f'Na posição {a} encontrei o valor {c}!')

