import time
import sys

black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
purple = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
normal = "\033[0m"

somador = 0
for c in range(1, 500, 2):
    time.sleep(0.01)
    print(c)
    somador += c
print('Valores somados: {}'.format(somador))
sys.exit()
