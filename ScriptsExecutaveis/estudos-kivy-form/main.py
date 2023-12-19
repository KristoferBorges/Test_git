from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from app.screens.telas import MenuPrincipal

class Tela(App):

    def build(self):
        self.title = 'Tela principal'
        adm = ScreenManager()
        return adm

if __name__ == '__main__':
    Tela().run()