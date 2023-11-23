import random

# Desafio 0

print("====== DESAFIO 0 ======\n\n");

cpfCorreto = "170.673.340-20"

def hackearCPF(cpf):
    print("[!] - CPF: " + cpf)

    tentativas = 0
    cpfFalhos = list()
    maxTentativas = 99999
    while True:
        n1 = random.randint(0, 9)
        n2 = random.randint(0, 9)
        n3 = random.randint(0, 9)
        n13 = random.randint(0, 9)
        n14 = random.randint(0, 9)
        cpfDecifrado = cpf[:0] + str(n1) + cpf[1:]
        cpfDecifrado = cpfDecifrado[:1] + str(n2) + cpfDecifrado[2:]
        cpfDecifrado = cpfDecifrado[:2] + str(n3) + cpfDecifrado[3:]
        cpfDecifrado = cpfDecifrado[:12] + str(n13) + cpfDecifrado[13:]
        cpfDecifrado = cpfDecifrado[:13] + str(n14) + cpfDecifrado[14:]
        
        while cpfDecifrado in cpfFalhos:
            n1 = random.randint(0, 9)
            n2 = random.randint(0, 9)
            n3 = random.randint(0, 9)
            n13 = random.randint(0, 9)
            n14 = random.randint(0, 9)
            cpfDecifrado = cpf[:0] + str(n1) + cpf[1:]
            cpfDecifrado = cpfDecifrado[:1] + str(n2) + cpfDecifrado[2:]
            cpfDecifrado = cpfDecifrado[:2] + str(n3) + cpfDecifrado[3:]
            cpfDecifrado = cpfDecifrado[:12] + str(n13) + cpfDecifrado[13:]
            cpfDecifrado = cpfDecifrado[:13] + str(n14) + cpfDecifrado[14:]

        print(f'\n[!] - TENTATIVA = [{tentativas}] - [{maxTentativas}]')
        print(f'[INFO] - {cpfDecifrado}')
        if tentativas == maxTentativas:
            print("\n[!] - CPF não decifrado")
            print(f'[!] - TENTATIVAS = [{maxTentativas}]')
            break
        elif cpfCorreto == cpfDecifrado:
            print(f'\n[!] - CPF DECIFRADO = [{cpfDecifrado}]')
            print(f'[!] - TENTATIVAS FEITAS = [{tentativas}]')
            break
        else:
            cpfFalhos.append(cpfDecifrado)

        tentativas += 1
    
    return cpfDecifrado

    
    


cpf = input("Digite um CPF: ")
hackearCPF(cpf)
end = input("\n\nPressione ENTER para sair...")