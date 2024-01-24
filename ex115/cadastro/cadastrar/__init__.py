def cadastro_nome(nome):
    ok = False
    nom = list()
    while True:
        perg = str(input(nome)).strip()
        if perg.isalpha():
            nom.append(perg)
            ok = True
        else:
            print('ERRO! Digite o nome corretamente.')
        if ok:
            break
    return nom

def cadastro_idade(idade):
    ok = False
    ida = list()
    while True:
        perg = input(idade).strip()
        if perg.isnumeric():
            ida.append(int(perg))
            ok = True
        else:
            print('ERRO! Digite a idade corretamente.')
        if ok:
            break
    return ida


def dicionario(nome, idade):
    print('~' * 35)
    print('Opção 1'.center(35))
    print('~' * 35)
    n = cadastro_nome
    i = cadastro_idade
    return f'{n} \t{i}'