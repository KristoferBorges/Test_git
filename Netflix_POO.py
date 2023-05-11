class Cliente:
    def __init__(self, nome, idade, email, plano):
        self.nome = nome
        self.idade = idade
        self.email = email
        lista_planos = ["Basic", "Master"]
        if plano in lista_planos:
            self.plano = plano
        else:
            raise Exception("[!] - PROCESSO INTERROMPIDO! (PLANO INEXISTENTE)")


cliente_id1 = Cliente("Kristofer", 21, "kristofer.souza@gmail.com", "Master")
cliente_id2 = Cliente("Jhonatam", 23, "jhonatam.souza@gmail.com", "Basic")
