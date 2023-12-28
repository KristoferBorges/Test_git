import os
from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory
from app.support.setup import Setup

class LiveApp(MDApp, App):

    DEBUG = 1 # set this to 0 make live app not working

    # *.kv files to watch
    KV_FILES = {
        # ScreenManager
        # os.path.join(os.getcwd(), "app/screens/screenmanager.kv"),
        os.path.join(os.getcwd(), "app/screens/tests/screenmanager.kv"),

        # Demais screens
        os.path.join(os.getcwd(), "app/screens/login_screen/loginscreen.kv"),
        os.path.join(os.getcwd(), "app/screens/tela_principal/telaprincipal.kv")
    }

    # class to watch from *.py files
    CLASSES = {
        # ScreenManager
        # "MainScreenManager": "app.screens.screenmanager",
        "MainScreenManager": "app.screens.tests.screenmanager",

        # Demais screens
        "LoginScreen": "app.screens.login_screen.loginscreen",
        "TelaPrincipal": "app.screens.tela_principal.telaprincipal",
    }

    # auto reload path
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]


    def build_app(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        Setup()
        return Factory.MainScreenManager()


if __name__ == "__main__":
    LiveApp().run()