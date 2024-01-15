cadastro = list()
princ = list()
totalpessoas = 0 
mai = men = 0
while True:
    cadastro.append(str(input('Nome: ')))
    cadastro.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = cadastro[1] # Se o tamanho da variável for igual á 0, quer dizer que não há valor inserido, logo o maior e menor são "cadastro[1]"
    else:
        if cadastro[1] > mai: # Aqui basicamente ele vai jogar um valor para saber se é maior ou não que
            mai = cadastro[1] # o valor já cadastrado do índice [1]!
        if cadastro[1] < men: # Aqui ele vai fazer o mesmo que o maior, porém para saber o menor valor!
            men = cadastro[1]
    princ.append(cadastro[:]) # CÓPIA
    cadastro.clear() # Utilizado para limpar os dados antigos para deixar somente os dados da nova cópia nessa situação do código!
    totalpessoas += 1
    perg = str(input('Você deseja continuar? [S/N]: ')).upper()
    if perg in 'Nn':
        break
print(f'O total de pessoas cadastradas é de {totalpessoas}!') # lembrando que aqui eu poderia também utilizar
print(f'O maior peso foi de {mai}kg. Peso de' ,end=' ')    # o "len(princ)" para fazer a contagem dos cadastros
for p in princ:
    if p[1] == mai: # Se p[1] (Peso) for igual ao maior, ele irá resultar ao p[0] (Nome) que condiz com a lista 
        print(f'{[p[0]]}')
print(f'O menor peso foi de {men}kg. Peso de' ,end=' ')
for p in princ:
    if p[1] == men: # Se p[1] (Peso) for igual ao menor, ele irá resultar ao p[0] (Nome) que condiz com a lista
        print(f'{[p[0]]}')
