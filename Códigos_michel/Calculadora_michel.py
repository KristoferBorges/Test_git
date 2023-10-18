def ler_numeros(operacao):
    """Lê uma lista de números inteiros do usuário."""
    numeros = []
    if operacao == 'soma' or operacao == 1:
        while True:
            numero = input("Digite um número inteiro: ")
            if numero == "=":
                break
            try:
                numero = int(numero)
            except ValueError:
                print("Por favor, digite um número válido.")
                continue
            numeros.append(numero)
        return numeros
    elif operacao == 'subtração' or operacao == 2:
        while True:
            numero = input("Digite um número inteiro: ")
            if numero == "=":
                break
            try:
                numero = int(numero)
            except ValueError:
                print("Por favor, digite um número válido.")
                continue
            numeros.append(numero)
        return numeros
    elif operacao == 'divisao' or operacao == 4:
        repeat = 0
        while True:
            numero = input("Digite um número inteiro: ")
            if numero == "=":
                break
            try:
                numero = int(numero)
            except ValueError:
                print("Por favor, digite um número válido.")
                continue
            repeat += 1
            if repeat > 2:
                resultado = numeros[0] / numeros[1]
                numeros = [resultado]
            numeros.append(numero)
        return numeros
    
    elif operacao == 'multiplicação' or operacao == 3:
        repeat = 0
        while True:
            numero = input("Digite um número inteiro: ")
            if numero == "=":
                break
            try:
                numero = int(numero)
            except ValueError:
                print("Por favor, digite um número válido.")
                continue
            repeat += 1
            if repeat > 2:
                resultado = numeros[0] * numeros[1]
                numeros = [resultado]
            numeros.append(numero)
        return numeros
    
def ler_operacao():
    """Lê uma operação matemática do usuário."""
    operacoes = ["1) - Soma", "2) - Subtração", "3) - Multiplicação", "4) - Divisão", "5) - Finalizar"]
    print("Escolha uma operação:")
    for operacao in operacoes:
        print(operacao)
    operacao = input("Escolha uma operação: ")
    operacao = operacao.lower()
    return operacao

def realizar_operacao(numeros, operacao):
    """Realiza uma operação matemática entre uma lista de números inteiros."""
    resultado = None
    if operacao == "soma" or operacao == 1:
        resultado = sum(numeros)
    elif operacao == "subtração" or operacao == 2:
        resultado = numeros[0] - sum(numeros[1:])
    elif operacao == "multiplicacao" or operacao == 3:
        resultado = numeros[0] * sum(numeros[1:])
    elif operacao == "divisao" or operacao == 4:
        resultado = numeros[0] / sum(numeros[1:])
    elif operacao == "finalizar" or operacao == 5:
        resultado = "Cálculo finalizado"
    return resultado

def main():
    """Função principal."""
    finalizar = False
    continuar = True
    while continuar:
        operacao = ler_operacao()
        numeros = ler_numeros(operacao)
        resultado = realizar_operacao(numeros, operacao)
        print(resultado)
        continuar = input("Deseja continuar calculando? (s/n): ").lower()
        if operacao == "finalizar":
            finalizar = True
            continuar = False

if __name__ == "__main__":
    main()