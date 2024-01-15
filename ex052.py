num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print(f'\033[33m', end=' ')
        total += 1
    else:
        print(f'\033[031m', end=' ')
    print(f'{c}', end='')
print(f'\n \033[mO número {num} foi divido {total} vezes.')

if total == 2:
    print(' ESSE NÚMERO É PRIMO')
else:
    print(' ESSE NÚMERO NÃO É PRIMO')
