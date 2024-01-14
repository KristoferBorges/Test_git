from datetime import datetime
from kivymd.uix.screen import MDScreen
from kivymd.uix.pickers import MDDatePicker

class NewService(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data_entrega = None
        self.data_atual = datetime.now().strftime("%Y-%m-%d")

    def on_save(self, instance, value, date_range):
        '''

        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;
        :param value: selected date;
        :type value: <class 'datetime.date'>;
        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''

        valueFormated = value.strftime("%d/%m/%Y")
        self.ids.data_entrega.text = valueFormated
        self.data_entrega = value.strftime(format="%Y-%m-%d")

        instance.dismiss()
        return self.data_entrega

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''
        pass

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.title = "DATA DE ENTREGA"
        date_dialog.radius = [20, 7, 20, 7]
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        self.ids.data_registro.text = datetime.now().strftime("%d/%m/%Y")
        date_dialog.open()

    def show_date(self):
        """
        Mostra a data atual ao clicar no botão
        """
        self.ids.data_registro.text = datetime.now().strftime("%d/%m/%Y")

    def finalizarRegistro(self):
        """
        Função responsável por analisar os campos preenchidos e utilizar a função de cadastro do sistema
        """
        pass