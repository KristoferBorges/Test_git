"""
Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a 
possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""

while True:
    try:
        numero_inteiro = int(input('Digite um número inteiro: '))
    except TypeError:
        print('Tipo incorreto!')
    except ValueError:
        print('Tipo incorreto!')
    except Exception as erro:
        print(f'O erro encontrato foi {erro.__cause__}')
    else:
        print(f'Você digitou corretamente o número [{numero_inteiro}]')
        break
while True:
    try:
        numero_real = float(input('Digite um número real: '))
    except TypeError:
        print('Tipo incorreto!')
    except ValueError:
        print('Valor incorreto!')
    except AttributeError:
        print('O valor não é do tipo REAL')
    except Exception as erro:
        print(f'O erro encontrato foi {erro.__cause__}')
    else:
        print(f'Você digitou corretamente o número [{numero_real:,.2f}]')
        break
