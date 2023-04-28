"""
Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro()
e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
"""


def dobro(number):
    """
    -> Dobra o valor passado como parâmetro.
    EX: 100 * 2 = 200
    :param number: Valor passado.
    :return: O dobro do valor passado.
    """
    number = (number * 2)
    return number


def metade(number):
    """
    -> Divide por 2 o valor passado como parâmetro.
    EX: 100 / 2 = 50
    :param number: Valor passado.
    :return: A metade do valor passado
    """
    number = (number / 2)
    return number


def aumentar(number):
    """
    -> Aumenta 10% do valor passado como parâmetro.
    EX: 100 + 10% = 110
    :param number: Valor passado.
    :return: Retorna +10% somado com o valor passado.
    """
    number = number + (number * 0.10)
    return number


def diminuir(number):
    pass
