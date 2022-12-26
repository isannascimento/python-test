import pandas as pd

planilha = pd.read_excel("./planilhas/Gabarito.xlsx", engine="openpyxl")
print(planilha)