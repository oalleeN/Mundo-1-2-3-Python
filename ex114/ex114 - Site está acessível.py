'''Crie um código em Python que teste se o site pudim está acessível pelo computador usado.'''

import requests

def acessar_site(url):
    try:
        resposta = requests.get(url) #
    except requests.RequestException:
        print()
        print(f'\033[31mErro na solicitação\033[m')
    else:
        #Verifica se a solição foi bem-sucedida (código de status 200)
        resposta.status_code == 200
        print()
        print('\033[32mA solicitação foi bem-sucedida\033[m')

url_alvo = "http://www.pudim.com.br"
acessar_site(url_alvo)