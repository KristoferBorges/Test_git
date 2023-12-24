from kivymd.uix.screen import MDScreen

class LoginScreen(MDScreen):
    
    def realizarLogin(self):
        # Resetando os valores informados na tela de login
        self.ids.text_login.text = ""
        self.ids.text_senha.text = ""