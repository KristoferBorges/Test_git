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

    def verFilme(self, cliente, filme):
        return print(f'{cliente} está vendo o filme {filme}')


    def alterarPlano(self, cliente, novo_plano):
        if novo_plano in self.lista_planos:
            if novo_plano != self.plano:
                try:
                    self.plano = novo_plano
                    print(f'[{cliente}], Seu plano foi alterado com sucesso!')
                except Exception as error:
                    print(f'{error.__class__}')
            else:
                raise Exception(f"[!] - PROCESSO INTERROMPIDO! (PLANO [{novo_plano}] JÁ EM USO)")


# Inserção se clientes
cliente_id1 = Cliente("Kristofer", 22, "kristofer.souza@gmail.com", "Master")
cliente_id2 = Cliente("Jhonatam", 23, "jhonatam.souza@gmail.com", "Basic")
cliente_id3 = Cliente("Ramon", 21, "ramon.souza@gmail.com", "Basic")
cliente_id4 = Cliente("Alice", 29, "alice.souza@gmail.com", "Master")

# Uso das funções
cliente_id1.verFilme(cliente_id1.nome, "Homem Aranha")
cliente_id3.alterarPlano(cliente_id3.nome, "Master")
cliente_id2.verFilme(cliente_id2.nome, "Homem De Ferro")
print('\n\n')
# Demonstrativo após alterações
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
print()
print(f" Nome = {cliente_id3.nome}")
print(f" Idade = {cliente_id3.idade}")
print(f" Email = {cliente_id3.email}")
print(f" Plano = {cliente_id3.plano}")
print()
print(f" Nome = {cliente_id4.nome}")
print(f" Idade = {cliente_id4.idade}")
print(f" Email = {cliente_id4.email}")
print(f" Plano = {cliente_id4.plano}")
