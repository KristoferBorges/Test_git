import datetime
import time

red = '\033[31m'
green = '\033[32m'
yellow = '\033[1;33m'
blue = '\033[34m'
blueBack = '\033[44m'
normal = '\033[m'
redBack = '\033[41m'
greenBack = '\033[42m'
yellowBack = '\033[43m'


def textFormatado(text):
    print('_' * 30 + normal)
    print('{}'.format(f'{text}'.center(30)))
    print('_' * 30)


def tryOption(op):

    while True:
        try:
            pass
        except ValueError:
            print(red + 'DIGITE UM NÚMERO INTEIRO VÁLIDO!' + normal)
        except Exception as error:
            print(red + f'ERRO DE {error.__class__}' + normal)
        else:
            if op in range(1, 4):
                return op
            else:
                print(red + 'APENAS NÚMEROS INTEIROS DAS OPÇÕES LISTADAS!' + normal)


def tryName(name):
    while True:
        try:
            pass
        except Exception as error:
            print(red + f'ERRO DE {error.__class__}')
        else:
            if name.isalpha():
                return name
            else:
                print(red + 'APENAS LETRAS!' + normal)


def tryAge(age):
    """
    --> Função usando tratamento de erros para identificar se o usuário digitou um número inteiro.
    :param age: idade ou número digitado pelo usuário.
    :return: retorna um except em caso de problema, caso não haja problemas o sistema seguirá com o número do usuário.
    """
    while True:
        try:
            pass
        except Exception as error:
            print(red + f'ERRO DE {error.__class__}')
        else:
            if age.isnumeric():
                age = int(age)
                return age
            else:
                print(red + 'APENAS NÚMEROS INTEIROS!' + normal)


def dateVerification(data):
    """
    --> Pedido do cliente: 'Preciso que o sistema pegue o dia de ontem baseado na data atual'.
    --> Sistema: Ele pegará a data atual e fara uma formatação dos dois primeiros números, fazendo com que seja a data
    de ontem.
    Exemplo: 15/03/2021 = 14/03/2021
    :return: Retornará uma string com a data de ontem
    """
    if len(data) == 0:
        date = datetime.datetime.now()
        date = datetime.datetime.date(date)
        date_formatada = date.strftime("%d/%m/%Y")
        data = date_formatada
        data_soma = int(data[:2])
        data_soma = data_soma - 1
        data = str(data_soma) + data[2:]
        # Data de ontem formatada
    print(data)


def maiorNumero(lista):
    """
    --> Define os maiores números de uma lista.
    :param lista:
    :return: String com os valores.
    """
    tamanho = len(lista)
    if tamanho > 0:
        maior = max(lista)
        menor = min(lista)
    else:
        maior = 0
        menor = 0
        tamanho = 0
    print(f'Foram recebidos ao todo [{tamanho}] números!\nO maior número obtido foi [{maior}]\n'
          f'O menor número obtido foi [{menor}]')


def contadorPersonalizado(start, end, jump):
    """
    --> Contador personalizado, pode conta de trás para frete ou de frente para trás.
    :param start:
    :param end:
    :param jump:
    :return: uma string com os passos.
    """
    # ContadorPersonalizado
    print('=' * 26)
    print(f'Contagem de [{start}] até [{end}] de [{jump} em {jump}]')
    print('=' * 26)

    if end > start:
        for n in range(start, end + 1, jump):
            print(n)
            time.sleep(0.2)
        print('FINISH')
    elif end < start:
        for n in range(start, end - 1, jump):
            print(n)
            time.sleep(0.1)
        print('FINISH')
