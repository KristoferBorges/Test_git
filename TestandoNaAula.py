import pandas

tabela = pandas.read_csv(r"C:\Users\Administrator\Desktop\ExerciciosGit\ConsultaDeMetas\listaRDMARCAS.txt", sep='|')
tabela.to_excel("DadosExcel.xlsx", index=False)
print(tabela)
