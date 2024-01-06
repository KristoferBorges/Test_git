import platform
import mysql.connector
from time import sleep
from kivy.clock import Clock
from kivy.core.window import Window

class Setup():
    """
    Classe responsável por configurar o sistema
    """
    def __init__(self):
        if platform.system() == "Windows":
            Window.size = (800, 694)
        else:
            pass

class UserManager:
    """
    Classe responsável por gerenciar o login e logout do usuário
    """
    def __init__(self):
        self.logged_in = False

    def login(self):
        # Lógica de login
        self.logged_in = True

    def logout(self):
        # Lógica de logout
        self.logged_in = False
        

    def is_user_logged_in(self):
        return self.logged_in

class System_Crud:
    """
    Classe responsável por gerenciar o CRUD do sistema
    """
    def __init__(self):
        self.connected = False
        self.conexao = None
        self.conectar_banco()
        self.error = None

    def conectar_banco(self):
        """
        Método responsável por conectar com o banco de dados
        """
        # Conexão com o banco de dados
        try:
            self.conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="bd_tests",
            )
            print("Conexão com o banco de dados realizada com sucesso!")
            self.connected = True

        except Exception as erro:
            self.connected = False
            print("Erro ao conectar com o banco de dados: ", erro)

    def createClients(self, RA, nome, semestre, comentario=None):
        """
        Método responsável por cadastrar novos clientes
        """
        # Executando teste de inserção
        try:
            # Definição do cursor
            ponteiro = self.conexao.cursor()

            # Query de inserção
            inserir_dados = f"INSERT INTO clientes VALUES ('{RA}', '{nome}', {semestre}, '{comentario}')"

            # Executando a query
            ponteiro.execute(inserir_dados)

            # Efetuando o commit
            self.conexao.commit()
            print("Inserção bem-sucedida!")

            return True

        except mysql.connector.errors.IntegrityError as erro:
            self.conexao.rollback()
            self.error = erro
            print(f"Exceção no arquivo Setup: {erro}")
            if "Duplicate entry" in str(erro):
                self.error = "Usuário já cadastrado"
            return False

        except Exception as erro:
            self.conexao.rollback()
            self.error = erro
            print(f"Exceção no arquivo Setup: {erro}")
            return False

        finally:
            print("Fechando conexão com o banco de dados...")
            self.conexao.close()
        


    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

