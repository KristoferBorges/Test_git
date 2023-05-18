from selenium import webdriver
import pandas
# import openpyxl
# import numpy
# import time

tabela = pandas.read_excel(r"C:\Users\Administrator\Downloads\commodities.xlsx")

for linha in tabela.index:

    produto = tabela.loc[linha, "Produto"]
    navegador = webdriver.Chrome()
    navegador.get(f"https://www.melhorcambio.com/{produto}-hoje")
    cotacao = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
    cotacao = cotacao.replace(".", "").replace(",", ".")
    tabela.loc[linha, 'Preço Atual'] = float(cotacao)


tabela["Comprar"] = tabela["Preço Atual"] < tabela["Preço Ideal"]
print(tabela)
tabela.to_excel("CommoditiesATT.xlsx", index=False)