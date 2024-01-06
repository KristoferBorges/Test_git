from kivymd.uix.screen import MDScreen
from app.support.setup import System_Crud
class CadastroCliente(MDScreen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.system_crud = System_Crud()

    def finalizarCadastroCliente(self):
        """
        Método responsável analisar os campos preenchidos e utilizar a função de cadastro do sistema
        """
        try:
            ra_cliente = self.ids.ra_cliente.text
            nome_cliente = self.ids.nome_cliente.text
            semestre_cliente = self.ids.semestre_cliente.text
            comentario_cliente = self.ids.comentario_cliente.text

            if ra_cliente == "" or nome_cliente == "" or semestre_cliente == "" or comentario_cliente == "":
                self.ids.resultado_preenchimento.color = (1, 0, 0, 1)
                self.ids.resultado_preenchimento.text = "Preencha todos os campos!"
            else:
                self.system_crud.createClients(ra_cliente, nome_cliente, semestre_cliente, comentario_cliente)

            self.ids.resultado_preenchimento.color = (0, 1, 0, 1)
            self.ids.resultado_preenchimento.text = "Cliente cadastrado com sucesso!"
        except Exception as erro:
            self.ids.resultado_preenchimento.color = (1, 0, 0, 1)
            self.ids.resultado_preenchimento.text = "Erro ao cadastrar cliente: "
            print(erro)
        
        finally:
            self.system_crud.conexao.close()