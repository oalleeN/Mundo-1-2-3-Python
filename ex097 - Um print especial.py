'''Faça uma programa que tenha uma função chamada escreva(), que receba 
um texto qualquer como parãmetro e mostre uma mensagem com tamanho 
adaptável. 

EX: 
escreva('Olá mundo!')

SAÍDA: 
-----------
 Olá mundo!
-----------
'''
def escreva():
    texto = str(input('Escreva... '))
    print('-' * len(texto))
    print(texto)
    print('-' * len(texto))

escreva() # serve para receber e mostrar os dados da função acima
