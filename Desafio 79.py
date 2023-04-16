lista = list()

print('Digite [00] para dar STOP!')
while True:
    number = int(input('Digite um número para listagem: '))
    if number == 00:
        break
    if number in lista:
        print('Número já registrado!')
    else:
        lista.append(number)
        
lista.sort()
print(lista)
