def soma():
    """
    --> Função realiza a soma entre números.
    """
    print('\nOpção escolhida - SOMA (Digite 0 para finalizar)')
    while True:
        try:
            numero = float(input('--> DIGITE UM NÚMERO: '))
            if numero == 0:
                break
            else:
                numeros.append(numero)

            if len(numeros) > 1:
                print(f'{numeros[0]} + {numeros[1]} = {numeros[0] + numeros[1]}')
                valor_atual = numeros[0] + numeros[1]
                numeros.clear()
                numeros.append(valor_atual)
        except ValueError:
            print('\n[!] - Digite apenas números - [!]\n')
            continue

def subtracao():
    """
    --> Função realiza a subtração entre números.
    """
    print('\nOpção escolhida - SUBTRAÇÃO (Digite 0 para finalizar)')
    while True:
        try:
            numero = float(input('--> DIGITE UM NÚMERO: '))
            if numero == 0:
                break
            else:
                numeros.append(numero)

            if len(numeros) > 1:
                print(f'{numeros[0]} - {numeros[1]} = {numeros[0] - numeros[1]}')
                valor_atual = numeros[0] - numeros[1]
                numeros.clear()
                numeros.append(valor_atual)
        except ValueError:
            print('\n[!] - Digite apenas números - [!]\n')
            continue
    
def multiplicacao():
    """
    --> Função realiza a multiplicação entre dois números.
    """
    print('\nOpção escolhida - MULTIPLICAÇÃO (Digite 0 para finalizar)')
    while True:
        try:
            numero = float(input('--> DIGITE UM NÚMERO: '))
            if numero == 0:
                break
            else:
                numeros.append(numero)

            if len(numeros) > 1:
                print(f'{numeros[0]} * {numeros[1]} = {numeros[0] * numeros[1]}')
                valor_atual = numeros[0] * numeros[1]
                numeros.clear()
                numeros.append(valor_atual)
        except ValueError:
            print('\n[!] - Digite apenas números - [!]\n')
            continue

def divisao():
    """
    --> Função realiza a divisão entre dois números.
    """
    print('\nOpção escolhida - DIVISÃO (Digite 0 para finalizar)')
    while True:
        try:
            numero = float(input('--> DIGITE UM NÚMERO: '))
            if numero == 0:
                break
            else:
                numeros.append(numero)

            if len(numeros) > 1:
                print(f'{numeros[0]} / {numeros[1]} = {numeros[0] / numeros[1]}')
                valor_atual = numeros[0] / numeros[1]
                numeros.clear()
                numeros.append(valor_atual)
        except ValueError:
            print('\n[!] - Digite apenas números - [!]\n')
            continue

def fluxo_usuario():
    """
    --> Função inicia o fluxo do usuário.
    """
    global numeros
    while True:
        try:
            numeros = []

            operacoes = ["\n1) - Soma", "2) - Subtração", "3) - Multiplicação", "4) - Divisão", "5) - Finalizar"]
            print("Escolha uma operação:")

            for _ in operacoes:
                print(_)
            opcao = int(input("Digite a opção escolhida: "))

            if opcao == 1:
                soma()

            elif opcao == 2:
                subtracao()

            elif opcao == 3:
                multiplicacao()

            elif opcao == 4:
                divisao()

            elif opcao == 5:
                print('\nAgradeço pela utilização do Software!\n   - Kristofer')
                break
        except ValueError:
            print('\n[!] - Digite os números correspondentes - [!]\n')
            continue

fluxo_usuario()