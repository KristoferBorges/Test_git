from kivymd.uix.screen import MDScreen
from app.support.setup import System_Crud
from app.support.modulo import FunctionsCase

class ConsultaUnica(MDScreen):
    """
    Classe reposável por gerenciar a tela de consulta única.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.system_crud = System_Crud()
    
    def realizarConsultaUnica(self):
        """
        Método ligado ao botão da interface para realizar a consulta única.
        """
        preenchimento = 0

        try:
            if self.ids.ra_cliente.text != "":
                preenchimento += 1
            if self.ids.id_servico.text != "":
                preenchimento += 1
            if self.ids.id_orcamento.text != "":
                preenchimento += 1
            
            if preenchimento == 0:
                # Popup de preenchimento inválido (Nenhum campo preenchido)
                FunctionsCase.popup_preenchimento()
                preenchimento = 0
                
            elif preenchimento > 1:
                # Popup de preenchimento inválido (Apenas um campo deve ser preenchido)
                FunctionsCase.popup_preenchimento_invalido()
                preenchimento = 0
                
            else:
                # Popup de preenchimento válido (Apenas uma consulta por vez)
                pass
        
        except Exception as error:
            preenchimento = 0
            print(f"Exceção ConsultaÚnica: {error}")
    