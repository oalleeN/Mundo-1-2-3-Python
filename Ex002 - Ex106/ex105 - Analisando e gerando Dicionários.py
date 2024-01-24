'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.'''

def notas(*num, sit=False):
    """
    -> Função para analizar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos.
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicinário com várias informações sobre a situação da turma.
    """
    nota = dict()
    nota['total'] = len(num)
    nota['menor'] = min(num)
    nota['maior'] = max(num)
    nota['média'] = sum(num) / len(num)
    if sit==True:
        if nota['média'] <= 4.9:
            nota['situação'] = 'RUIM'
        elif nota['média'] >= 8.5:
            nota['situação'] = 'EXCELENTE'
        elif nota['média'] >= 6.6 <= 8.4:
            nota['situação'] = 'BOM'
        elif nota['média'] >= 5 <= 6.5:
            nota['situação'] = 'RAZOÁVEL'
    return nota

resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)


# Resolução do professor:
def notas(*n, sit=False):
    """
    -> Função para analizar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos.
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicinário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['menor'] = min(n)
    r['maior'] = max(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] <= 4.9:
            r['situação'] = 'RUIM'
        elif r['média'] >= 8.5:
            r['situação'] = 'EXCELENTE'
        elif r['média'] >= 6.6 <= 8.4:
            r['situação'] = 'BOM'
        elif r['média'] >= 5 <= 6.5:
            r['situação'] = 'RAZOÁVEL'
    return r

# Programa principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
