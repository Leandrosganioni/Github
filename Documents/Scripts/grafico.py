import pandas as pd
import matplotlib.pyplot as plt

Resultados = 'Resultados'

df_sexta_folha = pd.read_excel('c:\\Users\\usuario\\Documents\\Scripts\\Teste tabela\\tabela_adulanco.xlsx', sheet_name=Resultados)

largura_aplicacao = df_sexta_folha['Largura de aplicação']
peso = df_sexta_folha['Peso']
plt.bar(df_sexta_folha['Largura de aplicação'], df_sexta_folha['Peso'])

nome_arquivo = 'histograma_largura_peso.png'

plt.savefig(nome_arquivo, dpi=300)
plt.show()
