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

print(yellow + '=' * 5 + '[Tabuada usando o FOR]' + '=' * 5 + normal)
c = 0
number = int(input('Escolha um número: '))

for c in range(0, 500+1, 1):
    time.sleep(0.1)
    print(purple + '{}x{} = {}'.format(number, c, (number * c)) + normal)

sys.exit()
