reta1 = float(input('Digite a primeira medida: '))
reta2 = float(input('Digite a segunda medida: '))
reta3 = float(input('Digite a terceira medida: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('É um triângulo', end='')
    if reta1 == reta2 == reta3:
        print(' EQUILÁTERO!')
    elif reta1 != reta2 != reta3 != reta1:
        print(' ESCALENO!')
    else:
        print(' ISÓSCELES') 

else: 
    print('Não é um triângulo')