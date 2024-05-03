from tabela import criar_tabela_vazia, processar_adulanco
#adulancoPrincipal
local_folder = 'C:\\Users\\usuario\\Documents\\Scripts'
tabela_entrada_xlsx = f'{local_folder}/Adulanco_202404302.xlsx'
tabela_saida_xlsx = f'{local_folder}/Adulanco_202404302_calculada.xlsx'
numero_coletores = 15
numero_passadas = 3
numero_repeticoes = 4
teste = criar_tabela_vazia(file_adulanco_xlsx = tabela_entrada_xlsx, numero_coletores = 15, numero_repeticoes=numero_repeticoes)
processar_adulanco(tabela_entrada_xlsx, tabela_saida_xlsx, numero_passadas)