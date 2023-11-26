import random
import time

# Cor verde
green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
normal = "\033[0m" # to come back to default 

print("====== DESAFIO 0 ======\n\n");
cpfCorreto = input(red + '\n[?] - DIGITE UM CPF PARA DECIFRAR: ' + normal)

def hackearCPF(cpf):
    print(yellow + '[!] - COMEÇANDO A PROCURA EM' + green + ' 3 SEGUNDOS')
    time.sleep(1)
    print(yellow + '[!] - COMEÇANDO A PROCURA EM' + green + ' 2 SEGUNDOS')
    time.sleep(1)
    print(yellow + '[!] - COMEÇANDO A PROCURA EM' + green + ' 1 SEGUNDOS')
    time.sleep(1)

    print(yellow + "[!] - CPF: " + green + cpf)
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
            print(red +"\n[!] - CPF não decifrado")
            print(f'[!] - TENTATIVAS = [{maxTentativas}]')
            break
        elif cpfCorreto == cpfDecifrado:
            print(green + f'\n[!] - CPF DECIFRADO = [{cpfDecifrado}]')
            print(f'[!] - TENTATIVAS FEITAS = [{tentativas}]' + normal)
            break
        else:
            cpfFalhos.append(cpfDecifrado)

        tentativas += 1
    
    return cpfDecifrado

    
    


cpf = input(green + "[?] - DIGITE O CPF ESCONDIDO: " + normal)
hackearCPF(cpf)
end = input('[!] - DIGITE ENTER PARA FINALIZAR')
