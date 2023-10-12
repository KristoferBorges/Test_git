print("Teste de Loop com while, Michel Macedo")
n = -1
while True:
    n = int(input("1: Soma, 2: Multiplicação, 3: Para Sair "))
#-----------------------------------------------------------------------
    if n==1:
        print("Calculo de Soma")
        
        soma=-1
        while True:
            soma =  int(input("para voltar ao menu principal digite 0, para continuar digite 1: "))
            if soma == 1:       
                n =  int(input("digite um numero"))
            if soma ==0:
                break
#------------------------------------------------------------------------       
    if n==2:
        print("Calculo de Multiplicação:")
        multiplicação=-1
        while True:
            multiplicação =  int(input("para voltar ao menu principal digite 0, para continuar digite 1: "))
            if multiplicação == 1:       
                n =  int(input("digite um numero"))
            if multiplicação ==0:
                break
#------------------------------------------------------------------------
    if n == 3:
        print("Fim do Prgrama")
        break