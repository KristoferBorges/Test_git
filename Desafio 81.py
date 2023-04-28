print('Escolha números e eu farei uma análise!')
print('Para para digite [00]')

lista = list()
c = 1
while True:
    number = int(input(f'[{c}]- Digite o valor: '))
    if number == 00:
        print('Finished program')
        break
    else:
        lista.append(number)
        c += 1


print(f'Número digitados = {c}')
print(f'Lista de números ordenados {list(sorted(lista))}')
if 5 in lista:
    print('A lista possui o número 5!')
else:
    print('A lista NÃO possui o número 5!')
