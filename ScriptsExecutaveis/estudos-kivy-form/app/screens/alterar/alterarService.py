from kivy.uix.screenmanager import Screen
from app.support.setup import System_Crud

class AlterarService(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.system_crud = System_Crud()
        self.data_from_database = None
        self.dependencia = None

    def mostrarIconSemDependencia(self):
        """
        Método responsável por mostrar o ícone de check
        """
        self.ids.icon_sem_dependencia.opacity = 1
        self.ids.icon_com_dependencia.opacity = 0
        self.dependencia = False

        return self.dependencia
    def mostrarIconComDependencia(self):
        """
        Método responsável por mostrar o ícone de check
        """
        self.ids.icon_sem_dependencia.opacity = 0
        self.ids.icon_com_dependencia.opacity = 1
        self.dependencia = True

        return self.dependencia