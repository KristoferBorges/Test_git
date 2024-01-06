from kivymd.uix.screen import MDScreen
from app.support.setup import System_Crud
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.popup import Popup
from kivymd.uix.button import MDFillRoundFlatButton
from app.support.modulo import FunctionsCase
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
            nome_cliente = FunctionsCase.filtrandoLetras(self.ids.nome_cliente.text)
            semestre_cliente = self.ids.semestre_cliente.text
            comentario_cliente = self.ids.comentario_cliente.text

            if (ra_cliente == "") or (nome_cliente == "" or len(nome_cliente) < 5) or (semestre_cliente == ""):
                # Pop-up de erro de preenchimento
                content = MDBoxLayout(orientation="vertical", padding="10dp")
                label = MDLabel(text="Preencha devidamente todos os campos", halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf")
                close_button = MDFillRoundFlatButton(text="Fechar", size_hint=(1, None), font_name="app/support/fonts/monofonto.otf")

                content.add_widget(label)
                content.add_widget(close_button)

                popup = Popup(title="Erro", content=content, size_hint=(0.8, 0.5), auto_dismiss=False)
                close_button.bind(on_release=popup.dismiss)
                popup.open()
            else:
                self.system_crud.conectar_banco()
                if self.system_crud.createClients(ra_cliente, nome_cliente, semestre_cliente, comentario_cliente) == True:
                    self.ids.ra_cliente.text = ""
                    self.ids.nome_cliente.text = ""
                    self.ids.semestre_cliente.text = ""
                    self.ids.comentario_cliente.text = ""
                    FunctionsCase.popup_sucesso()
                else:
                    FunctionsCase.popup_error(f"{self.system_crud.error}")
        except Exception as erro:
            print(f"Exceção cadastroCliente: {erro}")
