def calcula_media(numero1, numero2):
  if numero1 >= 0 or numero2 >= 0:
    media = (numero1 + numero2) / 2
    return media
  else:
    print("Não é possível calcular a média de números negativos!")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

media = calcula_media(numero1, numero2)
print("A média é:", media)