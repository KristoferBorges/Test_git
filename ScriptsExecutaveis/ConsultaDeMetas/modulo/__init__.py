# Cores
import sys
import random
import datetime

red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
ciano = '\033[36m'
normal = '\033[m'
roxo = '\033[35m'
rosa = '\033[95m'


def tryOption(option):
    """
    --> Função para determinar a opção que o usuário irá escolher no menu, atualmente temos 6 opções, de registro,
    consulta ou de sair do programa, caso o usuário digitar outro número ou letras fora do esperado o sistema
    apresentará uma exceção.
    :param option: Entrada do usuário.
    :return: Retorna a opção escolhida em caso de zero exceções.
    """
    try:
        option = int(option)
    except ValueError:
        if option != 'adm':
            print(red + ' [!] - DIGITE UM NÚMERO INTEIRO VÁLIDO!' + normal)
    except Exception as error:
        print(red + f' [!] - ERRO DE {error.__class__}' + normal)
    else:
        if option in range(1, 7):
            return option
        elif option == 'adm':
            return option
        else:
            print(red + ' [!] - APENAS NÚMEROS DAS OPÇÕES LISTADAS!' + normal)


def tryOptionList(option):
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
        if option != 'adm':
            print(red + ' [!] - DIGITE UM NÚMERO INTEIRO VÁLIDO!' + normal)
    except Exception as error:
        print(red + f' [!] - ERRO DE {error.__class__}' + normal)
    else:
        if option in range(1, 4):
            return option
        elif option == 'adm':
            return option
        else:
            print(red + ' [!] - APENAS NÚMEROS DAS OPÇÕES LISTADAS!' + normal)


def tryOptionConsult(option):
    """
    --> Função para determinar a opção que o usuário irá escolher no menu, atualmente temos 4 opções, de consulta,
    caso o usuário digitar outro número ou letras fora do esperado o sistema apresentará uma exceção.
    :param option: Entrada do usuário.
    :return: Retorna a opção escolhida em caso de zero exceções.
    """
    try:
        option = int(option)
    except ValueError:
        print(red + ' [!] - DIGITE UM NÚMERO INTEIRO VÁLIDO!' + normal)
    except Exception as error:
        print(red + f' [!] - ERRO DE {error.__class__}' + normal)
    else:
        if option in range(1, 5):
            return option
        else:
            print(red + ' [!] - APENAS NÚMEROS INTEIROS DAS OPÇÕES LISTADAS!' + normal)


def tryOptionBackup(option):
    """
    --> Função para determinar a opção que o usuário irá escolher no menu, atualmente temos 4 opções, de Backup,
    caso o usuário digitar outro número ou letras fora do esperado o sistema apresentará uma exceção.
    :param option: Entrada do usuário.
    :return: Retorna a opção escolhida em caso de zero exceções.
    """
    try:
        option = int(option)
    except ValueError:
        print(red + ' [!] - DIGITE UM NÚMERO INTEIRO VÁLIDO!' + normal)
    except Exception as error:
        print(red + f' [!] - ERRO DE {error.__class__}' + normal)
    else:
        if option in range(1, 5):
            return option
        else:
            print(red + ' [!] - APENAS NÚMEROS INTEIROS DAS OPÇÕES LISTADAS!' + normal)


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
        print(red + ' [!] - DIGITE UM NÚMERO INTEIRO VÁLIDO!' + normal)
    except Exception as error:
        print(red + f' [!] - ERRO DE {error.__class__}' + normal)
    else:
        if option in range(1, 5):
            return option
        else:
            print(red + ' [!] - APENAS NÚMEROS INTEIROS DAS OPÇÕES LISTADAS!' + normal)


def verificar_numero(valor):
    """
    --> Sub-Função para verificar se o input do usuário foi um número.
    :param valor: input do arquivo main.py
    :return: Valor verdadeiro ou falso
    """
    try:
        numero = float(valor)
        return True
    except ValueError:
        return False


def capturaDeValoresMetaDia():
    """
    --> Função simples para identificar se o usuário digitou um número inteiro válido para as metas do dia.
    :return: Retorna o número em caso de digitar corretamente.
    """
    try:
        while True:
            metaDia = input(green + ' [?] - Qual a Meta do Dia R$ ' + normal)
            if verificar_numero(metaDia):
                metaDia = float(metaDia)
                return metaDia
            else:
                print(red + ' [!] - Valor inválido. Insira um número válido.' + normal)
    except ValueError:
        print(red + ' [!] - DIGITE UM NÚMERO INTEIRO VÁLIDO!' + normal)


def capturaDeValoresVendaDia():
    """
    --> Função simples para identificar se o usuário digitou um número inteiro válido para as vendas do dia.
    :return: Retorna o número em caso de digitar corretamente.
    """
    try:
        while True:
            vendaDia = input(green + ' [?] - Qual a Venda do Dia R$ ' + normal)
            if verificar_numero(vendaDia):
                vendaDia = float(vendaDia)
                return vendaDia
            else:
                print(red + ' [!] - Valor inválido. Insira um número válido.' + normal)
    except ValueError:
        print(red + ' [!] - DIGITE UM NÚMERO INTEIRO VÁLIDO!' + normal)


def capturaDeValoresPecaDia():
    """
        --> Função simples para identificar se o usuário digitou um número inteiro válido para as peças do dia.
        :return: Retorna o número em caso de digitar corretamente.
        """
    try:
        while True:
            pecaDia = input(green + ' [?] - Quantas peças Vendeu Hoje: ' + normal)
            if pecaDia.isnumeric():
                pecaDia = int(pecaDia)
                return pecaDia
            else:
                print(red + ' [!] - Valor inválido. Insira um número válido.' + normal)
    except ValueError:
        print(red + ' [!] - DIGITE UM NÚMERO INTEIRO VÁLIDO!' + normal)


def tryIsNumber_pecas(valor):

    """
        --> Função simples para identificar se o usuário digitou um número inteiro válido no caso das peças.
        :param valor:
        :return: Retorna o número em caso de digitar corretamente.
        """
    try:
        pass
    except ValueError:
        print(red + ' [!] - DIGITE UM NÚMERO INTEIRO VÁLIDO!' + normal)
    except Exception as error:
        print(red + f' [!] - ERRO DE {error.__class__}' + normal)
    else:
        if valor.isnumeric():
            return int(valor)
        else:
            print(red + ' [!] - DIGITE UM NÚMERO INTEIRO VÁLIDO!' + normal)
            sys.exit()


def abatimento(meta, vendas):
    """
    Função para verificar se as metas foram atingidas, caso não tenham sido, o sistema apresentará o sinal de menos "-".
    :param meta: Valor da meta
    :param vendas: Valor das vendas
    :return: Um sinal negativo para em casos de não atingir as metas.
    """
    if vendas >= meta:
        devedor = ""
    else:
        devedor = "-"
    return devedor


def testList():
    """
    --> Função em aprimoramento para rápidas inserções de dados sem a necessidade de interação com o usuário
    (Ainda em desenvolvimento).
    :return: Inserção dos dados de forma aleatória.
    """
    global data, metaDia, vendaDia, linhas, linha, metaAcRDMARCAS, vendaAcRDMARCAS, sobrasRD, \
        porcentagemRDMARCAS, linhas2
    metaAcRDMARCAS = 0
    vendaAcRDMARCAS = 0
    sobrasRD = 0
    porcentagemRDMARCAS = 0
    quantidade = int(input(yellow + '[?] - Digite a quantidade de informações para inserir: '))
    for info in range(quantidade):
        # Inputs de dados - RD Marcas-TESTE
        print('\n')
        print(green + f'[{info + 1}] - CONCLUIDO' + normal)
        data = "31/03/2023"
        dateVerification()
        metaDia = float(random.randint(100, 1000))
        vendaDia = float(random.randint(100, 1000))
        with open("metaAcumuladaRDMARCAS.txt", "a") as metaAcumuladaRDMARCAS:
            metaAcumuladaRDMARCAS.write(f"{metaDia}\n")
        with open("metaAcumuladaRDMARCAS.txt", "r") as metaAcumuladaRDMARCAS:
            linhas = metaAcumuladaRDMARCAS.readlines()

        for linha in linhas:
            metaAcRDMARCAS = metaAcRDMARCAS + float(linha.strip())
        print(yellow + f" [!] - META ACUMULADA = ", end='')
        print(rosa + f"R$ {metaAcRDMARCAS:.2f}" + normal)

        # Cálculo de Vendas acumuladas
        with open("vendaAcumuladaRDMARCAS.txt", "a") as vendaAcumuladaRDMARCAS:
            vendaAcumuladaRDMARCAS.write(f"{vendaDia}\n")
        with open("vendaAcumuladaRDMARCAS.txt", "r") as vendaAcumuladaRDMARCAS:
            linhas2 = vendaAcumuladaRDMARCAS.readlines()

        for linha in linhas2:
            vendaAcRDMARCAS = vendaAcRDMARCAS + float(linha.strip())
        print(yellow + f" [!] - VENDA ACUMULADA = ", end='')
        print(rosa + f"R$ {vendaAcRDMARCAS:.2f}" + normal)

        # Cálculo de porcentagem
        if vendaAcRDMARCAS < metaAcRDMARCAS:
            sobrasRD = (metaAcRDMARCAS - vendaAcRDMARCAS)
        elif metaAcRDMARCAS < vendaAcRDMARCAS:
            sobrasRD = (vendaAcRDMARCAS - metaAcRDMARCAS)
        else:
            sobrasRD = 0
        porcentagemRDMARCAS = (vendaAcRDMARCAS / metaAcRDMARCAS) * 100
        print(yellow + f" [!] - PORCENTAGEM ACUMULADA = ", end='')
        print(rosa + f"{porcentagemRDMARCAS:.2f}%" + normal)
        print('\n')
        print(rosa + '=-' * 21 + normal)
        print(roxo + texto_dados_centralizado + normal)
        print(rosa + '=-' * 21 + normal)
        # Inserção de dados
        with open("listaRDMARCAS.txt", "a") as listaRDMARCAS:
            listaRDMARCAS.write(f"{data}|R${metaDia:.2f}|R${metaAcRDMARCAS:.2f}|R${vendaDia:.2f}|"
                                f"R${vendaAcRDMARCAS:.2f}|"
                                f"R${sobrasRD:.2f}|"
                                f"{porcentagemRDMARCAS:.2f}%\n")


