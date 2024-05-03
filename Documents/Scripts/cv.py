from tabela import create_rownames, create_named_table, table_mean, numero_coletores, distancia_coletores
import pandas as pd
import numpy as np

file_adulanco = 'c:\\Users\\usuario\\Documents\\Scripts\\Teste\\tabela_adulanco.xlsx'
file_adulanco_xlsx = 'tabela_adulanco.xlsx'

def create_rownames(numero_coletores):
    rownames = [f'Col. {i+1}' for i in range(numero_coletores)]
    return rownames


def create_named_table(rownames, colnames):
    table = pd.DataFrame(index=rownames, columns=colnames)
    table = table.astype(np.float64)  
    return table
#def Alternado(Medias):
    Acumulado_direito = []
    Acumulado_esquerdo = []
    N = len(Medias)
    
    # Calcular acumulado para o lado direito 
    for passo in range(1, N+1):
        acumulado = sum([Medias[n + passo] if 0 <= n + passo < N else 0 for n in range(N)])
        Acumulado_direito.append(acumulado)
    
    # Calcularacumulado par o lado esquerdo 
    for passo in range(1, N+1):
        acumulado = sum([Medias[N-i-1 - passo] if 0 <= N-i-1 - passo < N else 0 for i in range(N)])
        Acumulado_esquerdo.append(acumulado)
    
    return Acumulado_direito, Acumulado_esquerdo
def Alternado(Medias):
    Acumulado = []
    N = len(Medias)
    IdaVolta = [Medias, [Medias.iloc[N-i-1] for i in range(1, N+1)]]
    for passo in range(1, N+1):
        Acumulado.append([sum([IdaVolta[i % 2][n + passo*i] if 0 <= n + passo*i < N else 0 for i in range(-N, N)]) for n in range(N)])
    return Acumulado

def Continuo(Medias):
    Acumulado = []
    N = len(Medias)
    for passo in range(1, N+1):
        Acumulado.append([sum([Medias[n + passo*i] if 0 <= n + passo*i < N else 0 for i in range(-N, N)]) for n in range(N)])
    return Acumulado

def montar_tabela_resultados_vazia():
    colnames = ['Coletor', 'Largura de aplicação','Alternado', 'Contínuo', 'Peso']
    rownames = create_rownames(numero_coletores=numero_coletores)
    table = create_named_table(rownames=rownames, colnames=colnames)
    
    table['Coletor'] = list(range(1, numero_coletores + 1))
    larguras_aplicacao = [(i + 1) * distancia_coletores for i in range(numero_coletores)]
    table['Largura de aplicação'] = larguras_aplicacao
    
    table['Peso'] = table_mean['Média']
    
    Medias = table_mean['Média']
    acumulado_alternado = Alternado(Medias)
   #acumulado_alternado direito = alternado_direito(medias)
   #acumulado_alternado esquerdo = alternado_esquerdo(medias) 
    acumulado_continuo = Continuo(Medias)
    
    cv_alternado = calcula_cv(acumulado_alternado)
   #cv_alternado_direito(acumulado_direito) 
   #cv_alternado_esquerdo(acumulado esquerdo)
    cv_continuo = calcula_cv(acumulado_continuo)
    
    table['Alternado'] = cv_alternado
   #table['Alternado Direito'] = cv_alternado_direito
   #table['Alternado Esquerdo'] = cv_alternado_esquerdo
    table['Contínuo'] = cv_continuo
    
    return table

#cálculo do cv
def calcula_cv(acumulado):
    cv = [100 * np.std(s) / np.average(s) for s in acumulado]
    return cv

table_results = montar_tabela_resultados_vazia()

# Escrever a tabela 
with pd.ExcelWriter(file_adulanco_xlsx, engine='openpyxl', mode='a') as writer:
    table_results.to_excel(writer, sheet_name='Resultados', index=True)