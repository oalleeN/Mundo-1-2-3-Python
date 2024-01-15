''' Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''
d = int(input(' Quantos dias você ficou com o carro alugado? '))
km = float(input(' Quantos quilõmetros foram percorridos durante o tempo do seu aluguel? '))

r = (60 * d) + (0.15 * km)

print(f' O valor total do aluguel é de: R%{r:.2f}')
