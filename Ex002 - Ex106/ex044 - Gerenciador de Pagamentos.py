'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''

cliente = str(input('Nome do cliente: '))
produto = float(input('Digite o valor da compra: '))

print('Digite: ')
print('[1] para dinheiro ou cheque.')
print('[2] para cartão de crédito ou débito.')

opção = str(input('Digite aqui: '))

if opção == '2':
       print('Comprando à vista no cartão você terá 5% de desconto')
       print('-=-' * 10)
       print('Compre em até 2x no cartão sem juros.')
       print('-=-' * 10)
       print('Compre em até 3x ou mais no cartão com 20% de juros.')
       print('-=-' * 10)
       print('Digite: ')
       print('[1] para comprar à vista.')
       print('[2] para 2x sem juros')
       print('[3] para 3x ou mais com 20% de juros.')
       print('-=-' * 10)

       opção2 = str(input('Digite aqui: '))

       print('-=-' * 10)

       if opção2 == '1':
         a_vista = produto - (produto * 5 / 100)
         print(f' Valor sem desconto R${produto}. Valor com os 5% de desconto R${a_vista:.2f}.') 

       elif opção2 == '2':
         duas_vezes = produto / 2
         print(f' Sua parcela ficará de R${duas_vezes:.2f} sem juros.')

       elif opção2 == '3':
         total = produto + (produto * 20 / 100)
         totalparc = int(input('Em quantas parcelas? '))
         parcela = total / totalparc
         print(f'Sua compra de R${produto} em {totalparc}x, vai sair com uma parcela de R${parcela:.2f} com 20% de juros')
         print(f'O preço que será pago após quitar as parcelas será de {total:.2f}')

if opção == '1':
        desconto = produto - (produto * 10 / 100)
        print(f'Sua compra com 10% de desconto ficou: R${desconto:.2f}')
