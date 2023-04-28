"""Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
algum dado não tenha sido informado corretamente."""


def token(name, gols):
    """
    --> Registros de jogadores e gols realizados, o programa também pode aceitar dados nulos.
    :param name: Nome do jogador (none caso não digitado)
    :param gols: Gols do jogador (none caso não digitado)
    :return:
    """
    return print(f'JOGADOR > {name}\nQUANTIDADE DE GOLS > {gols}')


nome = str(input('NOME DO JOGADOR: '))
if len(nome) == 0:
    nome = "NÃO INFORMADO"
qnt_gols = str(input('QUANTIDADE DE GOLS: '))
if qnt_gols.isnumeric():
    qnt_gols = int(qnt_gols)
else:
    qnt_gols = "NÃO INFORMADO"
token(nome, qnt_gols)
