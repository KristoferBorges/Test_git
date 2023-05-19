while True:
    valor = float(input('Valor: '))
    if valor.is_integer():
        print('yes')
        print(valor)
    else:
        print('no')
        print(valor)