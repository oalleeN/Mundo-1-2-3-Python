w = maior = menor = 0

while True:

    print('-=-' * 15)
    idade = int(input('Qual a sua idade: '))
    print('-=-' * 15)
    sexo = str(input('Qual seu sexo? \nMasculino [M]\nFeminino [F]\nDigite aqui: ')).upper().strip()[0]
    print('-=-' * 15)
    print('Cadastro feito com sucesso!')
    print('-=-' * 15)
    cadastro = str(input('Deseja continuar? \nSim [S]\nNão [N]\nDigite aqui: ')).upper().strip()[0]
    print('-=-' * 15)

    if cadastro == 'S':
        if idade >= 18:
            maior += 1
        if sexo == 'F' or 'f':
            if idade <= 20:
                menor += 1
        if sexo == 'M' or 'm':
            w += 1
    else:
        if cadastro == 'N':
            print(f'Pessoas com mais de 18 anos: {maior}' )
            print(f'Homens que foram cadastrados: {w}')
            print(f'Mulheres com menos de 20 anos: {menor}')
            break

# abaixo veremos a forma que um cara fez do GitHub

add_age = add_men = add_women = 0

while True:
    age = int(input("Idade: \n"))
    if age >= 18:
        add_age += 1
    sex = str(input("Sexo: [M / F] \n")).strip().upper()
    if sex == "M":
        add_men += 1
    elif sex == "F":
        if age < 20:
            add_women += 1
    choice = str(input("Continuar? [S / N] \n")).strip().upper()
    if choice == "N":
        print(f"Pessoas com mais de 18: {add_age}.")
        print(f"Homens cadastrados: {add_men}")
        print(f"Mulheres com menos de 20 anos: {add_women}")
        break
