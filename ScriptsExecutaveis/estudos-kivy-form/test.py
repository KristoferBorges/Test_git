import mysql.connector

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
                    print("RA não encontrado!")
                else:
                    print("RA encontrado!")
            else:
                print("Erro ao conectar com o banco de dados!")
        except Exception as erro:
            print(f"Exceção read_RA: {erro}")
        
        finally:
            self.conexao.close()

System_Crud().read_RA(ra="54676")