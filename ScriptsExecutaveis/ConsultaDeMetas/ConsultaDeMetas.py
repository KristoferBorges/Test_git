import datetime
import random
import pandas as pd
import openpyxl
from time import sleep
from modulo import tryOption
from modulo import tryOptionList
from modulo import tryExclusion
from modulo import tryOptionBackup
from modulo import capturaDeValoresMetaDia
from modulo import capturaDeValoresVendaDia
from modulo import capturaDeValoresPecaDia
from modulo import abatimento
from modulo import tryOptionConsult

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
    Teste ON: Caso a variável {teste} for verdadeira, o sistema pegará aleatóriamente um número entre 1 e 28 para
    preencher o dia.
    :return: Retornará uma string com a data de ontem
    """
    global data_formatada, data
    if len(data) == 0:
        data = datetime.datetime.now()
        data = datetime.datetime.date(data)
        data = data.strftime("%d-%m-%Y")
        data_soma = int(data[:2])
        data_soma = data_soma - 1
        if teste:
            data_soma = random.randint(1, 28)
        data_soma = str(data_soma)
        if len(data_soma) == 1:
            data_soma = '0' + data_soma
        data = str(data_soma) + data[2:]
        # Data de ontem formatada


# Variável de Teste, deixar falso se não for utilizado
teste = False
if teste:
    teste_titulo = red + "(TESTE ON)" + normal
else:
    teste_titulo = ""
titulo = f"CONSULTA DE METAS {teste_titulo}" + ciano + " v1.7.2"
tamanho = 43
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

opcao = tuple([normal + "[1]", normal + "[2]", normal + "[3]", normal + "[4]", normal + "[5]", normal + "[6]"])
while True:
    print('\n\n')
    print(rosa + '$=' * 21 + normal)
    print(roxo + titulo_centralizado)
    print(rosa + '$=' * 21 + normal)
    print('\n')

    # input de decisão
    print(texto_decis_centralizado)
    decis_registro_exclusao_consulta = str(input(yellow + f' [?] - NOVOS REGISTROS {opcao[0]}\n' + yellow +
                                                 f' [?] - LIMPAR DADOS ATUAIS {opcao[1]}\n' + yellow +
                                                 f' [?] - CONSULTAR LISTAS ATUAIS {opcao[2]}\n' + yellow +
                                                 f' [?] - BACKUP DOS DADOS {opcao[3]}\n' + yellow +
                                                 f' [?] - VERIFICAR INTEGRIDADE DOS DADOS {opcao[4]}\n'
                                                 + yellow +
                                                 f' [?] - SAIR DO PROGRAMA {opcao[5]}\n' + yellow +
                                                 ' --> ' + normal))
    tryOption(decis_registro_exclusao_consulta)
    if decis_registro_exclusao_consulta == '2':
        print('\n')
        print(red + ' [!] - SISTEMA DE EXCLUSÃO\n' + normal)
        print(texto_decis_centralizado)
        decis2_listas = str(input(red + f' [?] - Lista de RD Marcas - {opcao[0]}\n' + red +
                                  f' [?] - Lista de Perfumaria - {opcao[1]}\n' + red +
                                  f' [?] - Lista de Dermo - {opcao[2]}\n' + red +
                                  f' [?] - TODAS AS LISTAS - {opcao[3]}\n' + red +
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
                    sleep(0.6)
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
                    sleep(0.6)
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
                    sleep(0.6)
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
                    sleep(0.6)
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
        decis_listas = str(input(yellow + f' [?] - Lista de RD Marcas - {opcao[0]}\n' + yellow +
                                 f' [?] - Lista de Perfumaria - {opcao[1]}\n' + yellow +
                                 f' [?] - Lista de Dermo - {opcao[2]}\n' + yellow +
                                 ' --> ' + normal))
        tryOptionList(decis_listas)
        if decis_listas == '1':
            # Inputs de dados - RD Marcas
            print('\n')
            print(texto_RDMarcas_centralizado)
            data = str(input(green + ' [?] - Informe a data [dia/mês/ano]: '))
            dateVerification()
            metaDia = capturaDeValoresMetaDia()
            vendaDia = capturaDeValoresVendaDia()
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
            if vendaAcRDMARCAS != 0 and metaAcRDMARCAS != 0:
                porcentagemRDMARCAS = (vendaAcRDMARCAS / metaAcRDMARCAS) * 100
            print(yellow + f" [!] - PORCENTAGEM ACUMULADA = ", end='')
            print(rosa + f"{porcentagemRDMARCAS:.2f}%" + normal)
            print('\n')
            print(rosa + '=-' * 21 + normal)
            print(roxo + texto_dados_centralizado + normal)
            print(rosa + '=-' * 21 + normal)
            # Análise alcance de metas
            devedor = abatimento(metaAcRDMARCAS, vendaAcRDMARCAS)
            # Inserção de dados
            with open("storage/listaRDMARCAS.txt", "a") as listaRDMARCAS:
                listaRDMARCAS.write(f"{data}|R${metaDia:.2f}|R${metaAcRDMARCAS:.2f}|R${vendaDia:.2f}|"
                                    f"R${vendaAcRDMARCAS:.2f}|"
                                    f"{devedor}R${sobrasRD:.2f}|"
                                    f"{porcentagemRDMARCAS:.2f}%\n")
        elif decis_listas == '2':
            # Inputs de dados - RD Perfumaria
            print('\n')
            print(texto_PERFUMARIA_centralizado)
            data = str(input(green + ' [?] - Informe a data [dia/mês/ano]: '))
            dateVerification()
            metaDia = capturaDeValoresMetaDia()
            vendaDia = capturaDeValoresVendaDia()
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
            if vendaAcPERFUMARIA != 0 and metaAcPERFUMARIA != 0:
                porcentagemPERFUMARIA = (vendaAcPERFUMARIA / metaAcPERFUMARIA) * 100
            print(yellow + f" [!] - PORCENTAGEM ACUMULADA = ", end='')
            print(rosa + f"{porcentagemPERFUMARIA:.2f}%" + normal)
            print('\n')
            print(rosa + '=-' * 21 + normal)
            print(roxo + texto_dados_centralizado + normal)
            print(rosa + '=-' * 21 + normal)
            # Análise alcance de metas
            devedor = abatimento(metaAcPERFUMARIA, vendaAcPERFUMARIA)
            # Inserção de dados
            with open("storage/listaPERFUMARIA.txt", "a") as listaPERFUMARIA:
                listaPERFUMARIA.write(f"{data} | R${metaDia:.2f} | R${metaAcPERFUMARIA:.2f} | R${vendaDia:.2f} |"
                                      f" R${vendaAcPERFUMARIA:.2f} | "
                                      f" {devedor}R${sobrasPerfumaria :.2f} |"
                                      f"{porcentagemPERFUMARIA:.2f}%\n")
        elif decis_listas == '3':
            # Inputs de dados - RD Dermo
            print('\n')
            print(texto_DERMO_centralizado)
            data = str(input(green + ' [?] - Informe a data [dia/mês/ano]: '))
            dateVerification()
            metaDia = capturaDeValoresMetaDia()
            vendaDia = capturaDeValoresVendaDia()
            pecaDia = capturaDeValoresPecaDia()
            # Impulso de inserção (Insere de forma rápida os dados de forma aleatória)
            if teste and metaDia == 0 and vendaDia == 0:
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
            if vendaAcDERMO != 0 and metaAcDERMO != 0:
                porcentagemDERMO = (vendaAcDERMO / metaAcDERMO) * 100
            print(yellow + f" [!] - PORCENTAGEM ACUMULADA = ", end='')
            print(rosa + f"{porcentagemDERMO:.2f}%" + normal)
            print('\n')
            print(rosa + '=-' * 21 + normal)
            print(roxo + texto_dados_centralizado + normal)
            print(rosa + '=-' * 21 + normal)
            # Análise alcance de metas
            devedor = abatimento(metaAcDERMO, vendaAcDERMO)
            # Inserção de dados
            with open("storage/listaDERMO.txt", "a") as listaDERMO:
                listaDERMO.write(f"{data} | R${metaDia:.2f} | R${metaAcDERMO:.2f} | R${vendaDia:.2f} |"
                                 f" R${vendaAcDERMO:.2f} | "
                                 f" {pecaAc}Un | "
                                 f" {devedor}R${sobrasDermo:.2f} | "
                                 f"{porcentagemDERMO:.2f}%\n")
    elif decis_registro_exclusao_consulta == '3':
        print('\n')
        print(texto_decis_centralizado)
        decis_consulta = str(input((yellow + f" [?] - CONSULTAR LISTA DE RD MARCAS {opcao[0]}\n" + yellow +
                                    f" [?] - CONSULTAR LISTA DE PERFUMARIA {opcao[1]}\n" + yellow +
                                    f" [?] - CONSULTAR LISTA DE DERMO {opcao[2]}\n" + yellow +
                                    f" [?] - CONSULTAR TODAS AS LISTAS {opcao[3]}\n" + yellow +
                                    " --> " + normal)))
        tryOptionConsult(decis_consulta)
        if decis_consulta == '1':
            print('¨¨' * 46)
            print(texto_RDMarcas_lista_centralizado)
            print(green + '{:>10}{:>15}{:>16}{:>14}{:>16}{:>11}{:>15}'.format('DATA', 'META', 'META.AC', 'VENDAS',
                                                                              'VENDAS.AC', 'SOBRAS', 'P' + normal))
            with open("storage/listaRDMARCAS.txt", "r") as listaRDMARCAS:
                linhas3 = listaRDMARCAS.readlines()
            for linha in linhas3:
                dado = linha.split('|')
                for i in dado:
                    print(f'{i:>14}', end='')
            print()
            print('¨¨' * 46)
        elif decis_consulta == '2':
            print('¨¨' * 46)
            print(texto_PERFUMARIA_lista_centralizado)
            print(green + '{:>10}{:>15}{:>15}{:>14}{:>15}{:>12}{:>16}'.format('DATA', 'META', 'META.AC', 'VENDAS',
                                                                              'VENDAS.AC', 'SOBRAS', 'P' + normal))
            with open("storage/listaPERFUMARIA.txt", "r") as listaPERFUMARIA:
                linhas3 = listaPERFUMARIA.readlines()
            for linha in linhas3:
                dado = linha.split('|')
                for i in dado:
                    print(f'{i:>14}', end='')
            print()
            print('¨¨' * 46)
        elif decis_consulta == '3':
            print('¨¨' * 52)
            print(texto_DERMO_lista_centralizado)
            print(green + '{:>10}{:>14}{:>16}{:>14}{:>14}{:>16}{:>12}{:>15}'.format('DATA', 'META',
                                                                                    'META.AC', 'VENDAS', 'VENDAS.AC',
                                                                                    'PECA.AC', 'SOBRAS', 'P' + normal))
            with open("storage/listaDERMO.txt", "r") as listaDERMO:
                linhas3 = listaDERMO.readlines()
            for linha in linhas3:
                dado = linha.split('|')
                for i in dado:
                    print(f'{i:>14}', end='')
            print()
            print('¨¨' * 52)
        elif decis_consulta == '4':
            print('¨¨' * 52)
            print('¨¨' * 52)
            print(texto_RDMarcas_lista_centralizado)
            print(green + '{:>10}{:>15}{:>16}{:>14}{:>16}{:>11}{:>15}'.format('DATA', 'META', 'META.AC', 'VENDAS',
                                                                              'VENDAS.AC', 'SOBRAS', 'P' + normal))
            with open("storage/listaRDMARCAS.txt", "r") as listaRDMARCAS:
                linhas3 = listaRDMARCAS.readlines()
            for linha in linhas3:
                dado = linha.split('|')
                for i in dado:
                    print(f'{i:>14}', end='')
            print()
            print('¨¨' * 52)
            print('¨¨' * 52)
            print(texto_PERFUMARIA_lista_centralizado)
            print(green + '{:>10}{:>15}{:>15}{:>14}{:>15}{:>12}{:>16}'.format('DATA', 'META', 'META.AC', 'VENDAS',
                                                                              'VENDAS.AC', 'SOBRAS', 'P' + normal))
            with open("storage/listaPERFUMARIA.txt", "r") as listaPERFUMARIA:
                linhas3 = listaPERFUMARIA.readlines()
            for linha in linhas3:
                dado = linha.split('|')
                for i in dado:
                    print(f'{i:>14}', end='')
            print()
            print('¨¨' * 52)
            print('¨¨' * 52)
            print(texto_DERMO_lista_centralizado)
            print(green + '{:>10}{:>14}{:>16}{:>14}{:>14}{:>16}{:>12}{:>15}'.format('DATA', 'META',
                                                                                    'META.AC', 'VENDAS', 'VENDAS.AC',
                                                                                    'PECA.AC', 'SOBRAS', 'P' + normal))
            with open("storage/listaDERMO.txt", "r") as listaDERMO:
                linhas3 = listaDERMO.readlines()
            for linha in linhas3:
                dado = linha.split('|')
                for i in dado:
                    print(f'{i:>14}', end='')
            print()
            print('¨¨' * 52)
            print('¨¨' * 52)
    elif decis_registro_exclusao_consulta == '4':
        print('\n')
        print(green + ' [!] - SISTEMA DE BACKUP')
        print('\n')
        print(normal + f'{texto_decis_centralizado}')
        print(yellow + f' [?] - LISTA RD MARCAS {opcao[0]}')
        print(yellow + f' [?] - LISTA PERFUMARIA {opcao[1]}')
        print(yellow + f' [?] - LISTA DERMO {opcao[2]}')
        print(yellow + f' [?] - TODAS AS LISTAS {opcao[3]}')
        opcaoBackup = str(input(' --> '))
        print('\n')
        tryOptionBackup(opcaoBackup)
        if opcaoBackup == '1':
            print(green + ' [!] - TODOS OS DADOS SERÃO GUARDADOS!')
            sleep(0.5)
            confirmacao = str(input(green + ' [!] - Confirma o Backup dos dados [S/N] ' + normal)).upper().strip()
            if confirmacao == 'S':
                try:
                    hora = datetime.datetime.now()
                    date = datetime.datetime.now()
                    date = datetime.datetime.date(date)
                    datahoje = date.strftime("%d-%m-%Y")
                    horahoje = hora.strftime("%H;%M;%S")
                    nomeArquivoRD = f"BackupRDMARCAS-{datahoje}-{horahoje}"

                    # Lê o arquivo CSV sem o cabeçalho
                    tabela_RDMARCAS = pd.read_csv("storage/listaRDMARCAS.txt", sep="|", header=None)

                    colunas = ["Data", "Meta", "Meta.AC", "Venda", "Venda.AC", "Sobras", "P"]

                    # Adiciona a primeira linha como cabeçalho
                    tabela_RDMARCAS.columns = colunas

                    # Concatena a primeira linha com o DataFrame original, ignorando o índice
                    tabela_RDMARCAS = pd.concat([tabela_RDMARCAS], ignore_index=True)

                    with pd.ExcelWriter(fr"backup/RDMARCAS/{nomeArquivoRD}.xlsx") as writer:
                        tabela_RDMARCAS.to_excel(writer, index=False, sheet_name='RDMARCAS')

                    print(green + ' [!] - PROCESSO FINALIZADO')
                    sleep(1)
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
        elif opcaoBackup == '2':
            print(green + ' [!] - TODOS OS DADOS SERÃO GUARDADOS!')
            sleep(0.5)
            # BACKUP DA LISTA PERFUMARIA
            confirmacao = str(input(green + ' [!] - Confirma o Backup dos dados [S/N] ' + normal)).upper().strip()
            if confirmacao == 'S':
                try:
                    hora = datetime.datetime.now()
                    date = datetime.datetime.now()
                    date = datetime.datetime.date(date)
                    datahoje = date.strftime("%d-%m-%Y")
                    horahoje = hora.strftime("%H;%M;%S")
                    nomeArquivoPERFUMARIA = f"BackupPERFUMARIA-{datahoje}-{horahoje}"

                    # Lê o arquivo CSV sem o cabeçalho
                    tabela_PERFUMARIA = pd.read_csv("storage/listaPERFUMARIA.txt", sep="|", header=None)

                    colunas = ["Data", "Meta", "Meta.AC", "Venda", "Venda.AC", "Sobras", "P"]

                    # Adiciona a primeira linha como cabeçalho
                    tabela_PERFUMARIA.columns = colunas

                    # Concatena a primeira linha com o DataFrame original, ignorando o índice
                    tabela_PERFUMARIA = pd.concat([tabela_PERFUMARIA], ignore_index=True)

                    with pd.ExcelWriter(fr"backup/PERFUMARIA/{nomeArquivoPERFUMARIA}.xlsx") as writer:
                        tabela_PERFUMARIA.to_excel(writer, index=False, sheet_name='PERFUMARIA')

                    print(green + ' [!] - PROCESSO FINALIZADO')
                    sleep(1)
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
        elif opcaoBackup == '3':
            print(green + ' [!] - TODOS OS DADOS SERÃO GUARDADOS!')
            sleep(0.5)
            # BACKUP DA LISTA DERMO
            confirmacao = str(input(green + ' [!] - Confirma o Backup dos dados [S/N] ' + normal)).upper().strip()
            if confirmacao == 'S':
                try:
                    hora = datetime.datetime.now()
                    date = datetime.datetime.now()
                    date = datetime.datetime.date(date)
                    datahoje = date.strftime("%d-%m-%Y")
                    horahoje = hora.strftime("%H;%M;%S")
                    nomeArquivoDERMO = f"BackupDERMO-{datahoje}-{horahoje}"

                    # Lê o arquivo CSV sem o cabeçalho
                    tabela_DERMO = pd.read_csv("storage/listaDERMO.txt", sep="|", header=None)

                    colunas_dermo = ["Data", "Meta", "Meta.AC", "Venda", "Venda.AC", "Pecas", "Sobras", "P"]

                    # Adiciona a primeira linha como cabeçalho
                    tabela_DERMO.columns = colunas_dermo

                    # Concatena a primeira linha com o DataFrame original, ignorando o índice
                    tabela_DERMO = pd.concat([tabela_DERMO], ignore_index=True)

                    with pd.ExcelWriter(fr"backup/DERMO/{nomeArquivoDERMO}.xlsx") as writer:
                        tabela_DERMO.to_excel(writer, index=False, sheet_name='DERMO')

                    print(green + ' [!] - PROCESSO FINALIZADO')
                    sleep(1)
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
        elif opcaoBackup == '4':
            print(green + ' [!] - TODOS OS DADOS SERÃO GUARDADOS!')
            sleep(0.5)
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
                    tabela_RDMARCAS = pd.read_csv("storage/listaRDMARCAS.txt", sep="|", header=None)
                    tabela_PERFUMARIA = pd.read_csv("storage/listaPERFUMARIA.txt", sep="|", header=None)
                    tabela_DERMO = pd.read_csv("storage/listaDERMO.txt", sep="|", header=None)

                    # Define as colunas específicas
                    colunas = ["Data", "Meta", "Meta.AC", "Venda", "Venda.AC", "Sobras", "P"]
                    colunas_dermo = ["Data", "Meta", "Meta.AC", "Venda", "Venda.AC", "Pecas", "Sobras", "P"]

                    # Renomeia as colunas nas tabelas
                    tabela_RDMARCAS.columns = colunas
                    tabela_PERFUMARIA.columns = colunas
                    tabela_DERMO.columns = colunas_dermo

                    # Converte em arquivos Excel e coloca na pasta requisitada
                    tabela_RDMARCAS = pd.concat([tabela_RDMARCAS], ignore_index=True)
                    tabela_PERFUMARIA = pd.concat([tabela_PERFUMARIA], ignore_index=True)
                    tabela_DERMO = pd.concat([tabela_DERMO], ignore_index=True)

                    with pd.ExcelWriter(fr"backup/RDMARCAS/{nomeArquivoRD}.xlsx") as writer:
                        tabela_RDMARCAS.to_excel(writer, index=False, sheet_name='RDMARCAS')
                    with pd.ExcelWriter(fr"backup/PERFUMARIA/{nomeArquivoPERFUMARIA}.xlsx") as writer:
                        tabela_PERFUMARIA.to_excel(writer, index=False, sheet_name='PERFUMARIA')
                    with pd.ExcelWriter(fr"backup/DERMO/{nomeArquivoDERMO}.xlsx") as writer:
                        tabela_DERMO.to_excel(writer, index=False, sheet_name='DERMO')
                    # Mensagem de finalização
                    print(green + ' [!] - PROCESSO FINALIZADO')
                    sleep(1)
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
    elif decis_registro_exclusao_consulta == '5':
        print('\n')
        print(green + ' [!] - SISTEMA DE ANÁLISE')
        print('\n')


        def check_data_RD():
            try:
                with open("storage/metaAcumuladaRDMARCAS.txt", "r") as arquivoRDMetas:
                    metas = arquivoRDMetas.readlines()
                    quantidade_linhas_meta = len(metas)
                with open("storage/vendaAcumuladaRDMARCAS.txt", "r") as arquivoRDVendas:
                    vendas = arquivoRDVendas.readlines()
                    quantidade_linhas_venda = len(vendas)

                metas = [float(meta.strip()) for meta in metas]
                vendas = [float(venda.strip()) for venda in vendas]

                total_metas = sum(metas)
                total_vendas = sum(vendas)
                sobra = abs(total_metas - total_vendas)
                porcentagem = (total_vendas / total_metas) * 100

                # Análise alcance de metas (Opção de integridade)
                devedor_abatimento_rd = abatimento(total_metas, total_vendas)
                if total_vendas < total_metas:
                    situacao = red
                else:
                    situacao = normal

                print(rosa + "Dados da lista de RD Marcas:" + normal)
                print(yellow + " [!] - Meta acumulada:" + normal + f"R$ {total_metas:.2f}")
                print(yellow + " [!] - Venda acumulada:" + normal + f"R$ {total_vendas:.2f}")
                print(yellow + f" [!] - Sobra:{situacao}{devedor_abatimento_rd}R$ {sobra:.2f}")
                print(yellow + f" [!] - Porcentagem:{normal} {porcentagem:.2f}%")
                sleep(1)
                if quantidade_linhas_meta == quantidade_linhas_venda:
                    print(green + ' [!] - INTEGRIDADE DOS DADOS CONFIRMADA' + normal)
                    print('\n')
                    sleep(1)
                else:
                    print(red + ' [!] - INTEGRIDADE DOS DADOS COMPROMETIDA' + normal)
                    print('\n')
                    sleep(1)
            except ZeroDivisionError:
                sleep(1.5)
                print(yellow + f' [!] - LISTA SEM NUMEROS PARA ANALISAR - [RDMARCAS]' + normal)
                print('\n')
            except Exception as error:
                print(red + f' [!] - ERRO DE {error.__class__}' + normal)


        check_data_RD()


        def check_data_PERFUMARIA():
            try:
                with open("storage/metaAcumuladaPERFUMARIA.txt", "r") as arquivoPERFUMARIAMetas:
                    metas = arquivoPERFUMARIAMetas.readlines()
                    quantidade_linhas_meta = len(metas)
                with open("storage/vendaAcumuladaPERFUMARIA.txt", "r") as arquivoPERFUMARIAVendas:
                    vendas = arquivoPERFUMARIAVendas.readlines()
                    quantidade_linhas_venda = len(vendas)

                metas = [float(meta.strip()) for meta in metas]
                vendas = [float(venda.strip()) for venda in vendas]

                total_metas = sum(metas)
                total_vendas = sum(vendas)
                sobra = abs(total_metas - total_vendas)
                porcentagem = (total_vendas / total_metas) * 100

                # Análise alcance de metas (Opção de integridade)
                devedor_abatimento_perfumaria = abatimento(total_metas, total_vendas)
                if total_vendas < total_metas:
                    situacao = red
                else:
                    situacao = normal

                print(rosa + "Dados da lista de PERFUMARIA:" + normal)
                print(yellow + " [!] - Meta acumulada:" + normal + f"R$ {total_metas:.2f}")
                print(yellow + " [!] - Venda acumulada:" + normal + f"R$ {total_vendas:.2f}")
                print(yellow + f" [!] - Sobra:{situacao}{devedor_abatimento_perfumaria}R$ {sobra:.2f}")
                print(yellow + f" [!] - Porcentagem:{normal} {porcentagem:.2f}%")
                sleep(1)
                if quantidade_linhas_meta == quantidade_linhas_venda:
                    print(green + ' [!] - INTEGRIDADE DOS DADOS CONFIRMADA' + normal)
                    print('\n')
                    sleep(1)
                else:
                    print(red + ' [!] - INTEGRIDADE DOS DADOS COMPROMETIDA' + normal)
                    print('\n')
                    sleep(1)
            except ZeroDivisionError:
                sleep(1.5)
                print(yellow + f' [!] - LISTA SEM NUMEROS PARA ANALISAR - [PERFUMARIA]' + normal)
                print('\n')
            except Exception as error:
                print(red + f' [!] - ERRO DE {error.__class__}' + normal)


        check_data_PERFUMARIA()


        def check_data_DERMO():
            try:
                with open("storage/metaAcumuladaDERMO.txt", "r") as arquivoDERMOMetas:
                    metas = arquivoDERMOMetas.readlines()
                    quantidade_linhas_meta = len(metas)
                with open("storage/vendaAcumuladaDERMO.txt", "r") as arquivoDERMOVendas:
                    vendas = arquivoDERMOVendas.readlines()
                    quantidade_linhas_venda = len(vendas)
                with open("storage/pecaAcumuladaDERMO.txt", "r") as arquivoDERMOPecas:
                    pecas = arquivoDERMOPecas.readlines()

                metas = [float(meta.strip()) for meta in metas]
                vendas = [float(venda.strip()) for venda in vendas]
                pecas = [int(peca.strip()) for peca in pecas]

                total_metas = sum(metas)
                total_vendas = sum(vendas)
                total_pecas = sum(pecas)
                sobra = abs(total_metas - total_vendas)
                porcentagem = (total_vendas / total_metas) * 100

                # Análise alcance de metas (Opção de integridade)
                devedor_abatimento_dermo = abatimento(total_metas, total_vendas)
                if total_vendas < total_metas:
                    situacao = red
                else:
                    situacao = normal

                print(rosa + "Dados da lista de DERMO:" + normal)
                print(yellow + " [!] - Meta acumulada:" + normal + f"R$ {total_metas:.2f}")
                print(yellow + " [!] - Venda acumulada:" + normal + f"R$ {total_vendas:.2f}")
                print(yellow + " [!] - Peças acumuladas:" + normal + f" {total_pecas}Un")
                print(yellow + f" [!] - Sobra:{situacao}{devedor_abatimento_dermo}R$ {sobra:.2f}")
                print(yellow + f" [!] - Porcentagem:{normal} {porcentagem:.2f}%" + normal)
                sleep(1)
                if quantidade_linhas_meta == quantidade_linhas_venda:
                    print(green + ' [!] - INTEGRIDADE DOS DADOS CONFIRMADA' + normal)
                    print('\n')
                    sleep(0.5)
                else:
                    print(red + ' [!] - INTEGRIDADE DOS DADOS COMPROMETIDA' + normal)
                    print('\n')
                    sleep(0.5)
            except ZeroDivisionError:
                sleep(1.5)
                print(yellow + f' [!] - LISTA SEM NUMEROS PARA ANALISAR - [DERMO]' + normal)
                print('\n')
            except Exception as error:
                print(red + f' [!] - ERRO DE {error.__class__}' + normal)


        check_data_DERMO()

    elif decis_registro_exclusao_consulta == '6':
        print('\n')
        print(red + ' [!] - ENCERRANDO A SESSÃO')
        break
