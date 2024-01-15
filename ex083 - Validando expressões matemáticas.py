#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses
#abertos e fechados na ordem correta

expr = str(input('Digite a expressão: ')).strip()
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(') 
                #PARA CADA "(" QUE FOR DIGITADO PELO USUÁRIO, ELE VAI SER ADICIONADO NA LISTA "pilha"                      
    elif simb == ')':
        if len(pilha) > 0: #SE O TAMANHO DA "pilha" FOR MAIOR QUE 0, NO CASO VAI ESTAR SOBRANDO OU FALTANDO
             pilha.pop()   #ENTÃO COM ISSO VAI SER RETIRADO MESMO ASSIM, SE FOR ")" ELE VAI SER RETIRADO
        else:              #PELO MÉTODO ".pop()". MAS SE NÃO VAI SER ADICIONADO O ")" E ASSIM IRÁ ESTARÁ COMPLETO!
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está incorreta!')
