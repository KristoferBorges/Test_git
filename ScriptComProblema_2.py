# Script Python com um problema

def calcular_media(lista):
    try:
        total = 0
        for numero in lista:
            total += numero
        media = total / len(lista)
        return media
    except ZeroDivisionError:
        print("\nNão é possível calcular a média de uma lista vazia!")
        return 0

numeros = [1,3,5,6]

media = calcular_media(numeros)
print(f"A média dos números é: {media}")