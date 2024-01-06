from kivy.uix.popup import Popup
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatButton

class FunctionsCase:
    """
    Classe com funções usadas frequentemente no sistema
    """
    def popup_sucesso():
        # Pop-up de sucesso
        content = MDBoxLayout(orientation="vertical", padding="10dp")
        label = MDLabel(text="Cadastro realizado com sucesso", halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf")
        close_button = MDFillRoundFlatButton(text="Concluir", size_hint=(1, None), font_name="app/support/fonts/monofonto.otf")

        content.add_widget(label)
        content.add_widget(close_button)

        popup = Popup(title="", content=content, size_hint=(0.8, 0.5), auto_dismiss=False)
        close_button.bind(on_release=popup.dismiss)
        popup.open()
    
    def popup_error(error):
        # Pop-up de erro
        content = MDBoxLayout(orientation="vertical", padding="10dp")
        label = MDLabel(text="Erro ao cadastrar cliente", halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf")
        close_button = MDFillRoundFlatButton(text="Fechar", size_hint=(1, None), font_name="app/support/fonts/monofonto.otf")

        content.add_widget(label)
        content.add_widget(close_button)

        popup = Popup(title=f"{error}", content=content, size_hint=(0.8, 0.5), auto_dismiss=False)
        close_button.bind(on_release=popup.dismiss)
        popup.open()
    
    def filtrandoLetras(texto):
        """
        Método para filtrar apenas letras de um texto ignorando números ou caracteres especiais
        """
        texto_filtrado = ""
        for letra in texto:
            if letra.isalpha():
                texto_filtrado += letra
            elif letra == " ":
                texto_filtrado += letra

        return texto_filtrado.title()