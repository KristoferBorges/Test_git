"""Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função
input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)"""


def readInt(num):
    """
    --> Analisa o número digitado pelo usuário confirmando se foi digitado um número.
    :return: O valor digitado já confirmado se é de fato um número
    """
    try:
        if num.isnumeric():
            return print(f'Você digitou corretamente o número [{num}]')
    except TypeError:
        print('Os dados foram do tipo incorreto!')

