class verificaCPF:
    def capturaCPF(cpf):
        cpf = cpf.replace('.', '').replace('-', '')
        cpf = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
        return print(f'Resutlado {cpf}')
    

class Tabuada:
    def input_multiplicador_tabuada():
        multiplicador = 0
        while multiplicador == 0:
            try:
                multiplicador = int(input('Digiter o número da Tabuada: '))
            except ValueError:
                print('Digite um número inteiro')

        return multiplicador