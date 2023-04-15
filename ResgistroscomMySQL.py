import mysql.connector

black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
purple = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
normal = "\033[0m"

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


def createMysql(name, age, doc):
    # C-REATE
    comando = f'INSERT INTO pessoas (nome, idade, cpf) VALUES ("{name}", {age}, "{doc}")'
    cursor.execute(comando)
    conexao.commit()


def readMysql():
    # R-EAD
    comando = 'SELECT * FROM registros.pessoas'
    cursor.execute(comando)
    recebimento = cursor.fetchall()
    print('==' * 30)
    print('{:>5} {:>7} {:>21} {:>8}'.format('ID', 'NOME', 'IDADE', 'CPF'))
    print('==' * 30)
    for p in recebimento:
        print(f'   {p[0]:<5} {p[1]:<20} {p[2]:<10} {p[3]}')
    print('==' * 30)
    print()


def updateMysql(column, alter_value, c_id):
    # U-PDATE
    comando = f'UPDATE pessoas SET {column} = "{alter_value}" WHERE idpessoa = "{c_id}"'
    cursor.execute(comando)
    conexao.commit()


def deleteMysql(info):
    # D-ELETE
    comando = f'DELETE FROM pessoas WHERE idpessoa = "{info}"'
    cursor.execute(comando)
    conexao.commit()


while True:
    print(yellow + '==' * 30 + normal)
    print(cyan + '{:>45}'.format('REGISTROS DE PESSOAS (MYSQL)') + normal)
    print(yellow + '==' * 30 + normal + '\n')
    print(' [1] - REGISTRAR\n [2] - CONSULTAR\n [3] - ALTERAR\n [4] - EXCLUIR\n [0] - SAIR\n')
    print(cyan)
    desc = int(input(' [?] - DIGITE O VALOR CORRESPONDENTE\n --> '))
    print(normal)
    if desc == 1:
        # CREATE
        print(yellow + '==' * 30 + normal)
        print(cyan + '{:>44}'.format('OPÇÃO ESCOLHIDA - REGISTROS') + normal)
        print(yellow + '==' * 30 + normal + '\n')
        print(cyan)
        nome = str(input(' [?] - NOME: '))
        idade = int(input(' [?] - IDADE: '))
        cpf = str(input(' [?] - CPF (somente números): '))
        print()
        print(' [!] DADOS RECEBIDOS')
        createMysql(nome, idade, cpf)

    elif desc == 2:
        # READ
        print(yellow + '==' * 30 + normal)
        print(cyan + '{:>44}'.format('OPÇÃO ESCOLHIDA - CONSULTA') + normal)
        print(yellow + '==' * 30 + normal + '\n')
        print()
        print(' [!] - PESSOAS CADASTRADAS ATUALMENTE')
        readMysql()
    elif desc == 3:
        # UPDATE
        print(yellow + '==' * 30 + normal)
        print(cyan + '{:>44}'.format('OPÇÃO ESCOLHIDA - ALTERAÇÃO') + normal)
        print(yellow + '==' * 30 + normal + '\n')
        coluna = str(input(' [?] - QUAL COLUNA: '))
        coluna_id = int(input(' [?] - QUAL O ID: '))
        coluna_subs = str(input(' [?] - QUAL SERÁ A ALTERAÇÃO: '))
        if coluna_subs.isnumeric():
            coluna_subs = int(coluna_subs)
        updateMysql(coluna, coluna_subs, coluna_id)
        print()
        print(' [!] DADOS ALTERADOS')
    elif desc == 4:
        # DELETE
        print(yellow + '==' * 30 + normal)
        print(cyan + '{:>44}'.format('OPÇÃO ESCOLHIDA - EXCLUSÃO') + normal)
        print(yellow + '==' * 30 + normal + '\n')
        print()
        coluna_id = str(input(' [?] - QUAL O ID: '))
        deleteMysql(coluna_id)
        print()
        print(' [!] DADOS EXCLUÍDOS')
    elif desc == 0:
        # EXIT
        print(green + ' [!] VOLTE SEMPRE' + normal)
        break

cursor.close()
conexao.close()
