from cadastro.interfacee import*
def arquivo_existe(nome): #Verifica se o arquivo existe!
    try: 
        a = open(nome, 'rt') # "rt" = leitura e texto
        a.close() # para poder abrir e fechar o arquivo
    except FileNotFoundError:
        return False
    else:
        return True

def criar_arquivo(nome): # Cria o arquivo!
    try: 
        a = open(nome, 'wt+') # Escreve um arquivo de texto, caso não exista um arquivo de texto, ele cria um
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO! Ao ler o arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq, nome="desconhecido", idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try: 
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()

