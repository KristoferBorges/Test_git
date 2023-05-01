"""Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando."""

from modulos_k.moeda import resumo

numero = float(input(' [?] - DIGITE UM VALOR E VEJA SEU:\n -> Dobro\n -> Metade\n -> + 10%\n -> - 10%\n [?] - R$'))
resumo(numero)
