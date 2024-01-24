''' Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''
nome = str(input('Qual o seu nome? '))
salario = float(input('Digite seu salário: '))

aumento1 = salario + (salario * 10 /100)
aumento2 = salario + (salario * 15 / 100)

if salario >=1250:
    print(f'Prezado {nome}, o seu salário de R${salario} teve um aumento de 10% e ficou o seguinte: R${aumento1:.2f}')
else:
    print(f'Prezado {nome}, o seu salario de R${salario} teve um aumento de 15% e ficou o seguinte: R${aumento2:.2f} ')  
 