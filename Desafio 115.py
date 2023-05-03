from modulos_k import tryOption
from modulos_k import tryName
from modulos_k import tryAge
from modulos_k import textFormatado
"""
Exercício Python 115a: Vamos criar um menu em Python, usando modularização.
"""

red = '\033[31m'
green = '\033[32m'
yellow = '\033[1;33m'
blue = '\033[34m'
blueBack = '\033[44m'
normal = '\033[m'
redBack = '\033[41m'
greenBack = '\033[42m'
yellowBack = '\033[43m'

while True:
    textFormatado('MENU PRINCIPAL')
    print(yellow + '1' + normal + ' - ' + blue + 'Novo registro')
    print(yellow + '2' + normal + ' - ' + blue + 'Ver registros')
    print(yellow + '3' + normal + ' - ' + blue + 'Sair do programa' + normal)
    opcao = int(input(yellow + '--> ' + normal))
    tryOption(opcao)
    if opcao == 1:
        textFormatado('NOVO CADASTRO')
        nome = str(input(' [?] Nome: '))
        tryName(nome)
        idade = str(input(' [?] Idade: '))
        tryAge(idade)
        with open('pessoas.txt', 'a') as pessoas:
            pessoas.write(f'{nome}' + ';' + f'{idade}\n')
    elif opcao == 2:
        textFormatado('REGISTROS ATUAIS')
        with open('pessoas.txt', 'r') as pessoas:
            linhas = pessoas.readlines()
        for linha in linhas:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<25}{dado[1]:>3} Anos')
    elif opcao == 3:
        print(yellow + 'Programa encerrado, Volte sempre!' + normal)
        break
