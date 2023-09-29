def dividir_numeros(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Não é possível dividir por zero")
        resultado = "Divisão por zero não permitida!"
    return resultado


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

resultado = dividir_numeros(num1, num2)
print(f"O resultado da divisão é: {resultado}")
