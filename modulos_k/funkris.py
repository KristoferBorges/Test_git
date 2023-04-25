import datetime
import time


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
