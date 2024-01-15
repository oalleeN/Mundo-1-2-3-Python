dados = list()
pessoas = list()
dados.append('Pedro')
dados.append(40)
pessoas.append(dados[:])
print(pessoas[0][0])

#---------------------------------

test = list()
test.append('Pedro')
test.append(25)
galera = list()
galera.append(test[:])  # usamos o "[:]" para poder "salvar" o valor contido na primeira lista "test"
test[0] = 'Alan'        # e assim o resultado gerado ser o primeiro valor que foi adicionado
test[1] = 19
galera.append(test[:])  # após ter alterado o índice 0 e 1, vamos adicionar os novos "valores" ('Alan' 19)
print(galera)          # na variável "galera" para poder o novo valor aparecer.

#---------------------------------

galera = [['Jonas', 32], ['Jurubeba', 89], ['Gomes', 19], ['Santos', 12]]
print(galera[2]) # usamos para pegar todo um valor de tal indice, nesse caso seria o ['Gomes', 19]
print(galera[0][1]) # usamos para pegar o valor '1' contido dentro do indice '0', nesse caso seria o "32"

#---------------------------------

galera = [['Jonas', 32], ['Jurubeba', 89], ['Gomes', 19], ['Santos', 12]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')

#---------------------------------

galera = list()
dado = list() # irá receber os dados temporariamente
totmaior = totmenor = 0 # variável criada para fazer a contagem do total de maiores e menores de idade
for c in range(0, 2): # para poder fazer as duas perguntas duas vezes 
    dado.append(str(input('Digite seu nome: ')))
    dado.append(int(input('Digite sua idade: ')))
    galera.append(dado[:])
    dado.clear() # para excluir a variável "dado" e deixar apenas a "galera" com o dados contidos nela
    print('-=' * 20)
for p in galera: 
    if p[1] >= 21: # aqui já sabendo que a idade irá ficar no segundo bloco do indice, usamos o "p[1]" 
                    # para ir direto na idade do usuário
        print(f'{p[0]} é maior de idade') 
        totmaior += 1 # para poder fazer a contagem de quantos números são acima ou igual a 21
    else:
        print(f'{p[0]} é menor de idade')
        totmenor += 1 # para poder fazer a contagem de quantos números são abaixo de 21
print(f'Temos {totmaior} maior de idade e {totmenor} menor de idade') #e aqui sai o resultado desse números
#------------------------
