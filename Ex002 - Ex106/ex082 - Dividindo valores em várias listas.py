'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e 
os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

valores = list()
impar = list()
par = list()
while True:
    valores.append(int(input('Digite um número: ')))
    resp = str(input('Deseja continuar [S/N]: ')).upper().strip()
    if resp not in 'SN':
        resp = str(input('Erro! Por favor, digite SIM (S) ou NÃO (N):  ')).upper().strip()
        if resp == 'N':
            break
    elif resp in 'N':
        break
for v in valores:
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'Aqui está a lista completa: {valores}')
print(f'-=' * 20)
print(f'Aqui está a lista de números pares: {par}')
print(f'-=' * 20)
print(f'Aqui está a lista de números ímpares: {impar}')
