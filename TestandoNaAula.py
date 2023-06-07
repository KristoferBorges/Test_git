valor = str(input(' [?] - R$'))
while True:
    if valor.isnumeric():
        valor = float(valor)
        break
    else:
        valor = str(input(' [?] - Insira um valor válido R$'))
