import platform
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from app.support.setup import Setup, UserManager

class LoginScreen(MDScreen):
    def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.user_manager = UserManager()

    def realizarLogin(self):
        # Resetando os valores informados na tela de login
        self.ids.text_login.text = ""
        self.ids.text_senha.text = ""

        # Realizando o login
        self.user_manager.login()
        if self.user_manager.is_user_logged_in() == True:
                 if platform.system() == "Windows":
                    Window.size = (800, 600)