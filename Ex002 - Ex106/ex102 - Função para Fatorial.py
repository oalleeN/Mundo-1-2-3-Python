'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que 
indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''

# Minha resolução
def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um númereo.
    :param m: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    if show==False:
        for c in range(n, 0, -1):
            f *= c
        return f
    else:
        for c in range(n, 0, -1):
            if c > 1:
                print(f'{c} x', end=' ')
            f *= c
        return f'{c} = {f}'

print(fatorial(5, show=True))
help(fatorial)


# Resolução do professor:
def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um númereo.
    :param m: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print(' x ', end=' ')
            else:
                print(' = ', end=' ')
        f *= c
    return f

#Programa principal
print(fatorial(5, show=True))
help(fatorial)
