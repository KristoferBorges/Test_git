import platform
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from app.support.setup import Setup

class TelaPrincipal(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Window.size = (800, 600)
    