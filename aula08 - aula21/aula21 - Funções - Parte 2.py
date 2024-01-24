# Interactive Help
def contador(i, f, p):
    c = i
    while c <= f:
        print(f'{c}' , end=' ')
        c = c + p
    print('FIM')

help(contador)

# Docstrings + Interactive Help
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: final da contagem
    :param p: passo da contage,
    :return: sem retorno
    Feito por Alan
    """
    c = i
    while c <= f:
        print(f'{c}' , end=' ')
        c = c + p
    print('FIM')

help(contador)


# Parâmetros Opcionais + Docstrings
def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    Função criada por Alan
    """
    s = a + b + c
    print(f'A soma vale {s}')

somar(2, 4)
#ou
somar(b=2, c=5) # pode informar o valor fora do padrão também, vai do jeito que você preferir

# Escopo de Varáveis
def teste():
    x = 8 # variável local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

# Programa principal
n = 2 # variável global
print(f'No programa principal, n vale {n}')
teste()


# Escopo Local e Global
def test(b):
    a = 4
    b += 6
    c = 3
    print(f'A variável local "a" vale {a}')
    print(f'A variável local "b" vale {b}') # vai ser a soma da variável "a" global mais a variável "b" local
    print(f'A variável local "c" vale {c}')

# Programa principal
a = 2
test(a)
print(f'A variável global "a" vale {a}')


# Usando a função GLOBAL
def testing(b):
    global a # fazendo com que a VL (Variável Local) "a" seja o valor Global do código
    a = 8
    b += 4
    c = 2
    print(f'A variável local "a" vale {a}')
    print(f'A variável local "b" vale {b}')
    print(f'A variável local "c" vale {c}')

# Programa principal
a = 5 # como a VL "a" recebeu a função "global a" ela vai se tornar o valor "a" Global do código e essa variável não terá VG
testing(a)
print(f'A variável global vale {a}')

# Retornando valores "return"
def soma(a=0, b=0, c=0):
    s = a + b + c
    return s 

# Programa princial
r1 = soma(1, 4, 5)
r2 = soma(2, 6)
r3 = soma(6)
print(f'Meus cálculos deram {r1}, {r2} e {r3}') 


# PRÁTICA PROPOSTA: 
# Cálcular o fatorial de um número e retornar ele para o meu programa principal

def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

# Programa principal
n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

#outro modo

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f'Os resultados são {f1}, {f2} e {f3}')

# Mais um prática proposta:

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    
num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
