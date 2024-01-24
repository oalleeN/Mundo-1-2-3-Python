def separate():
    print('-=' *40)
def lin():
    print('--' *10)

#Programa principal
lin()
print('    PARA O MEU    ')
lin()
print('      GitHub     ')
lin()
print('     SOU O ALAN    ')
lin()

separate()
# Agora usando textos 
def título(txt):
    print('--' *10)
    print(txt)
    print('--' *10)

título('    TESTANDO    ')   
título('   FUNCIONANDO   ')
título('     ÊXITO    ')

separate()
# Calculando parãmetros
def ssoma(a , b):
    s = a + b # Função que recebe dois números e retorna a soma
    print(s)

ssoma(2, 3)
ssoma(3, 4)
ssoma(5, 6)

separate()
# Outro modo:
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')

soma(a=4, b=5)

separate()
# Empacotar parãmetros
def contador (* núm):
    for valor in núm:
        print(f'{valor} ', end='- ')
    print('FIM')

contador(2, 3 ,8)
contador(9, 5, 7, 1, 3)
contador(0, 2, 4, 0)

separate()

# outro modo:
def cont(* numbers):
    print(numbers)

cont(2, 3 ,8)
cont(9, 5, 7, 1, 3)
cont(0, 2, 4, 0)

separate()

def conta (* numero):
    print(f'Recebi os valores {numero} e são ao todo {len(numero)} números')

conta(6, 3 ,7)
conta(2, 5, 8, 1, 0)
conta(0, 1, 4, 9)

separate()

# Função para dobrar os valores
def dobra(lst):
    pos = 0 #começa na posição 0
    while pos < len(lst): # enquanto for menor que o tmn da lista, ele vai continuar contando
        lst[pos] *= 2 
        pos += 1
valores = [7, 2, 3, 5, 0, 4]
dobra(valores)
print(valores)

separate()