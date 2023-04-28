print('Listagem de números!')
print('Caso queira encerrar digite [00]')
# lista geral
generalList = list()
# odd - ímpar
oddList = list()
# even - par
evenList = list()
while True:
    number = int(input('Digite um número: '))
    if number == 00:
        break
    generalList.append(number)
    if number % 2 == 0:
        evenList.append(number)
    elif number % 2 != 0:
        oddList.append(number)
    else:
        print('Error!')

print(f'Lista geral = {generalList}')
print(f'Lista de números pares = {evenList}')
print(f'Lista de números Ímpares = {oddList}')
