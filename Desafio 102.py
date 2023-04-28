"""Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o
primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o processo de cálculo do fatorial."""


def factorial(num=1, show=False):
    """
    --> Cálculo de Fatorial com detalhe ou sem detalhe.
    :param num: Número escolhido para ver o fatorial
    :param show: Caso seja verdadeiro terá os detalhes da conta para o resultado final
    :return: Retorna o valor
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(f' = ', end=' ')
        f = f * c
    return print(f)


factorial(5, True)
