somaidade = 0
médiaidade = 0
maioridade = 0
nomevelho = ''
totalfem = 0
for p in  range(1 , 5):
    print(f'====== {p}º PESSOA ======')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip()
    somaidade += idade

    if p == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade 
        nomevelho = nome
    if sexo in 'Ff' and idade > maioridade:
        totalfem += 1

médiaidade = somaidade / 4
print(f'A média de idade do grupo é de {médiaidade}')
print(f'O homem mais velho do grupo tem {maioridade} e se chama {nomevelho}')
print(f'No grupo há {totalfem} mulher(es) abaixo de 20 anos')
