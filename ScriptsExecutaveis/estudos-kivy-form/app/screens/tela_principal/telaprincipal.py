import platform
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from app.support.setup import System_Crud, UserManager
from kivy.lang import Builder

class TelaPrincipal(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_manager = UserManager()
        

    def logout(self):
        """
        Método responsável por fazer o logout do usuário ao clicar no botão de logout
        """
        self.user_manager.logout()
        if self.user_manager.is_user_logged_in() == False:
            if platform.system() == "Windows":
                Window.size = (800, 394)
        
        # Ativa a função de resetSpinner
        self.manager.get_screen("login_screen").resetSpinner()

    def verificarConexao(self):
        """
        Médoto que verifica a conexão com o banco de dados, caso esteja conectado irá mostrar um icone, e se não estiver, irá mostrar outro icone
        """
        if System_Crud.connected == True:
            self.ids.conexao_icon.text_color = (0, 1, 0, 1)
            self.ids.conexao_icon.icon_color = (0, 1, 0, 1)
            self.ids.conexao_icon.text = "CONEÇÃO ATIVADA"
        else:
            self.ids.conexao_icon.text_color = (1, 0, 0, 1)
            self.ids.conexao_icon.icon_color = (1, 0, 0, 1)
            self.ids.conexao_icon.text = "CONEÇÃO DESATIVADA"

    