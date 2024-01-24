'''try: # tente
    a = int(input('Numerador: ')) 
    b = int(input('Denominador: ')) # operação/código que deseja testar
    r = a / b
except: # exceção/erro correspondente
    print('Infelizemente tivemos um erro!')
else: 
    print(f'O resultado é {r:.1f}')
finally: # esse resultado vai acontecer sempre mesmo se der erro ou não no código
    print('Volte sempre!')'''


'''try: # tente
    a = int(input('Numerador: ')) 
    b = int(input('Denominador: ')) # operação/código que deseja testar
    r = a / b
except Exception as erro: # erro com variável para saber a tipagem
    print(f'Infelizemente tivemos um erro em {erro.__class__}!')
else: 
    print(f'O resultado é {r:.1f}')
finally: # esse resultado vai acontecer sempre mesmo se der erro ou não no código
    print('Volte sempre!')'''

try: # tente
    a = int(input('Numerador: ')) 
    b = int(input('Denominador: ')) # operação/código que deseja testar
    r = a / b
except (ValueError, TypeError): # para mostrar o erro direto
    print(f'Infelizemente tivemos um erro com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados')
else: 
    print(f'O resultado é {r:.1f}')
finally: # esse resultado vai acontecer sempre mesmo se der erro ou não no código
    print('Volte sempre!')
