"""
Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
"""

import requests

try:
    url = 'http://www.pudim.com.br/'
    response = requests.get(url)
except Exception as error:
    print(f'Não foi possível acessar o site por conta do erro {error.__class__}')
else:
    print('O site foi acessado e seu arquivo fonte foi armazenado!')
