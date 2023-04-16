# Solicita ao usuário que insira 5 números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))
num5 = int(input("Digite o quinto número: "))

# Adiciona os números à lista
lista = [num1, num2, num3, num4, num5]

# Ordena a lista do maior para o menor sem usar o método sort()
for i in range(len(lista)):
    for j in range(i+1, len(lista)):
        if lista[i] < lista[j]:
            lista[i], lista[j] = lista[j], lista[i]

# Imprime a lista ordenada do maior para o menor
print("Lista ordenada do maior para o menor:", list(reversed(lista)))
