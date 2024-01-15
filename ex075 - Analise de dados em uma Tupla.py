valor = (int(input('Digite um valor: ')),
         int(input('Digite mais um valor: ')),
         int(input('Digite novamente mais um valor: ')),
         int(input('Digite somente mais um valor: ')))
print(valor)
print(f'O valor 9 aparece {valor.count(9)} vez(es)')
if 3 in valor:
    print(f'Valor 3 aparece na {valor.index(3) + 1}ª posição')
else:
    print('O valor 3 não aparece no comando proposto!')
print(f'Os valores pares digitados foram ', end='')
for n in valor:
    if n % 2 == 0:
        print(n, end=' ')
