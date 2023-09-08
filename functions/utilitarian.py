class verificaCPF:
    def capturaCPF(cpf):
        cpf = cpf.replace('.', '').replace('-', '')
        cpf = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
        return print(f'Resutlado {cpf}')