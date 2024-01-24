'''from cadastro import cadastrar
from cadastro import opcao

while True:
    print('~' * 35)
    print(f'MENU PRINCIPAL'.center(35))
    print('~' * 35)

    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do sistema')

    print('~' * 35)
    opc = opcao.leia_opcao('Sua opção: ')
    print('~' * 35)


    if opc == 1:
        print('Opção 1'.center(35))
        print('~' * 35)
        continue
    elif opc == 2:
        print('Opção 2'.center(35))
        print('~' * 35)
        n = cadastrar.cadastro_nome('Nome: ')
        i = cadastrar.cadastro_idade('Idade: ')
        continue
    elif opc == 3:
        print('~' * 35)
        print('Saindo do sistema...'.center(35))
        print('~' * 35)
        break'''

from cadastro.interfacee import*
from time import sleep
from cadastro.arquivo import*

arq = 'arquivo.txt'

if not arquivo_existe(arq):
    criar_arquivo(arq)

while True:
    resposta = menu(['Listar todos os nomes', 'Cadastrar uma pessoa', 'Sair do sistema']) # resposta vai receber e rodar a funação inteira
    if resposta == 1:
        # Opção listar o conteúdo de um arquivo
        ler_arquivo(arq)
    elif resposta == 2:
        # Opção para cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Opção 3')
        break
    else: 
        print('\033[31mERRO! Digite uma opção válida\033[m')
    sleep(2)