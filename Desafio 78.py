lista = list()
menorN = 0
maiorN = 0
number = 0
positionMax = 0
positionMin = 0
for c in range(0, 5 + 1):
    number = (int(input(f'[{c}] Número: ')))
    lista.append(number)
    for p, v in enumerate(lista):
        if c == 0:
            maiorN = number
            menorN = number
        elif number > maiorN:
            maiorN = number
        elif number < menorN:
            menorN = number
        if v == maiorN:
            positionMax = p
        if v == menorN:
            positionMin = p


print(lista)
print(f'O maior Número foi {maiorN} na posição {positionMax}º')
print(f'O menor Número foi {menorN} na posição {positionMin}º')
