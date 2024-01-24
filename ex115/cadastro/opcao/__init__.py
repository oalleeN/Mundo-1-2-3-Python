def leia_opcao(msg):
    ok = True
    valor = 0
    while True:
        try:
            perg = str(input(msg)).strip()
            if perg.isnumeric() == 1 or 2 or 3:
                valor = int(perg)
                return valor
            elif perg.isnumeric() != 1 and 2 and 3:
                print('Digite uma opção válida')
                continue
        except (ValueError, TypeError):
            print('ERRO! Digite um número inteiro válido.')
        else:
            return valor
