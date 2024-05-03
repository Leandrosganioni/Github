import pandas as pd
import matplotlib.pyplot as plt


Resultados = 'Resultados'

df_sexta_folha = pd.read_excel('c:\\Users\\usuario\\Documents\\Scripts\\Teste tabela\\tabela_adulanco.xlsx', sheet_name=Resultados)

largura_aplicacao = df_sexta_folha['Largura de aplicação']
resultado_continuo = df_sexta_folha['Contínuo']
resultado_alternado = df_sexta_folha['Alternado']

plt.plot(df_sexta_folha['Largura de aplicação'], df_sexta_folha['Contínuo'], label = "Contínuo", linestyle='-')
plt.plot(df_sexta_folha['Largura de aplicação'], df_sexta_folha['Alternado'], label = "Alternado", linestyle='--')

nome_arquivo = 'grafico_continuo_alternado.png'

plt.savefig(nome_arquivo, dpi=300)

plt.legend()
plt.plot()
plt.show()
