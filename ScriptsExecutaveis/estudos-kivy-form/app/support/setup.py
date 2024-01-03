import platform
from time import sleep
from kivy.clock import Clock
from kivy.core.window import Window

class Setup():
    def __init__(self):
        if platform.system() == "Windows":
            Window.size = (800, 394)
        else:
            pass

class UserManager:
    def __init__(self):
        self.logged_in = False

    def login(self):
        # Lógica de login
        self.logged_in = True

    def logout(self):
        # Lógica de logout
        self.logged_in = False
        

    def is_user_logged_in(self):
        return self.logged_in