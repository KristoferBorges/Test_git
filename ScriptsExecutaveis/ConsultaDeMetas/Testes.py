from time import sleep

# Cores
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
ciano = '\033[36m'
normal = '\033[m'
roxo = '\033[35m'
rosa = '\033[95m'


def check_data_RD():
    try:
        with open("storage/metaAcumuladaRDMARCAS.txt", "r") as metaAcumuladaRDMARCAS:
            metas = metaAcumuladaRDMARCAS.readlines()
            quantidade_linhas_meta = len(metas)
        with open("storage/vendaAcumuladaRDMARCAS.txt", "r") as vendaAcumuladaRDMARCAS:
            vendas = vendaAcumuladaRDMARCAS.readlines()
            quantidade_linhas_venda = len(vendas)

        metas = [float(meta.strip()) for meta in metas]
        vendas = [float(venda.strip()) for venda in vendas]

        total_metas = sum(metas)
        total_vendas = sum(vendas)
        sobra = abs(total_metas - total_vendas)
        porcentagem = (total_vendas / total_metas) * 100

        print(rosa + "Dados da lista de RD Marcas:" + normal)
        print(yellow + f" [!] - Meta acumulada: R$ {total_metas:.2f}")
        print(f" [!] - Venda acumulada: R$ {total_vendas:.2f}")
        print(f" [!] - Sobra: R$ {sobra:.2f}")
        print(f" [!] - Porcentagem: {porcentagem:.2f}%" + normal)
        sleep(1.5)
        if quantidade_linhas_meta == quantidade_linhas_venda:
            print(green + ' [!] - INTEGRIDADE DOS DADOS CONFIRMADA' + normal)
            print('\n')
            sleep(1.5)
        else:
            print(red + ' [!] - INTEGRIDADE DOS DADOS COMPROMETIDA' + normal)
            print('\n')
            sleep(1.5)
    except Exception as error:
        print(red + f' [!] - ERRO DE {error.__class__}' + normal)


check_data_RD()


def check_data_PERFUMARIA():
    try:
        with open("storage/metaAcumuladaPERFUMARIA.txt", "r") as metaAcumuladaPERFUMARIA:
            metas = metaAcumuladaPERFUMARIA.readlines()
            quantidade_linhas_meta = len(metas)
        with open("storage/vendaAcumuladaPERFUMARIA.txt", "r") as vendaAcumuladaPERFUMARIA:
            vendas = vendaAcumuladaPERFUMARIA.readlines()
            quantidade_linhas_venda = len(vendas)

        metas = [float(meta.strip()) for meta in metas]
        vendas = [float(venda.strip()) for venda in vendas]

        total_metas = sum(metas)
        total_vendas = sum(vendas)
        sobra = abs(total_metas - total_vendas)
        porcentagem = (total_vendas / total_metas) * 100

        print(rosa + "Dados da lista de PERFUMARIA:" + normal)
        print(yellow + f" [!] - Meta acumulada: R$ {total_metas:.2f}")
        print(f" [!] - Venda acumulada: R$ {total_vendas:.2f}")
        print(f" [!] - Sobra: R$ {sobra:.2f}")
        print(f" [!] - Porcentagem: {porcentagem:.2f}%" + normal)
        sleep(1.5)
        if quantidade_linhas_meta == quantidade_linhas_venda:
            print(green + ' [!] - INTEGRIDADE DOS DADOS CONFIRMADA' + normal)
            print('\n')
            sleep(1.5)
        else:
            print(red + ' [!] - INTEGRIDADE DOS DADOS COMPROMETIDA' + normal)
            print('\n')
            sleep(1.5)
    except Exception as error:
        print(red + f' [!] - ERRO DE {error.__class__}' + normal)


check_data_PERFUMARIA()


def check_data_DERMO():
    try:
        with open("storage/metaAcumuladaDERMO.txt", "r") as metaAcumuladaDERMO:
            metas = metaAcumuladaDERMO.readlines()
            quantidade_linhas_meta = len(metas)
        with open("storage/vendaAcumuladaDERMO.txt", "r") as vendaAcumuladaDERMO:
            vendas = vendaAcumuladaDERMO.readlines()
            quantidade_linhas_venda = len(vendas)
        with open("storage/pecaAcumuladaDERMO.txt", "r") as pecaAcumuladaDERMO:
            pecas = pecaAcumuladaDERMO.readlines()

        metas = [float(meta.strip()) for meta in metas]
        vendas = [float(venda.strip()) for venda in vendas]
        pecas = [int(peca.strip()) for peca in pecas]

        total_metas = sum(metas)
        total_vendas = sum(vendas)
        total_pecas = sum(pecas)
        sobra = abs(total_metas - total_vendas)
        porcentagem = (total_vendas / total_metas) * 100

        print(rosa + "Dados da lista de DERMO:" + normal)
        print(yellow + " [!] - Meta acumulada:" + normal + f" R$ {total_metas:.2f}")
        print(yellow + " [!] - Venda acumulada:" + normal + f" R$ {total_vendas:.2f}")
        print(yellow + " [!] - Peças acumuladas:" + normal + f" {total_pecas}Un")
        print(yellow + " [!] - Sobra:" + normal + f" R$ {sobra:.2f}")
        print(yellow + " [!] - Porcentagem:" + normal + f" {porcentagem:.2f}%" + normal)
        sleep(1.5)
        if quantidade_linhas_meta == quantidade_linhas_venda:
            print(green + ' [!] - INTEGRIDADE DOS DADOS CONFIRMADA' + normal)
            print('\n')
            sleep(1.5)
        else:
            print(red + ' [!] - INTEGRIDADE DOS DADOS COMPROMETIDA' + normal)
            print('\n')
            sleep(1.5)
    except Exception as error:
        print(red + f' [!] - ERRO DE {error.__class__}' + normal)


check_data_DERMO()
