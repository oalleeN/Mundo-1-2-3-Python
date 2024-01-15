por_exten = ('zero', 'um', 'dois', 'três', 'quatro', 
             'cinco', 'seis', 'sete', 'oito', 'nove', 
             'dez', 'onze', 'doze', 'treze', 'quartoze',
             'quinze', 'dezesseis', 'dezessete', 'dezoito',
              'deznove', 'vinte')

while True:
    num = int(input('DIGITE UM NÚMERO DE 0 Á 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente!')
print(f'O número {num} por extenso é {por_exten[num]}')
