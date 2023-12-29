import platform
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from app.support.setup import Setup, UserManager
from kivy.lang import Builder

class TelaPrincipal(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_manager = UserManager()
        

    def logout(self):
        self.user_manager.logout()
        if self.user_manager.is_user_logged_in() == False:
            if platform.system() == "Windows":
                Window.size = (800, 200)
        
