def calcular():
    operacao = input('''
Digite a operação matemática que deseja realizar:
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')

    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))

    if operacao == '+':
        print('{} + {} = '.format(num1, num2))
        print(num1 + num2)

    elif operacao == '-':
        print('{} - {} = '.format(num1, num2))
        print(num1 - num2)

    elif operacao == '*':
        print('{} * {} = '.format(num1, num2))
        print(num1 * num2)

    elif operacao == '/':
        print('{} / {} = '.format(num1, num2))
        print(num1 / num2)

    else:
        print('Você não digitou um operador válido. Execute o programa novamente.')

calcular()
