c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')

n = 1
while n != 0: #enquanto os valores digitados forem diferentes de 0, o programa continua rodando.
    n = int(input('Digite um valor: '))
print('FIM')

r = 'S'
while r == 'S': #enquanto a resposta for "S" o programa continua rodando.
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar [S,N]')).upper()
print('FIM')

n = 1 
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números impares')


