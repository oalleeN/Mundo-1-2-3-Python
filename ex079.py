valores = list()
while True:
    n = int(input('Digite um valor: '))

    if n not in valores:
        valores.append(n)
    else:
        print('Valor duplicado! Não vou adicionar.')

    r = str(input('Deseja continuar? [S/N] '))

    if r in 'Nn':
        break
valores.sort()
print(valores)