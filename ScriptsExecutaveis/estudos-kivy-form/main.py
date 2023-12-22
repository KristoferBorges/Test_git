from kivymd.app import MDApp
from kivy.lang import Builder
from app.screens.telas import TelaPrincipal


class Tela(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        Builder.load_file('tela.kv')
        return TelaPrincipal()

if __name__ == '__main__':
    Tela().run()
