''' Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.'''
n = int(input('digite um valor: '))

d = n * 2
t = n * 3
r = n ** (1/2)

print(f' o dobro deste valor é: {d} \n o triplo deste valor é: {t} \n a raiz quadrada deste valor é: {r:.2f}')
