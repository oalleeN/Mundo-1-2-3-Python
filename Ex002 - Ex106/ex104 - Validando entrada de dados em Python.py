'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 
'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')'''

# Minha resolução:
def leiaInt(a):
    while a != int:
        n = input(a)
        if n.isnumeric():
            n = int(n)
            break
        else:
            print('ERRO! digite apenas valores inteiros')
    return n

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')


# Resolução do professor:
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! Digite apenas valores inteiros.')
        if ok:
            break
    return valor

#Programa principal:
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
