"""
Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro()
e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
"""

dinheiro = 'R$ '


def dobro(number):
    """
    -> Dobra o valor passado como parâmetro.
    EX: 100 * 2 = 200
    :param number: Valor passado.
    :return: O dobro do valor passado.
    """
    global dinheiro
    number = (number * 2)
    return f'{dinheiro}' + f'{number:,.2f}'.replace('.', ',')


def metade(number):
    """
    -> Divide por 2 o valor passado como parâmetro.
    EX: 100 / 2 = 50
    :param number: Valor passado.
    :return: A metade do valor passado
    """
    global dinheiro
    number = (number / 2)
    return f'{dinheiro}' + f'{number:,.2f}'.replace('.', ',')


def aumentar(number, aumento=0.50):
    """
    -> Aumenta 10% do valor passado como parâmetro.
    EX: 100 + 10% = 110
    :param aumento:
    :param number: Valor passado.
    :return: Retorna +10% somado com o valor passado.
    """
    global dinheiro
    number = number + (number * aumento)
    return f'{dinheiro}' + f'{number:,.2f}'.replace('.', ',')


def diminuir(number, reducao=0.50):
    """
        -> Diminui 10% do valor passado como parâmetro.
        EX: 100 - 10% = 90
        :param reducao:
        :param number: Valor passado.
        :return: Retorna -10% somado com o valor passado.
        """
    global dinheiro
    number = number - (number * reducao)
    return f'{dinheiro}' + f'{number:,.2f}'.replace('.', ',')


def moeda(number):
    """
    -> Função inútil para seu proposito atual.
    :param number: Valor do usuário
    :return: None
    """
    global dinheiro
    return f'{dinheiro}{number:,.2f}'.replace('.', ',')


def resumo(number):
    print()
    print(f' [!] - Valor digitado [{moeda(number)}')
    print(f' [!] - Dobro = {dobro(number)}')
    print(f' [!] - Metade = {metade(number)}')
    print(f' [!] - Aumentado = {aumentar(number)}')
    print(f' [!] - Redução = {diminuir(number)}')
