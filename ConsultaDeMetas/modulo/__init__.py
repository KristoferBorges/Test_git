# Cores
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
ciano = '\033[36m'
normal = '\033[m'
roxo = '\033[35m'
rosa = '\033[95m'


def tryOption(option):
    """
    --> Função para determinar a opção que o usuário irá escolher no menu, atualmente temos 3 opções, de registro,
    consulta ou de sair do programa, caso o usuário digitar outro número ou letras fora do esperado o sistema
    apresentará uma exceção.
    :param option: Entrada do usuário.
    :return: Retorna a opção escolhida em caso de zero exceções.
    """
    try:
        option = int(option)
    except ValueError:
        print(red + 'DIGITE UM NÚMERO INTEIRO VÁLIDO!' + normal)
    except Exception as error:
        print(red + f'ERRO DE {error.__class__}' + normal)
    else:
        if option in range(1, 4):
            return option
        else:
            print(red + 'APENAS NÚMEROS INTEIROS DAS OPÇÕES LISTADAS!' + normal)


def tryExclusion(option):
    """
    --> Função para determinar a opção que o usuário irá escolher no menu, atualmente temos 4 opções, poderá excluir as
    listas separadamente ou todas ao mesmo tempo, caso o usuário digitar outro número ou letras fora do esperado o
    sistema apresentará uma exceção.
    :param option: Entrada do usuário.
    :return: Retorna a opção escolhida em caso de zero exceções.
    """
    try:
        option = int(option)
    except ValueError:
        print(red + 'DIGITE UM NÚMERO INTEIRO VÁLIDO!' + normal)
    except Exception as error:
        print(red + f'ERRO DE {error.__class__}' + normal)
    else:
        if option in range(1, 5):
            return option
        else:
            print(red + 'APENAS NÚMEROS INTEIROS DAS OPÇÕES LISTADAS!' + normal)
