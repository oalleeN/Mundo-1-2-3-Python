núm = 0
soma = 0
cont = 0
núm = int(input('Digite um valor [999 para parar]: '))
while núm != 999:
    cont += 1
    soma += núm
    núm = int(input('Digite um valor [999 para parar]: '))
print(f'Você digitou {cont} números e a soma entre eles é de {soma}')

#----------------------------------------------------------------------
#duas formas, porém a mais recomendada é a primeira 

núm = cont = soma = 0
while núm != 999:
    núm = int(input('Digite um valor [999 para parar]: '))
    cont += 1
    soma += núm
print(f'Você digitou {cont - 1} números e a soma entre eles é de {soma - 999}')
