'''Faça um programa que tenha um função chamada área(), 
 que receba as dimensões de um terreno retangular 
 (largura e comprimento) e mostre a área do terreno.'''

def terreno(largura, comprimento):
    terreno = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {terreno:.2f}m² ')

largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))

terreno(largura, comprimento) # para poder multiplicar os valores das "INPUT's"
