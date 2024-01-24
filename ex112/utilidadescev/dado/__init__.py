def leiaDinheiro(msg):
    ok = False
    valor = ''
    while True:
        p = str(input(msg)).replace(",", ".").strip()
        if p.isalpha():
            print(f'\033[0;31mERRO! "{p}" é um preço inválido\033[m')
        elif p == '':
            print(f'\033[0;31mERRO! "{p}" é um preço inválido\033[m')
        else:
            valor = float(p)
            ok = True
        if ok:
            break
    return valor
