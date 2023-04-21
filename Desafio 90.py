"""Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um
dicionário. No final, mostre o conteúdo da estrutura na tela."""

dados = dict()
dados['name'] = str(input('Digite o nome do aluno: ')).strip()
dados['average'] = float(input(f'Digite a Média do aluno [{dados["name"]}]:  '))


def situations():
    if dados['average'] >= 7.0:
        dados['situation'] = 'APPROVED'
    elif dados['average'] < 5.0:
        dados['situation'] = 'DISAPPROVED'
    else:
        dados['situation'] = 'RECUPERATION'


situations()
print()
print(f'Nome = {dados["name"]}\nMédia = {dados["average"]}\nSituação = {dados["situation"]}')
