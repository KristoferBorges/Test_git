# Menu do Programa
n = -1
while True:
    print("1: Soma")
    print("2: Multiplicação")
    print("3: Divisão ")
    print("4: Subtração")
    print("5: Para Sair")
    n = int(input("Escolha uma Opção:"))
#-----------------------------------------------------------------------
    # Soma
    if n==1:
        print("Calculo de Soma")
        
        soma=-1
        while True:
            soma =  int(input("para voltar ao menu principal digite 0, para continuar digite 1: "))
            print("")
          #formula para adição
            if soma == 1:
                
                numeros = []
                while True:
                    numero = float(input("Digite um número: "))
                    numeros.append(numero)

                    if numero == 0:
                        break

                    soma = sum(numeros)

                    print("A soma dos números é", soma)
                
                           # Fim da Formula

            if soma ==0:
                break
#------------------------------------------------------------------------
            # Multiplicação
    if n==2:
        print("Calculo de Multiplicação:")
        multiplicação=-1
        while True:
            multiplicação =  int(input("para voltar ao menu principal digite 0, para continuar digite 1: "))
            if multiplicação == 0:
                    break
        #formula para Mulplicação
            if multiplicação == 1:       
                numeros = []
            print("Para finalizar, digite: sair")
            while True:
                numero = input("Digite um número: ")
                if numero == "sair" :
                    break
                if numero == "0":
                    print("O número 0 não é permitido.")
                    continue
                numeros.append(float(numero))
                multiplicacao = 1

                for numero in numeros:
                    multiplicacao *= numero

                print("A multiplicação dos números é", multiplicacao)
            
            # Fim da Formula
    
#------------------------------------------------------------------------
        # Divisão

    if n==3:
        print("Calculo de Divisão:")
        divisao=-1
        while True:
            divisao =  int(input("para voltar ao menu principal digite 0, para continuar digite 1: "))   
            if divisao == 0:
                break
        #formula para Divisão
            if divisao == 1:       
                numeros = []

            while True:
                numero = input("Digite um número: ")
                if numero == "sair":
                        break
                if numero == "0":
                    print("O número 0 não é permitido.")
                numeros.append(float(numero)) # no caso do armazenamento em lista precisa da conversão para (float ou int)
                divisao = numeros[0]

                for numero in numeros[1:]:
                    divisao /= numero
                    print("A divisão dos números é", divisao)
                    
            # Fim da Formula
    
            
#------------------------------------------------------------------------

        # Subtração

    if n==4:
        print("Calculo de Subtração:")
        subtracao=-1
        while True:
            subtracao =  int(input("para voltar ao menu principal digite 0, para continuar digite 1: "))
            print("")
        #formula para Subtração
            if multiplicação == 1:       
                numeros = []

            while True:
                numero = int(input("Digite um número: "))
                numeros.append(numero)

                if numero == 0:
                    break

                subtracao = numeros[0]

                for numero in numeros[1:]:
                    subtracao -= numero

                    print("A subtração dos números é", subtracao)
            
            # Fim da Formula
    
            if subtracao ==0:
                break
#------------------------------------------------------------------------
# Fim do Programa
            
    if n == 5:
        print("Fim do Programa")
        break