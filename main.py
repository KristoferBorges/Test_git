# TEST FILE

import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='registros',
)

# CRUD
cursor = conexao.cursor()
# Escolha de comandos
# Caso for edição = (COMMIT),
# Caso for leitura = (FETCHALL)
# conexao.commit()
# recebimento = cursor.fetchall()


def createMysql():
    # C-REATE
    comando = 'INSERT INTO pessoas (nome, idade, cpf) VALUES ("Kristofer", 34, "92023136874")'
    cursor.execute(comando)
    conexao.commit()


def readMysql():
    # R-EAD
    comando = 'SELECT * FROM registros.pessoas'
    cursor.execute(comando)
    recebimento = cursor.fetchall()
    print(recebimento)


def updateMysql():
    # U-PDATE
    comando = 'UPDATE pessoas SET nome = "Josivaldo" WHERE nome = "Kristofer"'
    cursor.execute(comando)
    conexao.commit()


def deleteMysql():
    # D-ELETE
    comando = 'DELETE FROM pessoas WHERE nome = "josivaldo"'
    cursor.execute(comando)
    conexao.commit()


createMysql()
cursor.close()
conexao.close()
