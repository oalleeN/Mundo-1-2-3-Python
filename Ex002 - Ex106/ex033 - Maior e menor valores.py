''' Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
n3 = int(input('Digite só mais um: '))
    

lista = [n1, n2, n3]


print(f'O maior número é o {max(lista)}')
print(f'O menor número é o {min(lista)}')



#Outra opção: 

primeiro = int(input('Primeiro numero: '))
segundo  = int(input('Segundo numero : '))
terceiro = int(input('Terceiro numero: '))

    # Achando o maior número
maior = primeiro

if (segundo > maior):
        maior = segundo
if (terceiro > maior):
        maior = terceiro

print('Maior: ',maior)

    # Achando o menor número
menor = primeiro

if (segundo < menor):
        menor = segundo
if (terceiro < menor):
        menor = terceiro

print('Menor: ',menor)
