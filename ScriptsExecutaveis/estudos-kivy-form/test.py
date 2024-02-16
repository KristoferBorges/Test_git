from app.support.modulo import FunctionsCase

def formatNome(nome):
    """
    Função que limita o tamanho do nome
    """
    space = list()
    nomeFormatado = ""
    primeiroNome = ""
    sobrenome = ""
    nome = FunctionsCase.filtrandoLetras(nome)
    
    for ind, letra in enumerate(nome):
        if letra == " ":
            space.append(ind)
        else:
            pass
    
    primeiroNome = nome[:space[0]].strip()
    sobrenome = nome[space[-1]:].strip()

    print(space)
    print(primeiroNome)
    print(sobrenome)


formatNome("João da Silva")
            
                