import csv
from openpyxl import Workbook


def ler_arquivo_csv(nome_arquivo):
    tabela = []
    with open(nome_arquivo, 'r') as arquivo:
        leitor = csv.reader(arquivo, delimiter='|')
        for linha in leitor:
            tabela.append(linha)
    return tabela


def salvar_em_excel(tabela, nome_arquivo_excel):
    workbook = Workbook()
    sheet = workbook.active
    for linha in tabela:
        sheet.append(linha)
    workbook.save(nome_arquivo_excel)


tabela_RDMARCAS = ler_arquivo_csv("listaRDMARCAS.txt")
tabela_PERFUMARIA = ler_arquivo_csv("listaPERFUMARIA.txt")
tabela_DERMO = ler_arquivo_csv("listaDERMO.txt")

nomeArquivoRD = "nome_arquivo_RD.xlsx"
nomeArquivoPERFUMARIA = "nome_arquivo_PERFUMARIA.xlsx"
nomeArquivoDERMO = "nome_arquivo_DERMO.xlsx"

salvar_em_excel(tabela_RDMARCAS, nomeArquivoRD)
salvar_em_excel(tabela_PERFUMARIA, nomeArquivoPERFUMARIA)
salvar_em_excel(tabela_DERMO, nomeArquivoDERMO)
