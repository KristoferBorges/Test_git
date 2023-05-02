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

# Opção de resposta ao menu
opcao = 0
nome = ''
idade = ''


def tryOption():
    global opcao
    while True:
        try:
            opcao = int(input(yellow + '--> ' + normal))
        except ValueError:
            print(red + 'DIGITE UM NÚMERO INTEIRO VÁLIDO!' + normal)
        except Exception as error:
            print(red + f'ERRO DE {error.__class__}' + normal)
        else:
            if opcao in range(1, 4):
                return opcao
            else:
                print(red + 'APENAS NÚMEROS INTEIROS DAS OPÇÕES LISTADAS!' + normal)


def tryName():
    global nome
    while True:
        try:
            nome = str(input(' [?] Nome: '))
        except Exception as error:
            print(red + f'ERRO DE {error.__class__}')
        else:
            if nome.isalpha():
                return nome
            else:
                print(red + 'APENAS LETRAS!' + normal)


def tryAge():
    global idade
    while True:
        try:
            idade = str(input(' [?] Idade: '))
        except Exception as error:
            print(red + f'ERRO DE {error.__class__}')
        else:
            if idade.isnumeric():
                idade = int(idade)
                return idade
            else:
                print(red + 'APENAS NÚMEROS INTEIROS!' + normal)


while True:
    print('_' * 30 + normal)
    print('{}'.format('MENU PRINCIPAL'.center(30)))
    print('_' * 30)
    print(yellow + '1' + normal + ' - ' + blue + 'Novo registro')
    print(yellow + '2' + normal + ' - ' + blue + 'Ver registros')
    print(yellow + '3' + normal + ' - ' + blue + 'Sair do programa' + normal)
    tryOption()
    if opcao == 1:
        print('_' * 30 + normal)
        print('{}'.format('NOVO CADASTRO'.center(30)))
        print('_' * 30)
        tryName()
        tryAge()
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
