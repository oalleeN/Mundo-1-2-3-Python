'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''

nome = str(input('Digite seu nome completo: '))
print(f'Seja bem-vindo(a), {nome}')

n1 = float(input('Digite sua nota do 1º bimestre: '))
n2 = float(input('Digite sua nota do 2º bimestre: '))

média = (n1 + n2) / 2

if média >= 7.0:
    print(f'APROVADO! Sua média foi de {média:.1f}')

elif média <= 5.0:
    print(f'REPROVADO! Sua média foi de {média:.1f}')

elif média > 5.0 and média < 7:
    print(f'RECUPERAÇÃO! Sua média foi de {média:.1f}')
#elif 7 > média >= 5:                     PODE USAR DESTA FORMA AI!!!!
