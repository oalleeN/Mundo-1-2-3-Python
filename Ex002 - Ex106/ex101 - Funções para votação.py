'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento 
de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''

# Minha resolução
def voto(ano_de_nascimento):
    from datetime import date
    today = date.today()
    age = today.year - ano_de_nascimento
    if age >= 65:
        return F'Você tem {age} anos e seu voto é opcional!'
    if age <= 15:
        return F'Você tem {age} anos e seu voto foi negado!'
    if age >= 18 <= 64: 
        return F'Você tem {age} anos e seu voto é obrigatório!'
    if age == 17 or 16:
        return F'Você tem {age} anos e seu voto é opcional!'
        
idade = int(input('Digite seu ano de nascimento: '))
print(voto(idade))

# Resolução do professor:

def voto(ano):
       from datetime import date
       atual = date.today().year
       idade = atual - ano
       if idade < 16:
            return f'Com {idade} anos: NÃO VOTA!'
       elif 16 <= idade < 18 or idade > 65:
            return f'Com {idade} anos: VOTO OPCIONAL'
       else:
            return f'Com {idade} anos: VOTO OBRIGATÓRIO'
       
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
