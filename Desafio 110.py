"""
Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
"""

from modulos_k.moeda import resumo

numero = float(input(' [?] - DIGITE UM VALOR E VEJA SEU:\n -> Dobro\n -> Metade\n -> + 10%\n -> - 10%\n [?] - R$'))
resumo(numero)
