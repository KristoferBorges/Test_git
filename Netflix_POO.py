class Cliente:
    def __init__(self, nome, idade, email, plano):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.lista_planos = ["Basic", "Master"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception(f"[!] - PROCESSO INTERROMPIDO! (PLANO [{plano}] INEXISTENTE)")

    def verFilme(self, filme):
        return print(f'{cliente_id1.nome} está vendo o filme {filme}')


    def alterarPlano(self, novo_plano):
        if novo_plano in self.lista_planos:
            if novo_plano != self.plano:
                try:
                    self.plano = novo_plano
                    print('Seu plano foi alterado com sucesso!')
                except Exception as error:
                    print(f'{error.__class__}')
            else:
                raise Exception(f"[!] - PROCESSO INTERROMPIDO! (PLANO [{novo_plano}] JÁ EM USO)")


cliente_id1 = Cliente("Kristofer", 22, "kristofer.souza@gmail.com", "Master")


cliente_id2 = Cliente("Jhonatam", 23, "jhonatam.souza@gmail.com", "Basic")

print('{}'.format("CLIENTES".center(30)))
print(f" Nome = {cliente_id1.nome}")
print(f" Idade = {cliente_id1.idade}")
print(f" Email = {cliente_id1.email}")
print(f" Plano = {cliente_id1.plano}")
print()
print(f" Nome = {cliente_id2.nome}")
print(f" Idade = {cliente_id2.idade}")
print(f" Email = {cliente_id2.email}")
print(f" Plano = {cliente_id2.plano}")
print('\n\n\n\n\n')
cliente_id1.verFilme("Homem Aranha")
cliente_id1.alterarPlano("Basic")

cliente_id2.verFilme("Homem De Ferro")
