# TEST FILE

import datetime


def dateVerification():
    data = str(input('Informe a data atual: '))
    if len(data) == 0:
        data = datetime.datetime.now()
        data = datetime.datetime.date(data)
        data_formatada = data.strftime("%d/%m/%Y")
        print(data_formatada)


dateVerification()
