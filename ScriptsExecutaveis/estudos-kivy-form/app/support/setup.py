import platform
from kivy.core.window import Window

class Setup():
    def __init__(self):
        if platform.system() == "Windows":
            Window.size = (800, 200)
        else:
            pass

class UserManager:
    def __init__(self):
        self.logged_in = False

    def login(self):
        # Lógica de login
        # Por exemplo, solicitar credenciais e verificar se estão corretas
        # Se as credenciais estiverem corretas, definir self.logged_in como True
        self.logged_in = True

    def logout(self):
        # Lógica de logout
        # Por exemplo, limpar as credenciais e definir self.logged_in como False
        self.logged_in = False
        

    def is_user_logged_in(self):
        return self.logged_in