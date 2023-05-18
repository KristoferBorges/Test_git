import pandas
import datetime

date = datetime.datetime.now()
date = datetime.datetime.date(date)
data = date.strftime("%d-%m-%Y")
print(type(data))
tabela = pandas.read_csv(r"C:\Users\Administrator\Desktop\ExerciciosGit\ConsultaDeMetas\listaRDMARCAS.txt", sep='|')
nomeArquivo = f"Backup-{data}"
tabela.to_excel(fr"ConsultaDeMetas\backup\{nomeArquivo}.xlsx", index=False)
print(tabela)