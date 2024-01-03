import platform
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from app.support.setup import Setup, UserManager
from kivy.clock import Clock

class LoginScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_manager = UserManager()

    def realizarLogin(self):
        usuario_login = self.ids.text_login.text
        usuario_senha = self.ids.text_senha.text

        if usuario_login == "admin" and usuario_senha == "admin":
            self.ids.text_login.text = ""
            self.ids.text_senha.text = ""
            self.ids.result_login.text = ""
            self.ids.text_login.hint_text_color = (0, 0, 0, 1)
            self.ids.text_senha.hint_text_color = (0, 0, 0, 1)
            self.manager.current = "tela_principal"

            self.user_manager.login()
            if self.user_manager.is_user_logged_in() == True:
                if platform.system() == "Windows":
                    Window.size = (800, 600)
        else:
            self.ids.text_login.text = ""
            self.ids.text_senha.text = ""
            self.ids.result_login.text = "Login ou senha incorretos"
            self.ids.text_login.hint_text_color = (1, 0, 0, 1)
            self.ids.text_senha.hint_text_color = (1, 0, 0, 1)