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
        
def linha(tam = 42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(f'{txt}'.center(42))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[34m{c}\033[m - \033[33m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc
