temp = list()
princ = list()
maximo = minimo = 0
stop = ''
while True:
    temp.append(str(input('Name: ')))
    temp.append(float(input('Weight: ')))

    if len(princ) == 0:
        maximo = minimo = temp[1]
    else:
        if temp[1] > maximo:
            maximo = temp[1]
        if temp[1] < minimo:
            minimo = temp[1]
    princ.append(temp[:])
    temp.clear()
    stop = input('Deseja continuar? [S/N]').upper()
    if stop == 'N':
        break

print('\n')
print(f'Quantidade de Registros = {len(princ)}')
print(f'O maior peso foi = {maximo}Kg')
for p in princ:
    if p[1] == maximo:
        print(f'-> {p[0]}', end=' | ')
print('\n')
print(f'O menor peso foi = {minimo}Kg')
for p in princ:
    if p[1] == minimo:
        print(f'-> {p[0]}', end=' | ')
