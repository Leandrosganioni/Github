import numpy as np
import math

entrada = {
    "numero_coletores": 33,
    "numero_repeticoes": 5,
    "numero_passadas": 3,
    "distancia_coletores": 0.5,
    #impar ou par
    #num_coletor central
}
#crlt z
valorInicial = [3, 4, 19, 33, 5]
valorMedio = [9, 1 , 10, 30, 13]
valorFim = [2, 3, 500, 20, 15]

import pandas as pd

numero_coletores = entrada['numero_coletores']
numero_repeticoes = entrada['numero_repeticoes']
numero_passadas = entrada['numero_passadas']
distancia_coletores = entrada['distancia_coletores']

file_adulanco_xlsx = 'tabela_adulanco.xlsx'
file_adulanco2_xlsx = 'tabela_adulanco2.xlsx'

def montar_tabela_vazia(numero_coletores , numero_repeticoes):
    print(f'numero de coletores: {numero_coletores} | numero de repeticoes: {numero_repeticoes}')
    colnames = create_colnames(numero_repeticoes=numero_repeticoes)
    rownames = create_rownames(numero_coletores=numero_coletores)
    table = create_named_table(rownames=rownames, colnames=colnames)
    table = reset_total_media(table)
    return table

def create_colnames(numero_repeticoes):
    colnames = []
    for i in range(numero_repeticoes):
        colnames.append(f'Rep. {i+1}')
    colnames.append('Total')
    colnames.append('Média')
    return colnames

def create_rownames(numero_coletores):
    rownames = []
    for i in range(numero_coletores):
        rownames.append(f'Col. {i+1}')
    return rownames

def create_table(nrows, ncols):
    table = pd.DataFrame(index=range(nrows),columns=range(ncols))
    return table

def create_named_table(rownames, colnames):
    table = pd.DataFrame(index=range(len(rownames)),columns=range(len(colnames)))
    table.columns = colnames
    table.index = rownames
    for colname in colnames:
        table[colname] = table[colname].astype(np.float64)
    return table

def reset_total_media(table):
    table['Total'].values[:] = 0
    table['Média'].values[:] = 0
    return table

def fill_values(table, valorInicial, valorMedio, valorFim):
    colnames = table.columns.values[0:len(table.columns)-2]
    for i, colname in enumerate(colnames):
        table[colname].values[0] = valorInicial[i]
        table[colname].values[math.floor(len(table.index)/2)] = valorMedio[i]
        table[colname].values[len(table.index)-1] = valorFim[i]
    return table

def interpolate_table(table):
    new_table = table.interpolate(method='linear')
    return new_table

def calcula_total(table, numero_passadas):
    colnames = table.columns.values[0:len(table.columns)-2]
    for linha in range(len(table.index)):
        table['Total'].values[linha] = sum(table[colnames].values[linha]) / numero_passadas
    return table

def calcula_media(table):
	colnames = table.columns.values[0:len(table.columns)-2]
	for linha in range(len(table.index)):
		table['Média'].values[linha] = table['Total'].values[linha] / len(colnames)
	return table


def criar_tabela_vazia(file_adulanco_xlsx, numero_coletores, numero_repeticoes):
    with pd.ExcelWriter(file_adulanco_xlsx) as writer:
        table_empty = montar_tabela_vazia(numero_coletores=numero_coletores, numero_repeticoes=numero_repeticoes)
        table_empty.to_excel(writer, sheet_name="Empty", index=False)
    return table_empty

def processar_adulanco(tabela_entrada_xlsx, tabela_saida_xlsx, numero_passadas):
    table_values = pd.read_excel(tabela_entrada_xlsx, sheet_name="Empty")
    print(table_values)
    with pd.ExcelWriter(tabela_saida_xlsx) as writer:
        table_interpolated = interpolate_table(table_values)
        table_total = calcula_total(table_interpolated, numero_passadas)
        table_mean = calcula_media(table_total)
        table_mean.to_excel(writer, sheet_name="Results", index=False)
    return tabela_saida_xlsx


# def criar_tabela_geral(file_adulanco_xlsx, numero_coletores, numero_repeticoes):    
#     with pd.ExcelWriter(file_adulanco_xlsx) as writer:

#         table_empty = montar_tabela_vazia(numero_coletores=numero_coletores, numero_repeticoes=numero_repeticoes)
#         table_empty.to_excel(writer, sheet_name="Empty", index=True)

#         table_values = fill_values(table_empty, valorInicial, valorMedio, valorFim)
#         table_values.to_excel(writer, sheet_name="Values", index=True)

#         table_interpolated = interpolate_table(table_values)
#         table_interpolated.to_excel(writer, sheet_name="Interpolated", index=True)

#         table_total = calcula_total(table_interpolated, numero_passadas)
#         table_total.to_excel(writer, sheet_name="Total", index=True)

#         table_mean = calcula_media(table_total)
#         table_mean.to_excel(writer, sheet_name="Média", index=True)
