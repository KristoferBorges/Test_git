"""Exercício Python 101: Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições."""

import datetime


def voto(idade):
    """
    --> Recebe como parâmetro a idade do usuário, após receber ele fará uma análise identificando se o usuário é menor
    de 18 anos, se ele for menor retornará um print escrito "VOTO É NEGADO", caso ele tenha de 18 anos até 64 mostrará
    outro print escrito "VOTO É OBRIGATÓRIO", no último caso, se ele tiver mais de 65 anos retornará um print escrito
    "VOTO É OPCIONAL".
    :param idade: Idade do usuário.
    :return: print('VOTO É NEGADO / VOTO É OBRIGATÓRIO / VOTO É OPCIONAL') + nome do usuário
    """
    if idade < 18:
        print(nome)
        return print(f'Com {idade} o VOTO É NEGADO')
    elif 18 <= idade < 65:
        print(nome)
        return print(f'Com {idade} o VOTO É OBRIGATÓRIO')
    else:
        print(nome)
        return print(f'Com {idade} o VOTO É OPCIONAL')


# Main Program
print('=' * 29)
print('{:>21}'.format('|FORMULÁRIO|'))
print('=' * 29)
nome = str(input('Digite seu nome: '))
nascimento = int(input('Nascimento: '))
calculo_idade = (datetime.datetime.now().year - nascimento)
voto(calculo_idade)
