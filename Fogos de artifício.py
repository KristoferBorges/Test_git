import time
import sys

Preto = "\033[0;30m"
Vermelho = "\033[0;31m"
Verde = "\033[0;32m"
Amarelo = "\033[0;33m"
Azul = "\033[0;34m"
Roxo = "\033[0;35m"
Ciano = "\033[0;36m"
Branco = "\033[0;37m"

print('Contagem para os Fogos')
for c in range(10, 0, -1):
    time.sleep(1)
    print(c)
print('Pow Pow POW')
sys.exit()
