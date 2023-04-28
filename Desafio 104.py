"""Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função
input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)"""


def readInt():
    """
    --> Analisa o número digitado pelo usuário confirmando se foi digitado um número.
    :return: O valor digitado já confirmado se é de fato um número
    """
    while True:
        num = str(input('Digite um número: '))
        if num.isnumeric():
            number = int(num)
            break
        else:
            print('TENTE NOVAMENTE')
    return print(f'Você digitou o número {number}!')


readInt()
