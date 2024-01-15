while True:
    n = (int(input('Digite um número: ')))
    print('-=-' * 10)
    print('[1] Binário')
    print('[2] Octal')
    print('[3] Hexadecimal')
    print('[X] Fechar')
    print('-=-' * 10)

    pergunta = (str(input('Digite a opção em que queira converter: ')))

    if pergunta == 'x' or pergunta == 'X':
        break
    elif pergunta == '1' or pergunta == '2' or pergunta == '3':
       if pergunta == '1':
         bn = str(bin(n))
         print(bn)

       elif pergunta == '2':
         oc = str(oct(n))
         print(oc)

       elif pergunta == '3':
         he = str(hex(n))
         print(he)

    else:
        print('Opção inválida!')

#---------------------------------------------------------------------------------------------------

num = int(input('Digite um número inteiro: '))
print('''ESCOLHA UMA DAS BASES PARA CONVERSÃO: 
[1] Binário
[2] Octal
[3] Hexadecimal''')

opção = int(input('Digite aqui: '))

if opção == 1:
    print(f'O resultado em base BINÁRIA é a seguinte {bin(num)[2:]} ')
elif opção == 2:
    print(f'O resultado em base OCTAL é o seguinte {oct(num)[2:]}')
elif opção == 3:
    print(f'O resultado em base HEXADECIMAL é a seguinte {hex(num)[2:]}')
else:
    print('Número inválido. Tente novamente...')