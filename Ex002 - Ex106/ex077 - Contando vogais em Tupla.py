'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, 
você deve mostrar, para cada palavra, quais são as suas vogais.'''

name = ('MEU','NOME','NAO','ALAN','MEU','NOME','ALLEN','MEU','SONHO','PROGRAMADOR')
for n in name:
    print(f' \n na palavra {n} temos' , end=' ')
    for letra in n:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
            