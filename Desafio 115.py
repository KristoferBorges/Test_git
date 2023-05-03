from modulos_k import tryOption
from modulos_k import tryName
from modulos_k import tryAge

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
    print('_' * 30 + normal)
    print('{}'.format('MENU PRINCIPAL'.center(30)))
    print('_' * 30)
    print(yellow + '1' + normal + ' - ' + blue + 'Novo registro')
    print(yellow + '2' + normal + ' - ' + blue + 'Ver registros')
    print(yellow + '3' + normal + ' - ' + blue + 'Sair do programa' + normal)
    opcao = int(input(yellow + '--> ' + normal))
    tryOption(opcao)
    if opcao == 1:
        print('_' * 30 + normal)
        print('{}'.format('NOVO CADASTRO'.center(30)))
        print('_' * 30)
        nome = str(input(' [?] Nome: '))
        tryName(nome)
        idade = str(input(' [?] Idade: '))
        tryAge(idade)
        with open('pessoas.txt', 'a') as pessoas:
            pessoas.write(f'{nome}' + ';' + f'{idade}\n')
    elif opcao == 2:
        print('_' * 30 + normal)
        print('{}'.format('REGISTROS ATUAIS'.center(30)))
        print('_' * 30)
        with open('pessoas.txt', 'r') as pessoas:
            linhas = pessoas.readlines()
        for linha in linhas:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<25}{dado[1]:>3} Anos')
    elif opcao == 3:
        print(yellow + 'Programa encerrado, Volte sempre!' + normal)
        break
