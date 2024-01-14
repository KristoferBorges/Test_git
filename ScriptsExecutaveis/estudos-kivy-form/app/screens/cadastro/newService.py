from datetime import datetime
from kivymd.uix.screen import MDScreen
from kivymd.uix.pickers import MDDatePicker
from app.support.modulo import FunctionsCase
from app.support.setup import System_Crud

class NewService(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.system_crud = System_Crud()
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
        self.data_entrega = value.strftime("%Y-%m-%d")

        instance.dismiss()

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
        try:
            if (self.ids.busca_ra_cliente.text == "") or (self.ids.busca_service.text == "") or (self.ids.valor_cobrado.text == "") or (self.ids.valor_pendente.text == "") or (self.data_entrega == None) or (self.data_atual == None):
                # Pop-up de erro de preenchimento
                FunctionsCase.popup_preenchimento()

            elif (self.system_crud.read_RA(self.ids.busca_ra_cliente.text) == False):
                # Pop-up de RA não encontrado
                FunctionsCase.popup_ra_nao_encontrado()

            elif (self.system_crud.read_ID_service(self.ids.busca_service.text) == False):
                # Pop-up de ID Service não encontrado
                FunctionsCase.popup_id_nao_encontrado()

            else:
                self.system_crud.conectar_banco()
                print(self.data_atual, self.data_entrega)
                if self.system_crud.registerNewService(self.ids.busca_ra_cliente.text, self.ids.busca_service.text, self.data_atual, self.data_entrega, self.ids.valor_cobrado.text, self.ids.valor_pendente.text) == True:
                    self.ids.busca_ra_cliente.text = ""
                    self.ids.busca_service.text = ""
                    self.ids.valor_cobrado.text = ""
                    self.ids.valor_pendente.text = ""
                    self.ids.data_entrega.text = "00/00/0000"
                    self.ids.data_registro.text = "00/00/0000"
                    FunctionsCase.popup_sucesso()
        except Exception as erro:
            print(f"Exceção newService: {erro}")