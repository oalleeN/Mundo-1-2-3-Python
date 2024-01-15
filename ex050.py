s = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        s += num
        cont += 1
print(f'Você informou {cont} números PARES e a soma dos mesmos foi de {s}')


