"""Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o
(com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar."""
import random
from datetime import datetime

contribuicao = 40
dados = dict()
dados['nome'] = str(input('Digite seu nome\n--> '))
dados['nascimento'] = int(input('Digite seu ano de Nascimento\n--> '))
idade = datetime.now().year - dados['nascimento']
dados['carteira'] = int(input('Digite o número da sua carteira de trabalho (0 CASO NÃO TENHA)\n--> '))
if dados['carteira'] != 0:
    dados['contratacao'] = datetime.now().year
    dados['salario'] = random.randint(2000, 3000)
    dados['aposentadoria'] = idade + contribuicao
    for k, v in dados.items():
        print(f'{k.upper()} = {v}')
else:
    for k, v in dados.items():
        print(f'{k.upper()} = {v}')
