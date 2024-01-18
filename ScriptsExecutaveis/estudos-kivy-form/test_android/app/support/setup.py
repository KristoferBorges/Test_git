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
            print("Conectado ao BD com sucesso!")
            self.connected = True

        except Exception as erro:
            self.connected = False
            print("Erro ao conectar com o banco de dados: ", erro)

    def createClients(self, RA, nome, semestre, data, comentario=None):
        """
        Método responsável por cadastrar novos clientes
        """
        # Executando teste de inserção
        try:
            # Definição do cursor
            ponteiro = self.conexao.cursor()

            # Query de inserção
            inserir_dados = f"INSERT INTO clientes VALUES ('{RA}', '{nome}', {semestre}, '{data}', '{comentario}')"

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
    
    def createService(self, nome, valor, dependencia):
        # Executando teste de inserção
        try:
            # Definição do cursor
            ponteiro = self.conexao.cursor()

            # Query de inserção
            inserir_dados = f"INSERT INTO servicos VALUES (default, '{nome}', '{valor}', '{dependencia}')"

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
                self.error = "Serviço já cadastrado"
            return False
        
        except Exception as erro:
            self.conexao.rollback()
            self.error = erro
            print(f"Exceção no arquivo Setup: {erro}")
            return False
        
        finally:
            print("Fechando conexão com o banco de dados...")
            self.conexao.close()

    def registerNewService(self, ra_cliente, id_service, data_registro, data_entrega, valor_cobrado, valor_pendente, ):
        """
        Método responsável por criar um novo serviço com base nos clientes/serviços já cadastrados
        """
        try:
            init_status = "PENDENTE"

            # Definição do cursor
            ponteiro = self.conexao.cursor()

            # Query de inserção
            inserir_dados = f"INSERT INTO cliente_servico VALUES (default, '{ra_cliente}', '{id_service}', '{data_registro}', '{data_entrega}', '{valor_cobrado}', '{valor_pendente}', '{init_status}')"

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
                self.error = "Serviço já cadastrado"
            return False
        
        except Exception as erro:
            self.conexao.rollback()
            self.error = erro
            print(f"Exceção no arquivo Setup: {erro}")
            return False
    
        finally:
            print("Fechando conexão com o banco de dados...")
            self.conexao.close()

    def read_RA(self, ra):
        """
        Método responsável por realizar a busca do RA do cliente
        """
        try:
            self.conectar_banco()
            if self.connected == True:
                ra_cliente = ra
                cursor = self.conexao.cursor()
                cursor.execute(f"SELECT * FROM clientes WHERE ra_cliente = '{ra_cliente}'")
                result = cursor.fetchall()
                if result == []:
                    return False
                else:
                    return True
            else:
                print("Erro ao conectar com o banco de dados!")
        except Exception as erro:
            print(f"Exceção read_RA: {erro}")
        
        finally:
            print("Fechando conexão com o banco de dados...")
            self.conexao.close()

    def read_ID_service(self, id_service):
        """
        Método responsável por realizar a busca do RA do cliente
        """
        try:
            self.conectar_banco()
            if self.connected == True:
                id = id_service
                cursor = self.conexao.cursor()
                cursor.execute(f"SELECT * FROM servicos WHERE id_servico = '{id}'")
                result = cursor.fetchall()
                if result == []:
                    return False
                else:
                    return True
            else:
                print("Erro ao conectar com o banco de dados!")
        except Exception as erro:
            print(f"Exceção read_ID_service: {erro}")
        
        finally:
            print("Fechando conexão com o banco de dados...")
            self.conexao.close()

    def read_clients(self):
        """
        Método que retorna todos os clientes cadastrados no banco de dados
        """
        try:
            self.conectar_banco()
            if self.connected == True:
                cursor = self.conexao.cursor()
                query = "SELECT * FROM clientes"
                cursor.execute(query)
                result = cursor.fetchall()

                return result
            else:
                print("Erro ao encontrar clientes!")
                return False
        
        except Exception as erro:
            print(f"Exceção read_clients: {erro}")

    def update(self):
        pass

    def delete(self):
        pass

