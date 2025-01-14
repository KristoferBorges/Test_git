import time
import datetime
import random
import pandas as pd
from modulo import tryOption
from modulo import tryExclusion
from modulo import tryIsNumber
from modulo import tryOptionConsult
from modulo import tryIsNumber_pecas

# Cores
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
ciano = '\033[36m'
normal = '\033[m'
roxo = '\033[35m'
rosa = '\033[95m'


def dateVerification():
    """
    --> Pedido do cliente: 'Preciso que o sistema pegue o dia de ontem baseado na data atual'.
    --> Sistema: Ele pegará a data atual e fara uma formatação dos dois primeiros números, fazendo com que seja a data
    de ontem.
    Exemplo: 15/03/2021 = 14/03/2021
    :return: Retornará uma string com a data de ontem
    """
    global data_formatada, data
    if len(data) == 0:
        data = datetime.datetime.now()
        data = datetime.datetime.date(data)
        data = data.strftime("%d-%m-%Y")
        data_soma = int(data[:2])
        data_soma = data_soma - 1
        data_soma = str(data_soma)
        if len(data_soma) == 1:
            data_soma = '0' + data_soma
        data = str(data_soma) + data[2:]
        # Data de ontem formatada


titulo = "CONSULTA DE METAS"
tamanho = 44
tamanho_lista = 105
titulo_centralizado = titulo.center(tamanho)
data_formatada = ""

texto_dados = "DADOS ARMAZENADOS!"
texto_dados_centralizado = texto_dados.center(tamanho)

texto_decis = "-DIGITE O NÚMERO CORRESPONDENTE-"
texto_decis_centralizado = texto_decis.center(tamanho)

texto_RDMarcas = roxo + "-LISTA DE RD MARCAS-" + normal
texto_RDMarcas_centralizado = texto_RDMarcas.center(tamanho)

texto_PERFUMARIA = roxo + "-LISTA DE PERFUMARIA-" + normal
texto_PERFUMARIA_centralizado = texto_PERFUMARIA.center(tamanho)

texto_DERMO = roxo + "-LISTA DE DERMO-" + normal
texto_DERMO_centralizado = texto_DERMO.center(tamanho)

texto_RDMarcas_lista_centralizado = texto_RDMarcas.center(tamanho_lista)
texto_PERFUMARIA_lista_centralizado = texto_PERFUMARIA.center(tamanho_lista)
texto_DERMO_lista_centralizado = texto_DERMO.center(tamanho_lista)

# Variável de Teste, deixar falso se não for utilizado
teste = False
activate = True
while activate:
    print('\n\n')
    print(rosa + '$=' * 21 + normal)
    print(roxo + titulo_centralizado + normal)
    print(rosa + '$=' * 21 + normal)
    print('\n')

    # input de decisão
    print(texto_decis_centralizado)
    decis_registro_exclusao_consulta = str(input(yellow + ' [?] - NOVOS REGISTROS [1]\n'
                                                          ' [?] - LIMPAR DADOS ATUAIS [2]\n'
                                                          ' [?] - CONSULTAR LISTAS ATUAIS [3]\n'
                                                          ' [?] - BACKUP DOS DADOS [4]' + red + ' '
                                                          '(COMPUTADOR)\n'
                                                          + yellow + ' --> ' + normal))
    tryOption(decis_registro_exclusao_consulta)
    if decis_registro_exclusao_consulta == '2':
        print('\n')
        print(red + ' [!] - SISTEMA DE EXCLUSÃO\n' + normal)
        print(texto_decis_centralizado)
        decis2_listas = str(input(red + ' [?] - Lista de RD Marcas - [1]\n'
                                        ' [?] - Lista de Perfumaria - [2]\n'
                                        ' [?] - Lista de Dermo - [3]\n'
                                        ' [?] - TODAS AS LISTAS - [4]\n'
                                        ' --> ' + normal + ''))
        tryExclusion(decis2_listas)
        print('\n')
        if decis2_listas == '1':
            confirmacao = str(input(red + ' [!] - Confirme a exclusao dos dados [S/N] ' + normal)).upper().strip()
            if confirmacao == 'S':
                # Exclusão RD MARCAS
                with open("storage/listaRDMARCAS.txt", "w") as listaRDMARCAS:
                    listaRDMARCAS.write("")
                with open("storage/metaAcumuladaRDMARCAS.txt", "w") as metaAcumuladaRDMARCAS:
                    metaAcumuladaRDMARCAS.write("")
                with open("storage/vendaAcumuladaRDMARCAS.txt", "w") as vendaAcumuladaRDMARCAS:
                    vendaAcumuladaRDMARCAS.write("")
                for i in range(3, 0, -1):
                    time.sleep(0.6)
                    print(red, end='')
                    print(f' [!] - CARREGANDO {i}')
                    print(normal, end='')
                print(green + ' [!] - PROCESSO FINALIZADO')

            elif confirmacao != 'S':
                print('\n' + red + ' [!] - PROCESSO INTERROMPIDO')
        elif decis2_listas == '2':
            # Exclusão Perfumaria
            confirmacao = str(input(red + ' [!] - Confirme a exclusao dos dados [S/N] ' + normal)).upper().strip()
            if confirmacao == 'S':
                with open("storage/listaPERFUMARIA.txt", "w") as listaPERFUMARIA:
                    listaPERFUMARIA.write("")
                with open("storage/metaAcumuladaPERFUMARIA.txt", "w") as metaAcumuladaPERFUMARIA:
                    metaAcumuladaPERFUMARIA.write("")
                with open("storage/vendaAcumuladaPERFUMARIA.txt", "w") as vendaAcumuladaPERFUMARIA:
                    vendaAcumuladaPERFUMARIA.write("")
                for i in range(3, 0, -1):
                    time.sleep(0.6)
                    print(red, end='')
                    print(f' [!] - CARREGANDO {i}')
                    print(normal, end='')
                print(green + ' [!] - PROCESSO FINALIZADO')

            elif confirmacao != 'S':
                print('\n' + red + ' [!] - PROCESSO INTERROMPIDO')
        elif decis2_listas == '3':
            # Exclusão Dermo
            confirmacao = str(input(red + ' [!] - Confirme a exclusao dos dados [S/N] ' + normal)).upper().strip()
            if confirmacao == 'S':
                with open("storage/listaDERMO.txt", "w") as listaDERMO:
                    listaDERMO.write("")
                with open("storage/metaAcumuladaDERMO.txt", "w") as metaAcumuladaDERMO:
                    metaAcumuladaDERMO.write("")
                with open("storage/vendaAcumuladaDERMO.txt", "w") as vendaAcumuladaDERMO:
                    vendaAcumuladaDERMO.write("")
                with open("storage/pecaAcumuladaDERMO.txt", "w") as pecaAcumuladaDERMO:
                    pecaAcumuladaDERMO.write("")
                for i in range(3, 0, -1):
                    time.sleep(0.6)
                    print(red, end='')
                    print(f' [!] - CARREGANDO {i}')
                    print(normal, end='')
                print(green + ' [!] - PROCESSO FINALIZADO')

            elif confirmacao != 'S':
                print('\n' + red + ' [!] - PROCESSO INTERROMPIDO')
        elif decis2_listas == '4':
            # Exclusão TODAS AS LISTAS
            confirmacao = str(input(red + ' [!] - Confirme a exclusao dos dados [S/N] ' + normal)).upper().strip()
            if confirmacao == 'S':
                with open("storage/listaRDMARCAS.txt", "w") as listaRDMARCAS:
                    listaRDMARCAS.write("")
                with open("storage/metaAcumuladaRDMARCAS.txt", "w") as metaAcumuladaRDMARCAS:
                    metaAcumuladaRDMARCAS.write("")
                with open("storage/vendaAcumuladaRDMARCAS.txt", "w") as vendaAcumuladaRDMARCAS:
                    vendaAcumuladaRDMARCAS.write("")

                with open("storage/listaPERFUMARIA.txt", "w") as listaPERFUMARIA:
                    listaPERFUMARIA.write("")
                with open("storage/metaAcumuladaPERFUMARIA.txt", "w") as metaAcumuladaPERFUMARIA:
                    metaAcumuladaPERFUMARIA.write("")
                with open("storage/vendaAcumuladaPERFUMARIA.txt", "w") as vendaAcumuladaPERFUMARIA:
                    vendaAcumuladaPERFUMARIA.write("")

                with open("storage/listaDERMO.txt", "w") as listaDERMO:
                    listaDERMO.write("")
                with open("storage/metaAcumuladaDERMO.txt", "w") as metaAcumuladaDERMO:
                    metaAcumuladaDERMO.write("")
                with open("storage/vendaAcumuladaDERMO.txt", "w") as vendaAcumuladaDERMO:
                    vendaAcumuladaDERMO.write("")
                with open("storage/pecaAcumuladaDERMO.txt", "w") as pecaAcumuladaDERMO:
                    pecaAcumuladaDERMO.write("")
                for i in range(3, 0, -1):
                    time.sleep(0.6)
                    print(red, end='')
                    print(f' [!] - CARREGANDO {i}')
                    print(normal, end='')
                print(green + ' [!] - PROCESSO FINALIZADO')

            elif confirmacao != 'S':
                print('\n' + red + ' [!] - PROCESSO INTERROMPIDO')
    elif decis_registro_exclusao_consulta == '1':
        print('\n')
        print(green + ' [!] - SISTEMA DE REGISTRO\n' + normal)
        print(texto_decis_centralizado)
        decis_listas = str(input(yellow + ' [?] - Lista de RD Marcas - [1]\n'
                                          ' [?] - Lista de Perfumaria - [2]\n'
                                          ' [?] - Lista de Dermo - [3]\n'
                                          ' --> ' + normal))
        tryOption(decis_listas)
        if decis_listas == '1':
            # Inputs de dados - RD Marcas
            print('\n')
            print(texto_RDMarcas_centralizado)
            data = str(input(green + ' [?] - Informe a data [dia/mês/ano]: '))
            dateVerification()
            metaDia = float(input(' [?] - Qual a Meta do Dia R$ '))
            vendaDia = float(input(' [?] - Quando Vendeu Hoje R$ '))
            tryIsNumber(metaDia)
            tryIsNumber(vendaDia)
            # Impulso de inserção (Insere de forma rápida os dados de forma aleatória)
            if teste and metaDia == 0 and vendaDia == 0:
                vendaDia = float(random.randint(99, 9999))
                metaDia = random.randint(99, 9999)
            print(normal)
            metaAcRDMARCAS = 0
            vendaAcRDMARCAS = 0
            sobrasRD = 0
            porcentagemRDMARCAS = 0

            # Cálculo de Metas acumuladas
            with open("storage/metaAcumuladaRDMARCAS.txt", "a") as metaAcumuladaRDMARCAS:
                metaAcumuladaRDMARCAS.write(f"{metaDia}\n")
            with open("storage/metaAcumuladaRDMARCAS.txt", "r") as metaAcumuladaRDMARCAS:
                linhas = metaAcumuladaRDMARCAS.readlines()

            for linha in linhas:
                metaAcRDMARCAS = metaAcRDMARCAS + float(linha.strip())
            print(yellow + f" [!] - META ACUMULADA = ", end='')
            print(rosa + f"R$ {metaAcRDMARCAS:.2f}" + normal)

            # Cálculo de Vendas acumuladas
            with open("storage/vendaAcumuladaRDMARCAS.txt", "a") as vendaAcumuladaRDMARCAS:
                vendaAcumuladaRDMARCAS.write(f"{vendaDia}\n")
            with open("storage/vendaAcumuladaRDMARCAS.txt", "r") as vendaAcumuladaRDMARCAS:
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
            with open("storage/listaRDMARCAS.txt", "a") as listaRDMARCAS:
                listaRDMARCAS.write(f"{data}|R${metaDia:.2f}|R${metaAcRDMARCAS:.2f}|R${vendaDia:.2f}|"
                                    f"R${vendaAcRDMARCAS:.2f}|"
                                    f"R${sobrasRD:.2f}|"
                                    f"{porcentagemRDMARCAS:.2f}%\n")
        elif decis_listas == '2':
            # Inputs de dados - RD Perfumaria
            print('\n')
            print(texto_PERFUMARIA_centralizado)
            data = str(input(green + ' [?] - Informe a data [dia/mês/ano]: '))
            dateVerification()
            metaDia = float(input(' [?] - Qual a Meta do Dia R$ '))
            vendaDia = float(input(' [?] - Quando Vendeu Hoje R$ '))
            tryIsNumber(metaDia)
            tryIsNumber(vendaDia)
            # Impulso de inserção (Insere de forma rápida os dados de forma aleatória)
            if teste and metaDia == 0 and vendaDia == 0:
                vendaDia = float(random.randint(99, 9999))
                metaDia = random.randint(99, 9999)
            print(normal)
            metaAcPERFUMARIA = 0
            vendaAcPERFUMARIA = 0
            sobrasPerfumaria = 0
            porcentagemPERFUMARIA = 0

            # Cálculo de Metas acumuladas
            with open("storage/metaAcumuladaPERFUMARIA.txt", "a") as metaAcumuladaPERFUMARIA:
                metaAcumuladaPERFUMARIA.write(f"{metaDia}\n")
            with open("storage/metaAcumuladaPERFUMARIA.txt", "r") as metaAcumuladaPERFUMARIA:
                linhas = metaAcumuladaPERFUMARIA.readlines()

            for linha in linhas:
                metaAcPERFUMARIA = metaAcPERFUMARIA + float(linha.strip())
            print(yellow + f" [!] - META ACUMULADA = ", end='')
            print(rosa + f"R$ {metaAcPERFUMARIA:.2f}" + normal)

            # Cálculo de Vendas acumuladas
            with open("storage/vendaAcumuladaPERFUMARIA.txt", "a") as vendaAcumuladaPERFUMARIA:
                vendaAcumuladaPERFUMARIA.write(f"{vendaDia}\n")
            with open("storage/vendaAcumuladaPERFUMARIA.txt", "r") as vendaAcumuladaPERFUMARIA:
                linhas2 = vendaAcumuladaPERFUMARIA.readlines()

            for linha in linhas2:
                vendaAcPERFUMARIA = vendaAcPERFUMARIA + float(linha.strip())
            print(yellow + f" [!] - VENDA ACUMULADA = ", end='')
            print(rosa + f"R$ {vendaAcPERFUMARIA:.2f}" + normal)

            # Cálculo de porcentagem
            if vendaAcPERFUMARIA < metaAcPERFUMARIA:
                sobrasPerfumaria = (metaAcPERFUMARIA - vendaAcPERFUMARIA)
            elif metaAcPERFUMARIA < vendaAcPERFUMARIA:
                sobrasPerfumaria = (vendaAcPERFUMARIA - metaAcPERFUMARIA)
            else:
                sobrasPerfumaria = 0
            porcentagemPERFUMARIA = (vendaAcPERFUMARIA / metaAcPERFUMARIA) * 100
            print(yellow + f" [!] - PORCENTAGEM ACUMULADA = ", end='')
            print(rosa + f"{porcentagemPERFUMARIA:.2f}%" + normal)
            print('\n')
            print(rosa + '=-' * 21 + normal)
            print(roxo + texto_dados_centralizado + normal)
            print(rosa + '=-' * 21 + normal)
            # Inserção de dados
            with open("storage/listaPERFUMARIA.txt", "a") as listaPERFUMARIA:
                listaPERFUMARIA.write(f"{data} | R${metaDia:.2f} | R${metaAcPERFUMARIA:.2f} | R${vendaDia:.2f} |"
                                      f" R${vendaAcPERFUMARIA:.2f} | "
                                      f" R${sobrasPerfumaria :.2f} | "
                                      f"{porcentagemPERFUMARIA:.2f}%\n")
        elif decis_listas == '3':
            # Inputs de dados - RD Dermo
            print('\n')
            print(texto_DERMO_centralizado)
            data = str(input(green + ' [?] - Informe a data [dia/mês/ano]: '))
            dateVerification()
            metaDia = float(input(' [?] - Qual a Meta do Dia R$ '))
            vendaDia = float(input(' [?] - Quando Vendeu Hoje R$ '))
            pecaDia = str(input(' [?] - Quantas peças Vendeu Hoje: '))
            if len(pecaDia) == 0:
                pecaDia = int(0)
            tryIsNumber(metaDia)
            tryIsNumber(vendaDia)
            tryIsNumber_pecas(pecaDia)
            # Impulso de inserção (Insere de forma rápida os dados de forma aleatória)
            if teste and metaDia == 0 and vendaDia == 0 and pecaDia == '0':
                vendaDia = float(random.randint(99, 9999))
                metaDia = random.randint(99, 9999)
                pecaDia = random.randint(5, 60)
            print(normal)
            metaAcDERMO = 0
            vendaAcDERMO = 0
            pecaAc = 0
            sobrasDermo = 0
            porcentagemDERMO = 0

            # Cálculo de Metas acumuladas
            with open("storage/metaAcumuladaDERMO.txt", "a") as metaAcumuladaDERMO:
                metaAcumuladaDERMO.write(f"{metaDia}\n")
            with open("storage/metaAcumuladaDERMO.txt", "r") as metaAcumuladaDERMO:
                linhas = metaAcumuladaDERMO.readlines()

            for linha in linhas:
                metaAcDERMO = metaAcDERMO + float(linha.strip())
            print(yellow + f" [!] - META ACUMULADA = ", end='')
            print(rosa + f"R$ {metaAcDERMO:.2f}" + normal)

            # Cálculo de Vendas acumuladas
            with open("storage/vendaAcumuladaDERMO.txt", "a") as vendaAcumuladaDERMO:
                vendaAcumuladaDERMO.write(f"{vendaDia}\n")
            with open("storage/vendaAcumuladaDERMO.txt", "r") as vendaAcumuladaDERMO:
                linhas2 = vendaAcumuladaDERMO.readlines()

            for linha in linhas2:
                vendaAcDERMO = vendaAcDERMO + float(linha.strip())
            print(yellow + f" [!] - VENDA ACUMULADA = ", end='')
            print(rosa + f"R$ {vendaAcDERMO:.2f}" + normal)

            # Cálculo de Peças acumuladas
            with open("storage/pecaAcumuladaDERMO.txt", "a") as pecaAcumuladaDERMO:
                pecaAcumuladaDERMO.write(f'{pecaDia}\n')
            with open("storage/pecaAcumuladaDERMO.txt", "r") as pecaAcumuladaDERMO:
                linhasPeca = pecaAcumuladaDERMO.readlines()

            for linha in linhasPeca:
                pecaAc = pecaAc + int(linha.strip())
            print(yellow + f" [!] - PEÇAS ACUMULADAS = ", end='')
            print(rosa + f"{pecaAc} Unidades" + normal)

            # Cálculo de porcentagem
            if vendaAcDERMO < metaAcDERMO:
                sobrasDermo = (metaAcDERMO - vendaAcDERMO)
            elif metaAcDERMO < vendaAcDERMO:
                sobrasDermo = (vendaAcDERMO - metaAcDERMO)
            else:
                sobrasDermo = 0
            porcentagemDERMO = (vendaAcDERMO / metaAcDERMO) * 100
            print(yellow + f" [!] - PORCENTAGEM ACUMULADA = ", end='')
            print(rosa + f"{porcentagemDERMO:.2f}%" + normal)
            print('\n')
            print(rosa + '=-' * 21 + normal)
            print(roxo + texto_dados_centralizado + normal)
            print(rosa + '=-' * 21 + normal)
            # Inserção de dados
            with open("storage/listaDERMO.txt", "a") as listaDERMO:
                listaDERMO.write(f"{data} | R${metaDia:.2f} | R${metaAcDERMO:.2f} | R${vendaDia:.2f} |"
                                 f" R${vendaAcDERMO:.2f} | "
                                 f" {pecaAc}Un | "
                                 f" R${sobrasDermo:.2f} | "
                                 f"{porcentagemDERMO:.2f}%\n")
    elif decis_registro_exclusao_consulta == '3':
        print('\n')
        print(texto_decis_centralizado)
        decis_consulta = str(input((yellow + " [?] - CONSULTAR LISTA DE RD MARCAS [1]\n"
                                             " [?] - CONSULTAR LISTA DE PERFUMARIA [2]\n"
                                             " [?] - CONSULTAR LISTA DE DERMO [3]\n"
                                             " [?] - CONSULTAR TODAS AS LISTAS [4]\n --> " + normal)))
        tryOptionConsult(decis_consulta)
        if decis_consulta == '1':
            print('¨¨' * 46)
            print(texto_RDMarcas_lista_centralizado)
            print(green + '{:>10}{:>13}{:>15}{:>12}{:>15}{:>11}{:>14}'.format('DATA', 'META', 'META.AC', 'VENDAS',
                                                                              'VENDAS.AC', 'SOBRAS', 'P' + normal))
            with open("storage/listaRDMARCAS.txt", "r") as listaRDMARCAS:
                linhas3 = listaRDMARCAS.readlines()
            for linha in linhas3:
                dado = linha.split('|')
                for i in dado:
                    print(f'{i:>13}', end='')
            print()
            print('¨¨' * 46)
        elif decis_consulta == '2':
            print('¨¨' * 46)
            print(texto_PERFUMARIA_lista_centralizado)
            print(green + '{:>10}{:>13}{:>15}{:>12}{:>15}{:>11}{:>14}'.format('DATA', 'META', 'META.AC', 'VENDAS',
                                                                              'VENDAS.AC', 'SOBRAS', 'P' + normal))
            with open("storage/listaPERFUMARIA.txt", "r") as listaPERFUMARIA:
                linhas3 = listaPERFUMARIA.readlines()
            for linha in linhas3:
                dado = linha.split('|')
                for i in dado:
                    print(f'{i:>13}', end='')
            print()
            print('¨¨' * 46)
        elif decis_consulta == '3':
            print('¨¨' * 52)
            print(texto_DERMO_lista_centralizado)
            print(green + '{:>10}{:>13}{:>15}{:>12}{:>14}{:>13}{:>12}{:>14}'.format('DATA', 'META',
                                                                                    'META.AC', 'VENDAS', 'VENDAS.AC',
                                                                                    'PECA.AC', 'SOBRAS', 'P' + normal))
            with open("storage/listaDERMO.txt", "r") as listaDERMO:
                linhas3 = listaDERMO.readlines()
            for linha in linhas3:
                dado = linha.split('|')
                for i in dado:
                    print(f'{i:>13}', end='')
            print()
            print('¨¨' * 52)
        elif decis_consulta == '4':
            print('¨¨' * 52)
            print('¨¨' * 52)
            print(texto_RDMarcas_lista_centralizado)
            print(green + '{:>10}{:>13}{:>15}{:>12}{:>15}{:>11}{:>14}'.format('DATA', 'META', 'META.AC', 'VENDAS',
                                                                              'VENDAS.AC', 'SOBRAS', 'P' + normal))
            with open("storage/listaRDMARCAS.txt", "r") as listaRDMARCAS:
                linhas3 = listaRDMARCAS.readlines()
            for linha in linhas3:
                dado = linha.split('|')
                for i in dado:
                    print(f'{i:>13}', end='')
            print()
            print('¨¨' * 52)
            print('¨¨' * 52)
            print(texto_PERFUMARIA_lista_centralizado)
            print(green + '{:>10}{:>13}{:>15}{:>12}{:>15}{:>11}{:>14}'.format('DATA', 'META', 'META.AC', 'VENDAS',
                                                                              'VENDAS.AC', 'SOBRAS', 'P' + normal))
            with open("storage/listaPERFUMARIA.txt", "r") as listaPERFUMARIA:
                linhas3 = listaPERFUMARIA.readlines()
            for linha in linhas3:
                dado = linha.split('|')
                for i in dado:
                    print(f'{i:>13}', end='')
            print()
            print('¨¨' * 52)
            print('¨¨' * 52)
            print(texto_DERMO_lista_centralizado)
            print(green + '{:>10}{:>13}{:>15}{:>12}{:>14}{:>13}{:>12}{:>14}'.format('DATA', 'META', 'META.AC', 'VENDAS',
                                                                                    'VENDAS.AC', 'PECA.AC', 'SOBRAS',
                                                                                    'P' + normal))
            with open("storage/listaDERMO.txt", "r") as listaDERMO:
                linhas3 = listaDERMO.readlines()
            for linha in linhas3:
                dado = linha.split('|')
                for i in dado:
                    print(f'{i:>13}', end='')
            print()
            print('¨¨' * 52)
            print('¨¨' * 52)
    elif decis_registro_exclusao_consulta == '4':
        # print(red + '[!] - OPÇÃO DESATIVADA POR QUESTÕES TÉCNICAS (19/05/2023) - SEM PREVISÃO DE RETORNO!')
        print(green + ' [!] - TODOS OS DADOS SERÃO GUARDADOS!')
        time.sleep(0.5)
        # BACKUP DE TODAS AS LISTAS
        confirmacao = str(input(green + ' [!] - Confirma o Backup dos dados [S/N] ' + normal)).upper().strip()
        if confirmacao == 'S':
            try:
                # Pega a data formatada no dia atual
                hora = datetime.datetime.now()
                date = datetime.datetime.now()

                date = datetime.datetime.date(date)
                datahoje = date.strftime("%d-%m-%Y")
                horahoje = hora.strftime("%H;%M;%S")
                nomeArquivoRD = f"BackupRDMARCAS-{datahoje}-{horahoje}"
                nomeArquivoPERFUMARIA = f"BackupPERFUMARIA-{datahoje}-{horahoje}"
                nomeArquivoDERMO = f"BackupDERMO-{datahoje}-{horahoje}"

                # Separa as informações em formato pandas
                tabela_RDMARCAS = pd.read_csv("storage/listaRDMARCAS.txt", sep="|")
                tabela_PERFUMARIA = pd.read_csv("storage/listaPERFUMARIA.txt", sep="|")
                tabela_DERMO = pd.read_csv("storage/listaDERMO.txt", sep="|")

                # Converte em arquivos Excel
                tabela_RDMARCAS.to_excel(fr"backup\RDMARCAS\{nomeArquivoRD}.xlsx", index=False)
                tabela_PERFUMARIA.to_excel(fr"backup\PERFUMARIA\{nomeArquivoPERFUMARIA}.xlsx", index=False)
                tabela_DERMO.to_excel(fr"backup\DERMO\{nomeArquivoDERMO}.xlsx", index=False)

                # Mensagem de finalização
                print(green + ' [!] - PROCESSO FINALIZADO')
                time.sleep(1)
            except PermissionError:
                print('\n' + red + ' [!] - PROCESSO INTERROMPIDO (ARQUIVO ABERTO)')
            except TypeError:
                print('\n' + red + ' [!] - PROCESSO INTERROMPIDO (DADOS NÃO COMPATÍVEIS)')
            except ValueError:
                print('\n' + red + ' [!] - PROCESSO INTERROMPIDO (VALORES AUSENTES OU NÃO COMPATÍVEIS)')
            except FileNotFoundError:
                print('\n' + red + ' [!] - PROCESSO INTERROMPIDO (DIRETÓRIO NÃO ENCONTRADO)')

        elif confirmacao != 'S':
            print('\n' + red + ' [!] - PROCESSO INTERROMPIDO')
