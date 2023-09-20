from functions.utilitarian import Tabuada

multiplicador = Tabuada.input_multiplicador_tabuada()

for i in range(1, 10 + 1):
    print(f'{multiplicador} x {i} = {multiplicador * i}')