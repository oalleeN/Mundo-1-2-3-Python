'''Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação 
de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''
def leiaInt(a):
    while True:
        try:
            i = int(input(a))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro.\033[m')
        except (KeyboardInterrupt):
            print('\n\033[31mO usuário interrompeu o programa!\033[m')
            return 0
        else:
            return i
def leiaFloat(a= 0):
    while True:
        try:
            f = float(input(a))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número real.\033[m')
        except (KeyboardInterrupt):
            print('\n\033[31mO usuário interrompeu o programa!\033[m ')
            return 0
        else:
            return f
        
i = leiaInt('Digite um número inteiro: ')
f = leiaFloat('Digite um número real: ')
print(f'O resultado inteiro digitado foi {i} e o real digitado foi {f}')
