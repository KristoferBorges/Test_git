import os
from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory
from app.support.setup import Setup

class LiveApp(MDApp, App):
    """
    Classe principal do sistema, responsável por gerenciar o sistema de programação em tempo real e também gerenciar os caminho dos arquivos .kv/.py
    """
    # Fontes
    font_monofonto = os.path.join(os.getcwd(), "app/support/fonts/monofonto.otf")

    DEBUG = 1 # set this to 0 make live app not working

    # *.kv files to watch
    KV_FILES = {
        # ScreenManager
        # os.path.join(os.getcwd(), "app/screens/screenmanager.kv"),
        os.path.join(os.getcwd(), "app/screens/tests/screenmanager.kv"),

        # Demais screens
        os.path.join(os.getcwd(), "app/screens/login_screen/loginscreen.kv"),
        os.path.join(os.getcwd(), "app/screens/tela_principal/telaprincipal.kv"),
        os.path.join(os.getcwd(), "app/screens/cadastro/cadastroCliente.kv"),
        os.path.join(os.getcwd(), "app/screens/cadastro/cadastroService.kv"),
        os.path.join(os.getcwd(), "app/screens/cadastro/newService.kv"),
        os.path.join(os.getcwd(), "app/screens/consulta/consultaCliente.kv"),
        os.path.join(os.getcwd(), "app/screens/consulta/consultaService.kv"),
        os.path.join(os.getcwd(), "app/screens/consulta/consultaUnica.kv"),
        os.path.join(os.getcwd(), "app/screens/alterar/alterarCliente.kv"),
        os.path.join(os.getcwd(), "app/screens/alterar/alterarService.kv"),
        os.path.join(os.getcwd(), "app/screens/alterar/alterarRegistro.kv"),
    }

    # class to watch from *.py files
    CLASSES = {
        # ScreenManager
        # "MainScreenManager": "app.screens.screenmanager",
        "MainScreenManager": "app.screens.tests.screenmanager",

        # Demais screens
        "LoginScreen": "app.screens.login_screen.loginscreen",
        "TelaPrincipal": "app.screens.tela_principal.telaprincipal",
        "CadastroCliente": "app.screens.cadastro.cadastroCliente",
        "CadastroService": "app.screens.cadastro.cadastroService",
        "NewService": "app.screens.cadastro.newService",
        "ConsultaCliente": "app.screens.consulta.consultaCliente",
        "ConsultaService": "app.screens.consulta.consultaService",
        "ConsultaUnica": "app.screens.consulta.consultaUnica",
        "AlterarCliente": "app.screens.alterar.alterarCliente",
        "AlterarService": "app.screens.alterar.alterarService",
        "AlterarRegistro": "app.screens.alterar.alterarRegistro",
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