"""
Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
"""

import requests

red = '\033[31m'
green = '\033[32m'
yellow = '\033[1;33m'
blue = '\033[34m'
blueBack = '\033[44m'
normal = '\033[m'
redBack = '\033[41m'
greenBack = '\033[42m'
yellowBack = '\033[43m'

try:
    url = 'http://www.pudim.com.br/'
    response = requests.get(url)
except Exception as error:
    print(red + f'Não foi possível acessar o site por conta do erro {error.__class__}' + normal)
else:
    print(green + 'O site foi acessado e seu arquivo fonte é:' + normal)
    for linha in response:
        print(linha)

