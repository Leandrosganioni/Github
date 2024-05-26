from fastapi import FastAPI
from tabela import criar_tabela_vazia, processar_adulanco
local_folder = 'C:\\Users\\usuario\\Documents\\Scripts'
tabela_entrada_xlsx = f'{local_folder}/Adulanco_202404302.xlsx'
tabela_saida_xlsx = f'{local_folder}/Adulanco_202404302_calculada.xlsx'
#entrada = {
#    1: {"variavel": "coletores", "quantidade": 15},
#    2: {"variavel_2": "passadas", "quantidade": 3},
#    3: {"variavel_2": "repeticoes", "quantidade": 4}
#}
numero_coletores = 15
numero_passadas = 3
numero_repeticoes = 4
#teste = criar_tabela_vazia(file_adulanco_xlsx = tabela_entrada_xlsx, numero_coletores = 15, numero_repeticoes=numero_repeticoes)
#processar_adulanco(tabela_entrada_xlsx, tabela_saida_xlsx, numero_passadas)
app = FastAPI()

@app.get("/receber-tabela-vazia")
def receber_tabela_vazia():
    criar_tabela_vazia(file_adulanco_xlsx=tabela_entrada_xlsx, numero_coletores=numero_coletores, numero_repeticoes=numero_repeticoes)
    return {"message": "Tabela vazia criada com sucesso"}

@app.post("/processar-tabela-preenchida")
def processar_tabela():
    processar_adulanco(tabela_entrada_xlsx, tabela_saida_xlsx, numero_passadas)
    return {"message": "Tabela processada com sucesso"}



#@app.post criar
#@app.put att
#@app.delete


